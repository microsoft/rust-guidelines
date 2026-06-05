<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Canonical error conversion uses `From`, not `map_err` (M-FROM-ERROR) { #M-FROM-ERROR }

<why>When `From<SourceError>` is implemented for the function's error type, the `?` operator converts automatically; sprinkling `.map_err(...)` at call sites duplicates that mapping, hides it from review, and lets variants drift as new conversions are added in different places.</why>
<version>0.1</version>

Conversions between error types that are part of the project's canonical error hierarchy should be implemented as `impl From<SourceError> for TargetError` (typically via `#[from]` on a `thiserror`-style derive or an explicit impl) and used implicitly via `?`. Call sites should not reach for `.map_err(...)` to perform the same conversion repeatedly.

- TODO: Specify when `map_err` is still appropriate (one-off context attachment, lossy summarization, conversions that depend on local context the `From` impl cannot see).
- TODO: Clarify the policy for canonical error structs (cf. [M-ERRORS-CANONICAL-STRUCTS](#M-ERRORS-CANONICAL-STRUCTS)) — each source error gets at most one `From` impl per target.
- TODO: Provide a concrete bad example (every call site doing `.map_err(MyError::Io)?` for `std::io::Error`).
- TODO: Provide a concrete good example (`impl From<std::io::Error> for MyError` once; call sites use `?` directly).
- TODO: Note interaction with [M-ERRORS-CANONICAL-STRUCTS](#M-ERRORS-CANONICAL-STRUCTS) and [M-APP-ERROR](../../apps/#M-APP-ERROR).
