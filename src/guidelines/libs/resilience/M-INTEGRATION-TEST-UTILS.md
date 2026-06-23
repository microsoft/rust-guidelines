<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Integration test utilities live in a separate crate (M-INTEGRATION-TEST-UTILS) { #M-INTEGRATION-TEST-UTILS }

<why>To keep test scaffolding reusable across integration tests without polluting the production crate or duplicating helpers per test binary.</why>

For complex projects, shared helpers used by integration tests (fixtures, builders, mock servers, assertion helpers, ...) should live in a dedicated crate rather than inside the production crate or copied between individual `tests/*.rs` files.

- TODO: Define what counts as a "complex project" (e.g., number of integration tests, crates, or helpers that triggers this rule).
- TODO: Specify the recommended crate name / location convention (e.g., sibling `foo-test-utils` crate in the workspace).
- TODO: Clarify the relationship with [M-TEST-UTIL](./#M-TEST-UTIL) (feature-gated helpers within a crate) — when to prefer which.
- TODO: Add a short example showing the crate layout and how integration tests depend on it (likely via `[dev-dependencies]`).
