<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Collections implement the appropriate iter traits (M-COLLECTION-TRAITS) { #M-COLLECTION-TRAITS }

<why>To ensure collections compose.</why>
<version>0.1</version>

Custom collections should implement the iterator-facing traits the standard library offers. 

Whenever you define a new collection type `Collection<T>` for consumption by third parties, the following traits and types should also be implemented, [see here](https://cheats.rs/#iterators) for more details:

- the structs `IntoIter<T>`, `Iter<T>` and `IterMut<T>`,
- an `impl Iterator` for all of them,
- the methods `c.iter()` and `c.iter_mut()`,
- an `impl IntoIterator` for `Collection<T>`, `&Collection<T>` and `&mut Collection<T>`,
- an `impl FromIterator` for `Collection<T>`,
- an `Extend` for `Collection<T>`,
- `DoubleEndedIterator`, `ExactSizeIterator`, ... as applicable

In addition, make sure you implement `size_hint()` on all iterators and do so truthfully.
