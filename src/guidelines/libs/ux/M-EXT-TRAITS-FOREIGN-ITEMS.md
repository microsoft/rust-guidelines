<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Extension traits are reserved for foreign items (M-EXT-TRAITS-FOREIGN-ITEMS) { #M-EXT-TRAITS-FOREIGN-ITEMS }

<why>Extension traits add API surface and import friction; they are only justified when inherent methods or owned traits aren't possible because the target type is foreign.</why>
<version>0.1</version>

- TODO: Define what counts as an "extension trait" (e.g., a trait whose primary purpose is to add methods to a type owned by another crate via `impl Ext for ForeignType`).
- TODO: Specify when extension traits are acceptable (foreign types from `std` or third-party crates) vs. when they must not be used (types owned by the current crate — use inherent impls or a regular trait instead).
- TODO: Clarify naming, sealing, and visibility expectations for such traits.
- TODO: Provide good/bad examples.
