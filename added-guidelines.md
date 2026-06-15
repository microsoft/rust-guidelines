# Guidelines added on this branch

| Name | Text |
|---|---|
| [M-ASYNC-FN](https://github.com/microsoft/rust-guidelines/blob/u/ralfbiedert/2026-05-update/src/guidelines/libs/ux/M-ASYNC-FN.md) | Functions are `async` over returning a Future |
| [M-AVOID-INDIRECTION](https://github.com/microsoft/rust-guidelines/blob/u/ralfbiedert/2026-05-update/src/guidelines/performance/M-AVOID-INDIRECTION.md) | Nested type hierarchies should avoid needless indirection |
| [M-BALANCED-MODULES](https://github.com/microsoft/rust-guidelines/blob/u/ralfbiedert/2026-05-update/src/guidelines/libs/ux/M-BALANCED-MODULES.md) | Modules are balanced in size and scope |
| [M-BOX-DST](https://github.com/microsoft/rust-guidelines/blob/u/ralfbiedert/2026-05-update/src/guidelines/performance/M-BOX-DST.md) | Use boxed slices and strings for immutable owned sequences |
| [M-BUILD-RESULT](https://github.com/microsoft/rust-guidelines/blob/u/ralfbiedert/2026-05-update/src/guidelines/libs/resilience/M-BUILD-RESULT.md) | Builders validate in final `.build()` |
| [M-CARGO-WORKSPACE](https://github.com/microsoft/rust-guidelines/blob/u/ralfbiedert/2026-05-update/src/guidelines/project/M-CARGO-WORKSPACE.md) | Common settings come from the workspace Cargo.toml |
| [M-COLLECTION-TRAITS](https://github.com/microsoft/rust-guidelines/blob/u/ralfbiedert/2026-05-update/src/guidelines/libs/ux/M-COLLECTION-TRAITS.md) | Collections implement the appropriate iter traits |
| [M-CRATES-FLAT-FOLDER](https://github.com/microsoft/rust-guidelines/blob/u/ralfbiedert/2026-05-update/src/guidelines/project/M-CRATES-FLAT-FOLDER.md) | All crates are siblings in one folder |
| [M-CRATES-IN-WORKSPACE](https://github.com/microsoft/rust-guidelines/blob/u/ralfbiedert/2026-05-update/src/guidelines/project/M-CRATES-IN-WORKSPACE.md) | The workspace lists and versions all crates |
| [M-FAST-HASHER](https://github.com/microsoft/rust-guidelines/blob/u/ralfbiedert/2026-05-update/src/guidelines/performance/M-FAST-HASHER.md) | Use a fast hasher where possible |
| [M-FFI-NAMING](https://github.com/microsoft/rust-guidelines/blob/u/ralfbiedert/2026-05-update/src/guidelines/ffi/M-FFI-NAMING.md) | FFI crates follow established naming conventions |
| [M-FFI-TRANSLATES](https://github.com/microsoft/rust-guidelines/blob/u/ralfbiedert/2026-05-update/src/guidelines/ffi/M-FFI-TRANSLATES.md) | Business logic belongs in core crates, FFI only translates |
| [M-FOREIGN-REEXPORTS](https://github.com/microsoft/rust-guidelines/blob/u/ralfbiedert/2026-05-update/src/guidelines/libs/interop/M-FOREIGN-REEXPORTS.md) | Items come from their original crate |
| [M-FROM-ERROR](https://github.com/microsoft/rust-guidelines/blob/u/ralfbiedert/2026-05-update/src/guidelines/libs/ux/M-FROM-ERROR.md) | Canonical error conversion uses `From`, not `map_err` |
| [M-HUMAN-REVIEW](https://github.com/microsoft/rust-guidelines/blob/u/ralfbiedert/2026-05-update/src/guidelines/ai/M-HUMAN-REVIEW.md) | All agent-generated APIs require human review |
| [M-INITIAL-CAPACITY](https://github.com/microsoft/rust-guidelines/blob/u/ralfbiedert/2026-05-update/src/guidelines/performance/M-INITIAL-CAPACITY.md) | Collections are created with sufficient initial capacity |
| [M-INTEGRATION-TESTS](https://github.com/microsoft/rust-guidelines/blob/u/ralfbiedert/2026-05-update/src/guidelines/libs/resilience/M-INTEGRATION-TESTS.md) | Integration tests live under `tests/` |
| [M-LATEST-EDITION](https://github.com/microsoft/rust-guidelines/blob/u/ralfbiedert/2026-05-update/src/guidelines/project/M-LATEST-EDITION.md) | New crates target latest edition |
| [M-LOG-NOT-PRINT](https://github.com/microsoft/rust-guidelines/blob/u/ralfbiedert/2026-05-update/src/guidelines/libs/resilience/M-LOG-NOT-PRINT.md) | Production code uses telemetry, not println |
| [M-LOG-OVERHEAD](https://github.com/microsoft/rust-guidelines/blob/u/ralfbiedert/2026-05-update/src/guidelines/performance/M-LOG-OVERHEAD.md) | Library telemetry does not tank performance |
| [M-MACRO-HELPERS](https://github.com/microsoft/rust-guidelines/blob/u/ralfbiedert/2026-05-update/src/guidelines/macros/M-MACRO-HELPERS.md) | Third party items come from hidden `_private` module |
| [M-MACRO-LAST-RESORT](https://github.com/microsoft/rust-guidelines/blob/u/ralfbiedert/2026-05-update/src/guidelines/macros/M-MACRO-LAST-RESORT.md) | Macros are a last resort |
| [M-MACRO-MAIN-CRATE](https://github.com/microsoft/rust-guidelines/blob/u/ralfbiedert/2026-05-update/src/guidelines/macros/M-MACRO-MAIN-CRATE.md) | Macros assume main crate |
| [M-MACROS-DONT-LIE](https://github.com/microsoft/rust-guidelines/blob/u/ralfbiedert/2026-05-update/src/guidelines/macros/M-MACROS-DONT-LIE.md) | Macros don't lie about signatures |
| [M-MBE-OVER-PROC](https://github.com/microsoft/rust-guidelines/blob/u/ralfbiedert/2026-05-update/src/guidelines/macros/M-MBE-OVER-PROC.md) | Prefer 'macros by example' over proc macros |
| [M-MEM-REUSE](https://github.com/microsoft/rust-guidelines/blob/u/ralfbiedert/2026-05-update/src/guidelines/performance/M-MEM-REUSE.md) | Reuse allocations where possible |
| [M-MSRV](https://github.com/microsoft/rust-guidelines/blob/u/ralfbiedert/2026-05-update/src/guidelines/project/M-MSRV.md) | MSRV is conservatively updated |
| [M-NO-META-DESIGN-DOCUMENTATION](https://github.com/microsoft/rust-guidelines/blob/u/ralfbiedert/2026-05-update/src/guidelines/ai/M-NO-META-DESIGN-DOCUMENTATION.md) | Avoid meta design documentation |
| [M-NO-PRELUDE](https://github.com/microsoft/rust-guidelines/blob/u/ralfbiedert/2026-05-update/src/guidelines/libs/ux/M-NO-PRELUDE.md) | Don't define preludes |
| [M-PANIC-CONTINUATION](https://github.com/microsoft/rust-guidelines/blob/u/ralfbiedert/2026-05-update/src/guidelines/libs/resilience/M-PANIC-CONTINUATION.md) | Panic continuation is last resort |
| [M-PANIC-MESSAGE](https://github.com/microsoft/rust-guidelines/blob/u/ralfbiedert/2026-05-update/src/guidelines/libs/resilience/M-PANIC-MESSAGE.md) | Custom panics have a helpful message |
| [M-PARAMETER-CONSISTENCY](https://github.com/microsoft/rust-guidelines/blob/u/ralfbiedert/2026-05-update/src/guidelines/libs/ux/M-PARAMETER-CONSISTENCY.md) | Parameter ordering is consistent |
| [M-PROC-IMPL](https://github.com/microsoft/rust-guidelines/blob/u/ralfbiedert/2026-05-update/src/guidelines/macros/M-PROC-IMPL.md) | Proc macros should have separate impl crate incl. tests |
| [M-PROC-IMPLIED-ITEMS](https://github.com/microsoft/rust-guidelines/blob/u/ralfbiedert/2026-05-update/src/guidelines/macros/M-PROC-IMPLIED-ITEMS.md) | Proc macros don't produce implied or hidden items |
| [M-RUST-SHAPED](https://github.com/microsoft/rust-guidelines/blob/u/ralfbiedert/2026-05-update/src/guidelines/ai/M-RUST-SHAPED.md) | Rust code solves Rust problems |
| [M-SHORT-NAMES](https://github.com/microsoft/rust-guidelines/blob/u/ralfbiedert/2026-05-update/src/guidelines/universal/M-SHORT-NAMES.md) | Names of items are short |
| [M-SHRINK-TO-FIT](https://github.com/microsoft/rust-guidelines/blob/u/ralfbiedert/2026-05-update/src/guidelines/performance/M-SHRINK-TO-FIT.md) | Shrink collections to fit after building |
| [M-SINGLE-ITEM-PATH](https://github.com/microsoft/rust-guidelines/blob/u/ralfbiedert/2026-05-update/src/guidelines/ai/M-SINGLE-ITEM-PATH.md) | Items are only visible through one path |
| [M-STRONG-TYPES-GUARD](https://github.com/microsoft/rust-guidelines/blob/u/ralfbiedert/2026-05-update/src/guidelines/libs/resilience/M-STRONG-TYPES-GUARD.md) | Newtypes guard their invariants |
| [M-TARGET-CPU](https://github.com/microsoft/rust-guidelines/blob/u/ralfbiedert/2026-05-update/src/guidelines/apps/M-TARGET-CPU.md) | Applications target highest viable target-cpu |
| [M-TAUTOLOGICAL-TESTS](https://github.com/microsoft/rust-guidelines/blob/u/ralfbiedert/2026-05-update/src/guidelines/ai/M-TAUTOLOGICAL-TESTS.md) | Tests do not assert ground truth |
