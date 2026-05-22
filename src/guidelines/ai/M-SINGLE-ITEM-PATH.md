<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Items are only visible through one path (M-SINGLE-ITEM-PATH) { #M-SINGLE-ITEM-PATH }

<why>to avoid confusion and clutter offering the same type multiple times.</why>
<version>0.1</version>

Public items within a crate should be reachable only through one path. For example some `crate::db::Connection` should not also be visible as `crate::Connection`:

```rust
// Not OK
pub mod db {
    pub struct Connection;
}

pub use db::Connection;
```

This rule is often violated by agents creating or refactoring large code bases over several iterations. In an attempt to _simplify_ their task, they re-export items under a multiple paths, often previous ones before some change, instead of cleanly redesigning structures where it makes sense. 

Note this only targets the duplication of user-facing items. Within a crate it is acceptable (and often unavoidable) to see the same item multiple times as export trees are constructed:

```rust
// OK
pub(crate) mod db {
    pub struct Connection;
}

pub use db::Connection;
```

Similarly, re-exports of foreign items are not covered by this rule, although they should follow M-ORIGINAL-CRATES.
