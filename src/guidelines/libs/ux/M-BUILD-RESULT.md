<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Builders validate in final `.build()` (M-BUILD-RESULT) { #M-BUILD-RESULT }

<why>Concentrating validation in the terminal `.build()` call gives users a single, predictable place where invalid configurations are reported, lets individual setter methods stay infallible and chainable, and makes the success type of the builder unambiguous.</why>
<version>0.1</version>

A builder's per-field setter methods should accept input without failing. All cross-field validation, required-field checks, and other consistency rules belong in the final `.build()` method, which returns a `Result` (or equivalent) carrying any error.

- TODO: State the expected `.build()` signature (e.g., `fn build(self) -> Result<T, BuildError>` vs. infallible `fn build(self) -> T`) and when each is appropriate.
- TODO: Clarify whether setters may ever return `Result` (e.g., for parsing-style inputs) or whether they must always be infallible.
- TODO: Specify how errors should aggregate (single error vs. collected errors for multiple problems).
- TODO: Provide a concrete bad example (a setter that returns `Result`, or validation scattered across setters).
- TODO: Provide a concrete good example (infallible chainable setters; `.build()` returns `Result<T, BuildError>` with a canonical error type per [M-ERRORS-CANONICAL-STRUCTS](#M-ERRORS-CANONICAL-STRUCTS)).
- TODO: Note interaction with [M-INIT-BUILDER](#M-INIT-BUILDER) and [M-INIT-CASCADED](#M-INIT-CASCADED).
