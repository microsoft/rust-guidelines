<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Common settings come from the workspace Cargo.toml (M-CARGO-WORKSPACE) { #M-CARGO-WORKSPACE }

<why>To ensure consistent, maintainable project configuration.</why>
<version>0.1</version>

Any repo with two or more crates that somehow belong together should unify these crates with a workspace `Cargo.toml`. Members then inherit shared metadata and dependency versions from the workspace root via `[workspace.dependencies]`, `[workspace.lints]`, ... rather than duplicating these values in each crate. 

Where a dependency is crate-specific, it should still be defined in the workspace. Workspace definitions should generally not enable dependency features (except basic ones such as `["std"]`), and should instead use `default-features = false`.
