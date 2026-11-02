## Data structures do not duplicate derived trait bounds (C-STRUCT-BOUNDS)

Generic data structures should not use trait bounds that can be derived or do
not otherwise add semantic value. Each trait in the `derive` attribute will be
expanded into a separate `impl` block that only applies to generic arguments
that implement that trait.

```
// Prefer this:
#[derive(Clone, Debug, PartialEq)]
struct Good<T> { /* ... */ }

// Over this:
#[derive(Clone, Debug, PartialEq)]
struct Bad<T: Clone + Debug + PartialEq> { /* ... */ }
```

Duplicating derived traits as bounds on `Bad` is unnecessary and a
backwards-compatibiliity hazard. To illustrate this point, consider deriving
`PartialOrd` on the structures in the previous example:

```
// Non-breaking change:
#[derive(Clone, Debug, PartialEq, PartialOrd)]
struct Good<T> { /* ... */ }

// Breaking change:
#[derive(Clone, Debug, PartialEq, PartialOrd)]
struct Bad<T: Clone + Debug + PartialEq + PartialOrd> { /* ... */ }
```

Generally speaking, adding a trait bound to a data structure is a breaking
change because every consumer of that structure will need to start satisfying
the additional bound. Deriving more traits from the standard library using the
`derive` attribute is not a breaking change.

The following traits should never be used in bounds on data structures:

- `Clone`
- `PartialEq`
- `PartialOrd`
- `Debug`
- `Display`
- `Default`
- `Error`
- `Serialize`
- `Deserialize`
- `DeserializeOwned`

There is a grey area around other non-derivable trait bounds that are not
strictly required by the structure definition, like `Read` or `Write`. They may
communicate the intended behavior of the type better in its definition but also
limits future extensibility. Including semantically useful trait bounds on data
structures is still less problematic than including derivable traits as bounds.

### Exceptions

There are three exceptions where trait bounds on structures are required:

1. The data structure refers to an associated type on the trait.
1. The bound is `?Sized`.
1. The data structure has a `Drop` impl that requires trait bounds.
Rust currently requires all trait bounds on the `Drop` impl are also present
on the data structure.

### Examples from the standard library

- [`std::borrow::Cow`] refers to an associated type on the `Borrow` trait.
- [`std::boxed::Box`] opts out of the implicit `Sized` bound.
- [`std::io::BufWriter`] requires a trait bound in its `Drop` impl.

[`std::borrow::Cow`]: https://doc.rust-lang.org/std/borrow/enum.Cow.html
[`std::boxed::Box`]: https://doc.rust-lang.org/std/boxed/struct.Box.html
[`std::io::BufWriter`]: https://doc.rust-lang.org/std/io/struct.BufWriter.html
