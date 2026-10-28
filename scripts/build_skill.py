#!/usr/bin/env python3
"""Build the portable skill download from the canonical guideline sources."""

import argparse
import io
from pathlib import Path, PurePosixPath
import posixpath
import re
from urllib.parse import unquote, urlsplit
import zipfile


NAME = "pragmatic-rust-guidelines"
INCLUDE = re.compile(r"\{\{#include (M-[A-Z-]+\.md)\}\}")


def markdown_cell(text):
    return text.replace("|", "\\|").replace("\n", " ")


def local_target(filename, link):
    url = urlsplit(link)
    if url.scheme or url.netloc or not url.path:
        return None
    return posixpath.normpath(
        str(PurePosixPath(filename).parent / unquote(url.path))
    )


def markdown_links(content):
    text = content.decode("utf-8-sig")
    links = re.findall(r"\]\(([^)\s]+)", text)
    links.extend(re.findall(r"^\[[^\]]+\]:\s+(\S+)", text, re.MULTILINE))
    return links


def rewrite_links(filename, content, files, identifiers):
    def destination(link):
        url = urlsplit(link)
        if url.scheme or url.netloc:
            return link
        if url.fragment in identifiers:
            target = identifiers[url.fragment]
        else:
            target = local_target(filename, link)
            if target is None:
                return link
            readme = target.rstrip("/") + "/README.md"
            if readme in files:
                target = readme
            else:
                return link
        relative = posixpath.relpath(target, str(PurePosixPath(filename).parent))
        return relative + ("#" + url.fragment if url.fragment else "")

    text = content.decode("utf-8-sig")
    text = re.sub(
        r"(\]\()([^\s)]+)(\))",
        lambda match: match[1] + destination(match[2]) + match[3],
        text,
    )
    text = re.sub(
        r"^(\[[^\]]+\]:\s+)(\S+)",
        lambda match: match[1] + destination(match[2]),
        text,
        flags=re.MULTILINE,
    )
    return text.encode()


def validate_links(files):
    for filename, content in files.items():
        if not filename.endswith(".md"):
            continue
        for link in markdown_links(content):
            target = local_target(filename, link)
            if target is not None and target not in files:
                raise ValueError(f"Unbundled reference in {filename}: {link}")


def package_files(root):
    files = {
        "SKILL.md": (root / "skill/SKILL.md").read_bytes(),
        "LICENSE.md": (root / "LICENSE.md").read_bytes(),
    }
    summary = (root / "src/SUMMARY.md").read_text(encoding="utf-8-sig")
    categories = re.findall(
        r"^\s*- \[([^\]]+)\]\(\./guidelines/(.+)/README\.md\)$",
        summary,
        re.MULTILINE,
    )
    guidelines = {}
    memberships = {}
    for title, category in categories:
        readme = root / "src/guidelines" / category / "README.md"
        content = readme.read_text(encoding="utf-8-sig")
        entries = INCLUDE.findall(content)
        memberships[category] = entries
        for name in entries:
            source = readme.parent / name
            text = source.read_text(encoding="utf-8-sig")
            identifier = source.stem
            heading = re.search(
                r"^## (.+) \(" + re.escape(identifier) + r"\) \{",
                text,
                re.MULTILINE,
            )
            if not heading:
                raise ValueError(f"Missing guideline heading: {source}")
            relative = "references/" + source.relative_to(root / "src").as_posix()
            guidelines[identifier] = (relative, heading[1], text)
            files[relative] = source.read_bytes()
        content = INCLUDE.sub(
            lambda match: f"- [{Path(match[1]).stem}]({match[1]}): "
            + guidelines[Path(match[1]).stem][1],
            content,
        )
        files[f"references/guidelines/{category}/README.md"] = content.encode()

    overview = [
        "# Guideline Catalog",
        "",
        "This catalog is generated from Pragmatic Rust Guidelines.",
        "Read the relevant category catalog, then follow its links to individual guidelines.",
        "Draft guidelines are investigation prompts rather than established recommendations.",
        "",
        "| Category | Guidelines |",
        "| --- | --- |",
    ]
    version = re.search(
        r"^Version: (.+)$",
        (root / "src/guidelines/README.md").read_text(encoding="utf-8-sig"),
        re.MULTILINE,
    )
    if version:
        overview[2:2] = [f"Book version: {version[1]}", ""]
    for title, category in categories:
        catalog_path = f"references/catalogs/{category}.md"
        catalog = [
            f"# {title}",
            "",
            "Read the guidelines relevant to the code under investigation.",
            "The reference text, not the catalog keywords, defines each guideline's scope.",
            "",
        ]
        children = [
            (child_title, child)
            for child_title, child in categories
            if str(PurePosixPath(child).parent) == category
        ]
        if children:
            catalog.extend(["| Subcategory | Catalog |", "| --- | --- |"])
            for child_title, child in children:
                link = posixpath.relpath(
                    f"references/catalogs/{child}.md",
                    str(PurePosixPath(catalog_path).parent),
                )
                catalog.append(f"| {child_title} | [{child_title}]({link}) |")
            catalog.append("")
        entries = memberships[category]
        if entries:
            catalog.extend([
                "| Guideline | Description | Keywords | Status |",
                "| --- | --- | --- | --- |",
            ])
        for name in sorted(entries):
            identifier = Path(name).stem
            relative, heading, content = guidelines[identifier]
            draft = "> Draft" in content or "<version>0.1</version>" in content
            keywords = identifier[2:].lower().split("-")
            keywords.extend(re.findall(r"`([^`\n]+)`", content)[:4])
            link = posixpath.relpath(
                relative, str(PurePosixPath(catalog_path).parent)
            )
            catalog.append(
                f"| [{identifier}]({link}) | {markdown_cell(heading)} "
                f"| {markdown_cell(', '.join('`' + word + '`' for word in dict.fromkeys(keywords)))} "
                f"| {'Draft' if draft else 'Not marked as draft'} |"
            )
        files[catalog_path] = ("\n".join(catalog).rstrip() + "\n").encode()
        count = str(len(entries)) if entries else "See subcategories"
        overview.append(f"| [{title}](catalogs/{category}.md) | {count} |")
    files["references/CATALOG.md"] = ("\n".join(overview) + "\n").encode()

    identifiers = {key: value[0] for key, value in guidelines.items()}
    unavailable = {}
    for filename, content in files.items():
        for link in markdown_links(content):
            url = urlsplit(link)
            if not url.scheme and not url.netloc and re.fullmatch(r"M-[A-Z-]+", url.fragment):
                if url.fragment not in identifiers:
                    unavailable.setdefault(url.fragment, set()).add(filename)
    if unavailable:
        notes_path = "references/REFERENCE-NOTES.md"
        notes = [
            "# Reference Notes",
            "",
            "These identifiers appear in source cross-references but have no matching guideline Markdown in this edition.",
            "No missing guideline text is supplied or inferred.",
        ]
        for identifier, sources in sorted(unavailable.items()):
            identifiers[identifier] = notes_path
            notes.extend([
                "",
                f'<a id="{identifier}"></a>',
                "",
                f"## {identifier}",
                "",
                "This guideline is unavailable in this edition.",
                "Do not infer its requirements from the identifier.",
                "",
                "Referenced by:",
                "",
            ])
            for source in sorted(sources):
                link = posixpath.relpath(source, "references")
                notes.append(f"- [{PurePosixPath(source).stem}]({link})")
        files[notes_path] = ("\n".join(notes) + "\n").encode()
        files["references/CATALOG.md"] += (
            "\nSome source cross-references name unavailable guidelines. "
            "Read the [reference notes](REFERENCE-NOTES.md) rather than inferring missing guidance.\n"
        ).encode()
    for filename, content in list(files.items()):
        if filename.endswith(".md"):
            files[filename] = rewrite_links(filename, content, files, identifiers)
    for filename, content in list(files.items()):
        if not filename.endswith(".md"):
            continue
        links = re.findall(r"!\[[^\]]*\]\(([^)\s]+)", content.decode("utf-8-sig"))
        for link in links:
            target = local_target(filename, link)
            if target is None or target in files:
                continue
            if not target.startswith("references/guidelines/"):
                raise ValueError(f"Asset outside guideline sources: {link}")
            source = root / "src" / target.removeprefix("references/")
            data = source.read_bytes()
            if data.startswith(b"version https://git-lfs.github.com/spec/v1"):
                raise ValueError(f"Git LFS asset is not downloaded: {source}")
            files[target] = data
    validate_links(files)
    return files


def build_archive(root):
    output = io.BytesIO()
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for relative, content in sorted(package_files(root).items()):
            info = zipfile.ZipInfo(f"{NAME}/{relative}")
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, content)
    return output.getvalue()


def main():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=root / f"src/agents/{NAME}.zip",
        help="Destination for the self-contained skill ZIP archive.",
    )
    args = parser.parse_args()
    content = build_archive(root)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    if not args.output.exists() or args.output.read_bytes() != content:
        args.output.write_bytes(content)
    print(f"Built {args.output} ({len(content):,} bytes)")


if __name__ == "__main__":
    main()
