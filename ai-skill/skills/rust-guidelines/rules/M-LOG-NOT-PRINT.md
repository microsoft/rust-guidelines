## Production code uses telemetry, not println (M-LOG-NOT-PRINT)

Why: diagnostics available where they are needed.

Production code paths should emit diagnostics through the project's telemetry framework rather than via `println!` or `dbg!`. Console output is reserved for CLIs that intentionally write to stdout as their user interface.
