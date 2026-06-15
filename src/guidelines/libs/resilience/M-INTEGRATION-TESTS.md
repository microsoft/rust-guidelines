<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Integration tests live under `tests/` (M-INTEGRATION-TESTS) { #M-INTEGRATION-TESTS }

<why>To keep code files reasonably clean.</why>
<version>0.1</version>

Tests that only touch public API surface are _integration tests_ and belong under `tests/`, not `mod tests {}`.

In projects with coverage targets, it is not uncommon for `src/` files to contain more testing code than actual business logic. This can make browsing and understanding the code harder both in IDEs and PRs. Likewise, if a testing goal can be achieved through either an integration test or a unit test, the former is always preferred.
