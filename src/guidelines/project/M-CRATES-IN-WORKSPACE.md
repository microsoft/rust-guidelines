<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## The workspace lists and versions all crates (M-CRATES-IN-WORKSPACE) { #M-CRATES-IN-WORKSPACE }

<why>To simplify inter-crate dependencies and debugging.</why>
<version>0.1</version>

Every crate produced by the project should be listed as a workspace member, and its version should be declared in `[workspace.dependencies]` so that intra-workspace dependencies resolve to a single canonical version.

```toml
# Bad, crate links its sibling directly
[dependencies]
sibling.path = "../sibling"


# Good, going through workspace
[dependencies]
sibling.workspace = true

[workspace.dependencies]
sibling = { path = "crates/sibling", version = "0.5.2" }
```
