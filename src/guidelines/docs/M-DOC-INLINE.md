<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Mark `pub use` Items with `#[doc(inline)]` (M-DOC-INLINE) { #M-DOC-INLINE }

<why>To make re-exported items 'fit in' with their non re-exported siblings.</why>
<version>1.0</version>

When publicly re-exporting crate items via `pub use foo::Foo` or `pub use foo::*`, they show up in an opaque re-export block. In most cases, this is not
helpful to the reader:

![TEXT](M-DOC-INLINE_BAD.png)

Instead, you should annotate them with `#[doc(inline)]` at the `use` site, for them to be inlined organically:

```rust,edition2021,ignore
# pub(crate) mod foo { pub struct Foo; }
#[doc(inline)]
pub use foo::*;

// or

#[doc(inline)]
pub use foo::Foo;
```

![TEXT](M-DOC-INLINE_GOOD.png)

This does not apply to `std` or 3rd party types; these should always be re-exported without inlining to make it clear they are external.

> ### <alert></alert> Still avoid glob exports
>
> The `#[doc(inline)]` trick above does not change [M-NO-GLOB-REEXPORTS]; you generally should not re-export items via wildcards.

[M-NO-GLOB-REEXPORTS]: /guidelines/libs/resilience/#M-NO-GLOB-REEXPORTS
