<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Collections implement the appropriate iter traits (M-COLLECTION-TRAITS) { #M-COLLECTION-TRAITS }

<why>Implementing the standard iterator traits lets custom collections drop into `for` loops, `collect`, and iterator chains the same way `Vec` and `HashMap` do; missing them forces users into ad-hoc workarounds and breaks ecosystem composition.</why>
<version>0.1</version>

Custom collection types should implement the iterator-facing traits the standard library uses — at minimum `IntoIterator` for the owned type as well as for `&Collection` and `&mut Collection`, and `FromIterator` / `Extend` where construction or accumulation makes sense.

- TODO: Enumerate the exact set of required traits (`IntoIterator` on three forms, `FromIterator`, `Extend`) and which are optional vs. recommended.
- TODO: Specify the conventional inherent methods that should accompany them (`iter`, `iter_mut`, `into_iter`, `len`, `is_empty`).
- TODO: Note when *not* to implement a given trait (e.g., `FromIterator` for collections that need extra context to construct).
- TODO: Provide a concrete bad example (a custom collection missing `IntoIterator for &Collection` so users cannot iterate by reference in a `for` loop).
- TODO: Provide a concrete good example.
- TODO: Note interaction with [M-ESSENTIAL-FN-INHERENT](#M-ESSENTIAL-FN-INHERENT) and [M-IMPL-ASREF](#M-IMPL-ASREF).

