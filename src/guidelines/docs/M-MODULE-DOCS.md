<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Has Comprehensive Module Documentation (M-MODULE-DOCS) { #M-MODULE-DOCS }

<why>To allow for better API docs navigation.</why>
<version>1.1</version>

Any public library module must have `//!` module documentation, and the first sentence must follow [M-DOC-FIRST-SENTENCE].

```rust,edition2021,ignore
pub mod ffi {
    //! Contains FFI abstractions.

    pub struct String {};
}
```

The rest of the module documentation should be comprehensive, i.e., cover the most relevant technical aspects of the contained items, including

- what the module contains
- when it should be used, possibly when not
- examples
- subsystem specifications (e.g., `std::fmt` [also describes its formatting language](https://doc.rust-lang.org/stable/std/fmt/index.html#formatting-parameters))
- observable side effects, including what guarantees are made about these, if any
- relevant implementation details, e.g., the used system APIs

 Great examples include:

- [`std::fmt`](https://doc.rust-lang.org/stable/std/fmt/index.html)
- [`std::pin`](https://doc.rust-lang.org/stable/std/pin/index.html)
- [`std::option`](https://doc.rust-lang.org/stable/std/option/index.html)

This does not mean every module should contain all of these items. But if there is something to say about the interaction of the contained types,
their module documentation is the right place.

[M-DOC-FIRST-SENTENCE]: ./#M-DOC-FIRST-SENTENCE
