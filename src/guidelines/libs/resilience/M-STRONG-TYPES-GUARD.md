<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Newtypes guard their invariants (M-STRONG-TYPES-GUARD) { #M-STRONG-TYPES-GUARD }

<why>To centralize essential correctness invariants.</why>

When introducing a strong type or newtype that exists to encode an invariant (a non-empty string, a percentage, a port number, a sanitized path, ...), the type itself must enforce that invariant where applicable.

Construction should be fallible, returning a proper error when the invariant cannot be upheld, rather than handing the responsibility off to every user:

```rust,ignore
// Bad, creates a new type but enforces nothing. Every caller now has to
// re-check that the value is actually a valid month, defeating the point of
// having a dedicated type.
pub struct Month(pub u8);

impl Month {
    pub fn new(value: u8) -> Self { ... }
}


// Good, the invariant (1..=12) is checked once, at the boundary, and
// every later use of `Month` can rely on it.
pub struct Month(u8);

impl Month {
    pub fn from_u8(value: u8) -> Result<Self, DateError> { ... }
}
```

This means for any newtype that is non-total:

- It must have at least one fallible constructor (e.g., `fn from_foo(...) -> Result<Self, _>`).
- Additional panicking constructors are allowed (e.g., `new`), and should preferably be `const`.
- Conversions from weaker types into the newtype must be fallible (`TryFrom`/`FromStr`).
- Infallible `From` implementations may not be offered.

> ### <tip></tip> Why `const`?
>
> Const constructors allows them to be used inside `const {}` blocks, which surfaces these violations as errors. This enables
> users to do `let month_due = const { Month::new(14) }` and avoids hitting these paths during runtime.
