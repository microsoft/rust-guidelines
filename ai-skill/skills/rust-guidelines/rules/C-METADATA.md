## Cargo.toml includes all common metadata (C-METADATA)

The `[package]` section of `Cargo.toml` should include the following
values:

- `authors`
- `description`
- `license`
- `repository`
- `keywords`
- `categories`

In addition, there are two optional metadata fields:

- `documentation`
- `homepage`

By default, *crates.io* links to documentation for the crate on [*docs.rs*]. The
`documentation` metadata only needs to be set if the documentation is hosted
somewhere other than *docs.rs*, for example because the crate links against a
shared library that is not available in the build environment of *docs.rs*.

[*docs.rs*]: https://docs.rs

The `homepage` metadata should only be set if there is a unique website for the
crate other than the source repository or API documentation. Do not make
`homepage` redundant with either the `documentation` or `repository` values. For
example, serde sets `homepage` to *https://serde.rs*, a dedicated website.
