import io
from pathlib import Path
import tempfile
import unittest
import zipfile

from build_skill import build_archive, package_files, validate_links


class BuildSkillTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        sources = {
            "LICENSE.md": "Test license\n",
            "skill/SKILL.md": "# Skill\n\n[Catalog](references/CATALOG.md)\n",
            "src/SUMMARY.md": (
                "# Summary\n\n- [Universal](./guidelines/universal/README.md)\n"
                "- [Libraries](./guidelines/libs/README.md)\n"
                "  - [UX](./guidelines/libs/ux/README.md)\n"
            ),
            "src/guidelines/README.md": "# About\n\nVersion: test\n",
            "src/guidelines/universal/README.md": (
                "# Universal\n\n{{#include M-CHECK.md}}\n"
            ),
            "src/guidelines/universal/M-CHECK.md": (
                "## Check code (M-CHECK) { #M-CHECK }\n\n"
                "> Draft guideline. Examples needed.\n\n"
                "Use `Clippy`, `Result<T, _>`, and [errors](../libs/ux/#M-ERROR).\n"
                "[UX](../libs/ux/)\n\n![Example](example.png)\n"
            ),
            "src/guidelines/libs/README.md": "# Libraries\n\n[UX](./ux/)\n",
            "src/guidelines/libs/ux/README.md": (
                "# UX\n\n{{#include M-ERROR.md}}\n"
            ),
            "src/guidelines/libs/ux/M-ERROR.md": (
                "## Use errors (M-ERROR) { #M-ERROR }\n\nUse error values.\n"
                "[M-CHECK]: ../../universal/#M-CHECK\n"
            ),
            "src/guidelines/universal/M-UNPUBLISHED.md": "Not a published guideline.\n",
        }
        for name, content in sources.items():
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)
        (self.root / "src/guidelines/universal/example.png").write_bytes(b"\x89PNG\r\n\x1a\n")

    def test_portable_bundle_covers_nested_catalogs_and_images(self):
        first = build_archive(self.root)
        self.assertEqual(first, build_archive(self.root))
        with zipfile.ZipFile(io.BytesIO(first)) as archive:
            self.assertIsNone(archive.testzip())
            prefix = "pragmatic-rust-guidelines/"
            names = archive.namelist()
            self.assertFalse(any("UNPUBLISHED" in name for name in names))
            self.assertEqual(
                archive.read(prefix + "references/guidelines/universal/example.png"),
                b"\x89PNG\r\n\x1a\n",
            )
            catalog = archive.read(prefix + "references/catalogs/universal.md").decode()
            self.assertIn("[M-CHECK](../guidelines/universal/M-CHECK.md)", catalog)
            self.assertIn("Clippy", catalog)
            self.assertIn("`Result<T, _>`", catalog)
            self.assertIn("| Draft |", catalog)
            nested = archive.read(prefix + "references/catalogs/libs/ux.md").decode()
            self.assertIn("../../guidelines/libs/ux/M-ERROR.md", nested)
            self.assertIn("| Not marked as draft |", nested)
            parent = archive.read(prefix + "references/catalogs/libs.md").decode()
            self.assertIn("[UX](libs/ux.md)", parent)
            readme = archive.read(prefix + "references/guidelines/universal/README.md")
            self.assertNotIn(b"{{#include", readme)
            self.assertIn(prefix + "LICENSE.md", names)
        source = self.root / "src/guidelines/libs/ux/M-ERROR.md"
        source.write_text(source.read_text() + "\nUpdated source content.\n")
        self.assertNotEqual(first, build_archive(self.root))

    def test_aggregate_links_resolve_to_individual_guidelines(self):
        files = package_files(self.root)
        text = files["references/guidelines/universal/M-CHECK.md"].decode()
        self.assertIn("[errors](../libs/ux/M-ERROR.md#M-ERROR)", text)
        self.assertIn("[UX](../libs/ux/README.md)", text)
        nested = files["references/guidelines/libs/ux/M-ERROR.md"].decode()
        self.assertIn("[M-CHECK]: ../../universal/M-CHECK.md#M-CHECK", nested)
        validate_links(files)

    def test_missing_and_lfs_pointer_assets_reject_incomplete_package(self):
        asset = self.root / "src/guidelines/universal/example.png"
        asset.unlink()
        with self.assertRaises(FileNotFoundError):
            package_files(self.root)
        asset.write_bytes(b"version https://git-lfs.github.com/spec/v1\n")
        with self.assertRaisesRegex(ValueError, "Git LFS asset is not downloaded"):
            package_files(self.root)

    def test_reference_outside_bundle_is_rejected(self):
        source = self.root / "src/guidelines/universal/M-CHECK.md"
        source.write_text(source.read_text() + "\n[Missing](../../../outside.md)\n")
        with self.assertRaisesRegex(ValueError, "Unbundled reference"):
            package_files(self.root)

    def test_unavailable_guideline_is_flagged_without_inventing_content(self):
        source = self.root / "src/guidelines/universal/M-CHECK.md"
        source.write_text(source.read_text() + "\n[Unavailable](../libs/ux/#M-MISSING)\n")
        files = package_files(self.root)
        text = files["references/guidelines/universal/M-CHECK.md"].decode()
        self.assertIn("[Unavailable](../../REFERENCE-NOTES.md#M-MISSING)", text)
        notes = files["references/REFERENCE-NOTES.md"].decode()
        self.assertIn('<a id="M-MISSING"></a>', notes)
        self.assertIn("This guideline is unavailable", notes)
        self.assertIn("guidelines/universal/M-CHECK.md", notes)
        validate_links(files)


if __name__ == "__main__":
    unittest.main()
