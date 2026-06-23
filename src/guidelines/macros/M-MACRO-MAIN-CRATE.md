<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Macros assume main crate (M-MACRO-MAIN-CRATE) { #M-MACRO-MAIN-CRATE }

<why>To simplify macro logic.</why>
<version>0.1</version>

Procedural macros can (and should) assume they are used through their main crate and emit paths for that.

For crates including proc macros it is common to ship them split in 3 for technical reasons:

- `foo` - the main crate that re-exports macros from `foo_proc`, along with extra traits or types,
- `foo_proc` - facade re-exporting macros from `foo_proc_impl` with `proc-macro = true`,
- `foo_proc_impl` - the actual macro implementation and unit tests.

In some cases there can be additional crates involved. Authors might be tempted to make `foo`, `foo_proc`, and siblings all work, resulting in complex re-export hierarchies or the use of 3rd party helpers. In reality, the minimal UX gain is usually not worth the added complexity (or compile time overhead), given the ecosystem precedent of mostly not supporting these usage modes in the first place.

This also implies you should not attempt to support use cases where your crate is imported under a different name.
