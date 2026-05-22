<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## All crates are siblings in one folder (M-CRATES-FLAT-FOLDER) { #M-CRATES-FLAT-FOLDER }

<why>To simplify project navigation and follow established Rust standards.</why>
<version>0.1</version>

All crates in a workspace live as direct subdirectories of a single folder (e.g., `crates/`). In rare cases this rule can be broken where two or more aggregation hierarchies exist, such as differentiating unpublished crates from released ones (e.g. `crates/` and `crates_internal/`), or third-party from own (e.g., `vendored/`).

Placing crates inside other crates (at or below their `Cargo.toml`), or even inside their `src/` folder is never acceptable. If a crate relation should be expressed, this is done via common prefixes instead (e.g., `foo`, `foo_util`, `foo_build`).
