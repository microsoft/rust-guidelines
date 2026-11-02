## Sealed traits protect against downstream implementations (C-SEALED)

Some traits are only meant to be implemented within the crate that defines them.
In such cases, we can retain the ability to make changes to the trait in a
non-breaking way by using the sealed trait pattern.

```
/// This trait is sealed and cannot be implemented for types outside this crate.
pub trait TheTrait: private::Sealed {
    // Zero or more methods that the user is allowed to call.
    fn ...();

    // Zero or more private methods, not allowed for user to call.
    #[doc(hidden)]
    fn ...();
}

// Implement for some types.
impl TheTrait for usize {
    /* ... */
}

mod private {
    pub trait Sealed {}

    // Implement for those same types, but no others.
    impl Sealed for usize {}
}
```

The empty private `Sealed` supertrait cannot be named by downstream crates, so
we are guaranteed that implementations of `Sealed` (and therefore `TheTrait`)
only exist in the current crate. We are free to add methods to `TheTrait` in a
non-breaking release even though that would ordinarily be a breaking change for
traits that are not sealed. Also we are free to change the signature of methods
that are not publicly documented.

Note that removing a public method or changing the signature of a public method
in a sealed trait are still breaking changes.

To avoid frustrated users trying to implement the trait, it should be documented
in rustdoc that the trait is sealed and not meant to be implemented outside of
the current crate.

### Examples

- [`serde_json::value::Index`](https://docs.serde.rs/serde_json/value/trait.Index.html)
- [`byteorder::ByteOrder`](https://docs.rs/byteorder/1.1.0/byteorder/trait.ByteOrder.html)
