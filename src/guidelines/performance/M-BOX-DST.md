<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Use boxed slices and strings for immutable owned sequences (M-BOX-DST) { #M-BOX-DST }

<why>low memory consumption and good cache utilization.</why>

Frequently used, internal, immutable sequences that will not be resized after construction should be stored as `Box<[T]>`, `Arc<str>` or similar, rather than their original  `Vec<T>` or `String` counterparts.

Regular growable collections consist of a `(ptr, len, capacity)` triple. Converting them to boxed slices makes them immutable, executes a [shrink-to-fit](./#M-SHRINK-TO-FIT), and drops the `capacity` bit, reducing their handle size by 1/3.  For this pattern to be useful, the following preconditions should apply:

- the sequence should be frequently instantiated (e.g., >1000's of instances),
- it must be immutable,
- it should not be user-visible, i.e., regular users would just deal with `&str` or similar.

Some collections provide dedicated methods for this, e.g., `String::into_boxed_str`.

```rust,ignore
// Bad, with many entries this wastes space and makes
// traversal ultimately slower. 
struct Data {
    ids: Vec<String>
}

// Good, reduces memory consumption and fits more elements 
// into cache.
struct Data {
    ids: Vec<Box<str>>
}
```
