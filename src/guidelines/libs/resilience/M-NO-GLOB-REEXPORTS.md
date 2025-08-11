<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Don't Glob Re-Export Items (M-NO-GLOB-REEXPORTS) { #M-NO-GLOB-REEXPORTS }

<why>To prevent accidentally leaking unintended types.</why>
<guideline-status><active>1.0</active></guideline-status>

Don't `pub use foo::*` from other modules, especially not from other crates. You might accidentally export more than you want,
and globs are hard to review in PRs. Re-export items individually instead:

```rust,ignore
pub use other_module::{A, B, C};
```
