<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Macros don't lie about signatures (M-MACROS-DONT-LIE) { #M-MACROS-DONT-LIE }

<why>To avoid confusing users and LLMs.</why>
<version>0.1</version>

Macros must not (make users) misrepresent signatures or shape of items. 

Macros have the ability to arbitrarily rewrite token streams. They could convert structs to enums, traits to functions, or perform any other transformation imaginable. They should, however, do none of that, as the resulting code will be highly confusing and virtually impossible to predict or reason about. 

Among others, macros must not

- convert the nature of data types (e.g., structs to enums, ...),
- alter function signatures,
- convert the `async`-ness of items,
- do anything else that materially detaches _what's written_ from _what's happening_.

```rust
// Bad: Adds extra parameter and marks function `async`. Impossible to 
// predict from reading code. 
#[magic_transform]
fn foo() { }

foo(token).await
```
