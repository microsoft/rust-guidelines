## Rustdoc does not show unhelpful implementation details (C-HIDDEN)

Rustdoc is supposed to include everything users need to use the crate fully and
nothing more. It is fine to explain relevant implementation details in prose but
they should not be real entries in the documentation.

Especially be selective about which impls are visible in rustdoc -- all the ones
that users would need for using the crate fully, but no others. In the following
code the rustdoc of `PublicError` by default would show the `From<PrivateError>`
impl. We choose to hide it with `#[doc(hidden)]` because users can never have a
`PrivateError` in their code so this impl would never be relevant to them.

```
// This error type is returned to users.
pub struct PublicError { /* ... */ }

// This error type is returned by some private helper functions.
struct PrivateError { /* ... */ }

// Enable use of `?` operator.
#[doc(hidden)]
impl From<PrivateError> for PublicError {
    fn from(err: PrivateError) -> PublicError {
        /* ... */
    }
}
```

[`pub(crate)`] is another great tool for removing implementation details from
the public API. It allows items to be used from outside of their own module but
not outside of the same crate.

[`pub(crate)`]: https://github.com/rust-lang/rfcs/blob/master/text/1422-pub-restricted.md
