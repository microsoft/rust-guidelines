## Crate and its dependencies have a permissive license (C-PERMISSIVE)

The software produced by the Rust project is dual-licensed, under either the
[MIT] or [Apache 2.0] licenses. Crates that simply need the maximum
compatibility with the Rust ecosystem are recommended to do the same, in the
manner described herein. Other options are described below.

These API guidelines do not provide a detailed explanation of Rust's license,
but there is a small amount said in the [Rust FAQ]. These guidelines are
concerned with matters of interoperability with Rust, and are not comprehensive
over licensing options.

[MIT]: https://github.com/rust-lang/rust/blob/master/LICENSE-MIT
[Apache 2.0]: https://github.com/rust-lang/rust/blob/master/LICENSE-APACHE
[Rust FAQ]: https://github.com/dtolnay/rust-faq#why-a-dual-mitasl2-license

To apply the Rust license to your project, define the `license` field in your
`Cargo.toml` as:

```toml
[package]
name = "..."
version = "..."
authors = ["..."]
license = "MIT OR Apache-2.0"
```

Then add the files `LICENSE-APACHE` and `LICENSE-MIT` in the repository root,
containing the text of the licenses (which you can obtain, for instance, from
choosealicense.com, for [Apache-2.0](https://choosealicense.com/licenses/apache-2.0/)
and [MIT](https://choosealicense.com/licenses/mit/)).

And toward the end of your README.md:

```
## License

Licensed under either of

 * Apache License, Version 2.0
   ([LICENSE-APACHE](LICENSE-APACHE) or <http://www.apache.org/licenses/LICENSE-2.0>)
 * MIT license
   ([LICENSE-MIT](LICENSE-MIT) or <http://opensource.org/licenses/MIT>)

at your option.

## Contribution

Unless you explicitly state otherwise, any contribution intentionally submitted
for inclusion in the work by you, as defined in the Apache-2.0 license, shall be
dual licensed as above, without any additional terms or conditions.
```

Besides the dual MIT/Apache-2.0 license, another common licensing approach used
by Rust crate authors is to apply a single permissive license such as MIT or
BSD. This license scheme is also entirely compatible with Rust's, because it
imposes the minimal restrictions of Rust's MIT license.

Crates that desire perfect license compatibility with Rust are not recommended
to choose only the Apache license. The Apache license, though it is a permissive
license, imposes restrictions beyond the MIT and BSD licenses that can
discourage or prevent their use in some scenarios, so Apache-only software
cannot be used in some situations where most of the Rust runtime stack can.

The license of a crate's dependencies can affect the restrictions on
distribution of the crate itself, so a permissively-licensed crate should
generally only depend on permissively-licensed crates.
