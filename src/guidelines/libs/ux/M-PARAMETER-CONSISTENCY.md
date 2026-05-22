<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Parameter ordering is consistent across crates or ecosystem (M-PARAMETER-CONSISTENCY) { #M-PARAMETER-CONSISTENCY }

<why>Consistent parameter order across related APIs reduces cognitive load, prevents argument-swap bugs, and makes it easier to learn and remember a family of functions.</why>
<version>0.1</version>

When the same conceptual parameters appear in multiple functions — within a crate or across crates in the same ecosystem — they should appear in the same order everywhere.

- TODO: Define the precedence when conventions conflict (own crate vs. broader ecosystem vs. `std`).
- TODO: List recurring parameter pairs that need a canonical order (e.g., `src, dst` vs `dst, src`; `key, value`; `haystack, needle`; `expected, actual`).
- TODO: Provide a concrete bad example (two sibling functions with swapped argument order).
- TODO: Provide a concrete good example.
- TODO: Clarify whether this also constrains builder method order, trait method order, or only free/inherent functions.
