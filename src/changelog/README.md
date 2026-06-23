<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

# Changelog

This page tracks notable changes to the Pragmatic Rust Guidelines. 

## 2026.6

The 2026 update substantially expanded the guidelines, adding 42 new entries spanning
macros, performance, project layout, FFI, AI-assisted development, and more:

| Guideline | Title |
|---|---|
| [M-ASYNC-FN](../guidelines/libs/ux/#M-ASYNC-FN) | Functions are `async` over returning a Future |
| [M-ASYNC-STACK-SIZE](../guidelines/performance/#M-ASYNC-STACK-SIZE) | Hot `async` functions reduce stack size |
| [M-AVOID-INDIRECTION](../guidelines/performance/#M-AVOID-INDIRECTION) | Nested type hierarchies should avoid needless indirection |
| [M-BALANCED-MODULES](../guidelines/libs/ux/#M-BALANCED-MODULES) | Modules are balanced in size and scope |
| [M-BOX-DST](../guidelines/performance/#M-BOX-DST) | Use boxed slices and strings for immutable owned sequences |
| [M-BUILD-RESULT](../guidelines/libs/resilience/#M-BUILD-RESULT) | Builders validate in final `.build()` |
| [M-CARGO-WORKSPACE](../guidelines/project/#M-CARGO-WORKSPACE) | Common settings come from the workspace Cargo.toml |
| [M-COLLECTION-TRAITS](../guidelines/libs/ux/#M-COLLECTION-TRAITS) | Collections implement the appropriate iter traits |
| [M-CRATES-FLAT-FOLDER](../guidelines/project/#M-CRATES-FLAT-FOLDER) | All crates are siblings in one folder |
| [M-CRATES-IN-WORKSPACE](../guidelines/project/#M-CRATES-IN-WORKSPACE) | The workspace lists and versions all crates |
| [M-EXAMPLE-OVER-PROC](../guidelines/macros/#M-EXAMPLE-OVER-PROC) | Prefer 'macros by example' over proc macros |
| [M-FAST-HASHER](../guidelines/performance/#M-FAST-HASHER) | Use a fast hasher where possible |
| [M-FFI-NAMING](../guidelines/ffi/#M-FFI-NAMING) | FFI crates follow established naming conventions |
| [M-FFI-TRANSLATES](../guidelines/ffi/#M-FFI-TRANSLATES) | Business logic belongs in core crates, FFI only translates |
| [M-FOREIGN-REEXPORTS](../guidelines/libs/interop/#M-FOREIGN-REEXPORTS) | Items come from their original crate |
| [M-FROM-ERROR](../guidelines/libs/ux/#M-FROM-ERROR) | Canonical error conversion uses `From`, not `map_err` |
| [M-INITIAL-CAPACITY](../guidelines/performance/#M-INITIAL-CAPACITY) | Collections are created with sufficient initial capacity |
| [M-INTEGRATION-TEST-UTILS](../guidelines/libs/resilience/#M-INTEGRATION-TEST-UTILS) | Integration test utilities live in a separate crate |
| [M-INTEGRATION-TESTS](../guidelines/libs/resilience/#M-INTEGRATION-TESTS) | Integration tests live under `tests/` |
| [M-LATEST-EDITION](../guidelines/project/#M-LATEST-EDITION) | New crates target latest edition |
| [M-LOG-NOT-PRINT](../guidelines/libs/resilience/#M-LOG-NOT-PRINT) | Production code uses telemetry, not println |
| [M-LOG-OVERHEAD](../guidelines/performance/#M-LOG-OVERHEAD) | Library telemetry does not tank performance |
| [M-MACRO-HELPERS](../guidelines/macros/#M-MACRO-HELPERS) | Third party items come from hidden `_private` module |
| [M-MACRO-LAST-RESORT](../guidelines/macros/#M-MACRO-LAST-RESORT) | Macros are a last resort |
| [M-MACRO-MAIN-CRATE](../guidelines/macros/#M-MACRO-MAIN-CRATE) | Macros assume main crate |
| [M-MACROS-DONT-LIE](../guidelines/macros/#M-MACROS-DONT-LIE) | Macros don't lie about signatures |
| [M-MEM-REUSE](../guidelines/performance/#M-MEM-REUSE) | Reuse allocations where possible |
| [M-MSRV](../guidelines/project/#M-MSRV) | MSRV is conservatively updated |
| [M-NO-META-DESIGN-DOCUMENTATION](../guidelines/ai/#M-NO-META-DESIGN-DOCUMENTATION) | Avoid meta design documentation |
| [M-NO-PRELUDE](../guidelines/libs/ux/#M-NO-PRELUDE) | Don't define preludes |
| [M-PANIC-CONTINUATION](../guidelines/correctness/#M-PANIC-CONTINUATION) | Panic continuation is last resort |
| [M-PANIC-MESSAGE](../guidelines/correctness/#M-PANIC-MESSAGE) | Custom panics have a helpful message |
| [M-PARAMETER-CONSISTENCY](../guidelines/libs/ux/#M-PARAMETER-CONSISTENCY) | Parameter ordering is consistent |
| [M-PROC-IMPL](../guidelines/macros/#M-PROC-IMPL) | Proc macros should have separate impl crate incl. tests |
| [M-PROC-IMPLIED-ITEMS](../guidelines/macros/#M-PROC-IMPLIED-ITEMS) | Proc macros don't produce implied or hidden items |
| [M-RUST-SHAPED](../guidelines/ai/#M-RUST-SHAPED) | Rust code solves Rust problems |
| [M-SHORT-NAMES](../guidelines/universal/#M-SHORT-NAMES) | Names of items are short |
| [M-SHRINK-TO-FIT](../guidelines/performance/#M-SHRINK-TO-FIT) | Shrink collections to fit after building |
| [M-SINGLE-ITEM-PATH](../guidelines/ai/#M-SINGLE-ITEM-PATH) | Items are only visible through one path |
| [M-STRONG-TYPES-GUARD](../guidelines/libs/resilience/#M-STRONG-TYPES-GUARD) | Newtypes guard their invariants |
| [M-TARGET-CPU](../guidelines/apps/#M-TARGET-CPU) | Applications target highest viable target-cpu |
| [M-TAUTOLOGICAL-TESTS](../guidelines/ai/#M-TAUTOLOGICAL-TESTS) | Tests do not assert ground truth |


## 2025

Initial release of the Pragmatic Rust Guidelines.
