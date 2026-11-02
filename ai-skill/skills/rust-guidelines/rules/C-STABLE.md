## Public dependencies of a stable crate are stable (C-STABLE)

A crate cannot be stable (>=1.0.0) without all of its public dependencies being
stable.

Public dependencies are crates from which types are used in the public API of
the current crate.

```
pub fn do_my_thing(arg: other_crate::TheirThing) { /* ... */ }
```

A crate containing this function cannot be stable unless `other_crate` is also
stable.

Be careful because public dependencies can sneak in at unexpected places.

```
pub struct Error {
    private: ErrorImpl,
}

enum ErrorImpl {
    Io(io::Error),
    // Should be okay even if other_crate isn't
    // stable, because ErrorImpl is private.
    Dep(other_crate::Error),
}

// Oh no! This puts other_crate into the public API
// of the current crate.
impl From<other_crate::Error> for Error {
    fn from(err: other_crate::Error) -> Self {
        Error { private: ErrorImpl::Dep(err) }
    }
}
```
