<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Pin supporting proc macro crates (M-MACRO-VERSION-PIN) { #M-MACRO-VERSION-PIN }

<why>keep generated code compatible with its library</why>

A crate that re-exports macros from companion proc macro crates must pin those dependencies
to its own exact version via `=x.y.z` and publish all related crates at the same time with the
same exact version.

Without exact pins, a newer macro may generate code incompatible with an older version of the
crate, causing unexpected and hard-to-diagnose compilation failures in the generated code.

M-MACRO-VERSION-PIN does not apply to independently consumed macro libraries.

Example:

```toml
# foo/Cargo.toml
[dependencies]
foo_macros = "=1.2.3"
```
