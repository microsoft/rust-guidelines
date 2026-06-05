<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Production code uses telemetry, not println (M-LOG-NOT-PRINT) { #M-LOG-NOT-PRINT }

<why>To ensure diagnostics are available where they need to be.</why>
<version>0.1</version>

Production code paths should emit diagnostics through the project's telemetry framework rather than via `println!` or `dbg!`. Console output is reserved for CLIs that intentionally write to stdout as their user interface.
