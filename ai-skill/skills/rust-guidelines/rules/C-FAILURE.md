## Function docs include error, panic, and safety considerations (C-FAILURE)

Error conditions should be documented in an "Errors" section. This applies to
trait methods as well -- trait methods for which the implementation is allowed
or expected to return an error should be documented with an "Errors" section.

For example in the standard library, Some implementations of the
[`std::io::Read::read`] trait method may return an error.

[`std::io::Read::read`]: https://doc.rust-lang.org/std/io/trait.Read.html#tymethod.read

```
/// Pull some bytes from this source into the specified buffer, returning
/// how many bytes were read.
///
/// ... lots more info ...
///
/// # Errors
///
/// If this function encounters any form of I/O or other error, an error
/// variant will be returned. If an error is returned then it must be
/// guaranteed that no bytes were read.
```

Panic conditions should be documented in a "Panics" section. This applies to
trait methods as well -- traits methods for which the implementation is allowed
or expected to panic should be documented with a "Panics" section.

In the standard library the [`Vec::insert`] method may panic.

[`Vec::insert`]: https://doc.rust-lang.org/std/vec/struct.Vec.html#method.insert

```
/// Inserts an element at position `index` within the vector, shifting all
/// elements after it to the right.
///
/// # Panics
///
/// Panics if `index` is out of bounds.
```

It is not necessary to document all conceivable panic cases, especially if the
panic occurs in logic provided by the caller. For example documenting the
`Display` panic in the following code seems excessive. But when in doubt, err on
the side of documenting more panic cases.

```
/// # Panics
///
/// This function panics if `T`'s implementation of `Display` panics.
pub fn print<T: Display>(t: T) {
    println!("{}", t.to_string());
}
```

Unsafe functions should be documented with a "Safety" section that explains all
invariants that the caller is responsible for upholding to use the function
correctly.

The unsafe [`std::ptr::read`] requires the following of the caller.

[`std::ptr::read`]: https://doc.rust-lang.org/std/ptr/fn.read.html

```
/// Reads the value from `src` without moving it. This leaves the
/// memory in `src` unchanged.
///
/// # Safety
///
/// Beyond accepting a raw pointer, this is unsafe because it semantically
/// moves the value out of `src` without preventing further usage of `src`.
/// If `T` is not `Copy`, then care must be taken to ensure that the value at
/// `src` is not used before the data is overwritten again (e.g. with `write`,
/// `zero_memory`, or `copy_memory`). Note that `*src = foo` counts as a use
/// because it will attempt to drop the value previously at `*src`.
///
/// The pointer must be aligned; use `read_unaligned` if that is not the case.
```
