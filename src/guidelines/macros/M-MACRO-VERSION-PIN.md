<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Pin supporting proc macro crates (M-MACRO-VERSION-PIN) { #M-MACRO-VERSION-PIN }

<why>keep generated code compatible with its library</why>

A crate that re-exports macros from a companion proc macro crates must pin those dependencies
to its own exact version via `=x.y.z` and publish all related crates at the same time with the
same exact version.

Without exact pins, a newer macro may generate code incompatible with older crate's version
causing unexpected and hard to diagnose compilation failures in the generated code.

M-MACRO-VERSION-PIN does not apply to independently consumed macro libraries.

Example:

```toml
# my_crate/Cargo.toml
[package]
version = "1.2.3"

[dependencies]
my_crate_macros = "=1.2.3"

# my_crate_macros/Cargo.toml
[package]
version = "1.2.3"

[dependencies]
my_crate_macros_impl = "=1.2.3"

# my_crate_macros_impl/Cargo.toml
[package]
version = "1.2.3"
```
