# Pragmatic Rust Guidelines

A collection of pragmatic design guidelines helping developers to produce idiomatic Rust that scales.

👉 [**Pragmatic Rust Guidelines**](https://microsoft.github.io/rust-guidelines)

## Agent Skill

Use the [Pragmatic Rust Guidelines agent skill](src/agents/README.md) in your own Rust repository.
The downloadable package contains instructions, category catalogs, the guideline Markdown, and its supporting images.
Agents can read relevant guidelines without loading the entire book or checking out this repository.

## Development

The guidelines use [mdbook](https://github.com/rust-lang/mdBook). Once installed you can view them locally via

```bash
mdbook serve --open
```

To build the distributable skill download, run:

```bash
python3 scripts/build_skill.py
```

The archive is generated at `src/agents/pragmatic-rust-guidelines.zip` and included in the published book.
The `skill/` directory contains the packaging template, not a skill installed for this repository.
The build requires the guideline images to be downloaded through Git LFS.

To submit new guidelines, file a PR. They should be

- beneficial for { safety, COGs, maintenance },
- agreeable to a majority of experienced (3+ years) Rust developers,
- comprehensible to Rust novices (4+ weeks),
- practically applicable in real world scenarios.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft trademarks or logos is
subject to and must follow Microsoft’s Trademark & Brand Guidelines. Use of Microsoft trademarks or logos in modified versions of this
project must not cause confusion or imply Microsoft sponsorship. Any use of third-party trademarks or logos are subject to those
third-party’s policies.
