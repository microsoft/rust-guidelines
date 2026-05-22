<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Production code uses telemetry, not println (M-LOG-NOT-PRINT) { #M-LOG-NOT-PRINT }

<why>`println!` / `eprintln!` / `dbg!` bypass log levels, structured fields, sampling, sinks, and filters; they pollute stdout/stderr in ways that are invisible to telemetry pipelines and uncontrollable in production.</why>
<version>0.1</version>

Production code paths should emit diagnostics through the project's telemetry framework (e.g., `tracing`, `log`) rather than via `println!`, `eprintln!`, `print!`, `eprint!`, or `dbg!`. Console output is reserved for CLI binaries that intentionally write to stdout/stderr as their user interface.

- TODO: Enumerate the legitimate exceptions (CLI binaries' user-facing output, build scripts, examples, tests).
- TODO: Specify the recommended telemetry stack or refer to a separate decision (e.g., `tracing` with structured fields per M-LOG-STRUCTURED).
- TODO: Provide a concrete bad example (a library function calling `eprintln!("failed: {e}")` instead of `tracing::error!`).
- TODO: Provide a concrete good example.
- TODO: Note guidance for `dbg!` — banned in committed code; lint enforcement suggested.
- TODO: Note interaction with M-LOG-STRUCTURED.
