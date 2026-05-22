<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Proc macros should have separate impl crate incl. tests (M-PROC-IMPL) { #M-PROC-IMPL }

<why>To allow for better testing.</why>
<version>0.1</version>

Proc macros should be thin shims inside some `foo_proc` crate that delegate to a separate, regular library crate, usually called `foo_proc_impl`, which contains the actual token-stream transformation logic and its tests.

As proc macro crates are special, testing them from `foo_proc` usually requires workaround for unit and snapshot tests. Instead, consider having a `foo_proc_impl` crate:

```rust
use proc_macro2::TokenStream;

pub fn my_macro(attr: TokenStream, item: TokenStream) -> TokenStream { ... }
```
These can come with regular [insta](https://insta.rs/) or similar snapshot tests, and are then exported as genuine proc macros via a `foo_proc` crate like so:

```rust
#[proc_macro_attribute]
pub fn my_macro(attr: TokenStream, item: TokenStream) -> TokenStream {
    foo_proc_impl::my_macro(attr.into(), item.into()).into()
}
```
The macros are then re-exported from the core crate:

```rust
pub use foo_proc::my_macro;
```
Inside the core crate, we also recommend adding [trybuild](https://docs.rs/trybuild/latest/trybuild/) UI tests with negative examples to ensure consistent error messages.
