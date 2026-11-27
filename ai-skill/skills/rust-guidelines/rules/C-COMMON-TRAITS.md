## Types eagerly implement common traits (C-COMMON-TRAITS)

Rust's trait system does not allow _orphans_: roughly, every `impl` must live
either in the crate that defines the trait or the implementing type.
Consequently, crates that define new types should eagerly implement all
applicable, common traits.

To see why, consider the following situation:

* Crate `std` defines trait `Display`.
* Crate `url` defines type `Url`, without implementing `Display`.
* Crate `webapp` imports from both `std` and `url`,

There is no way for `webapp` to add `Display` to `Url`, since it defines
neither. (Note: the newtype pattern can provide an efficient, but inconvenient
workaround.)

The most important common traits to implement from `std` are:

- [`Copy`](https://doc.rust-lang.org/std/marker/trait.Copy.html)
- [`Clone`](https://doc.rust-lang.org/std/clone/trait.Clone.html)
- [`Eq`](https://doc.rust-lang.org/std/cmp/trait.Eq.html)
- [`PartialEq`](https://doc.rust-lang.org/std/cmp/trait.PartialEq.html)
- [`Ord`](https://doc.rust-lang.org/std/cmp/trait.Ord.html)
- [`PartialOrd`](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html)
- [`Hash`](https://doc.rust-lang.org/std/hash/trait.Hash.html)
- [`Debug`](https://doc.rust-lang.org/std/fmt/trait.Debug.html)
- [`Display`](https://doc.rust-lang.org/std/fmt/trait.Display.html)
- [`Default`](https://doc.rust-lang.org/std/default/trait.Default.html)

Note that it is common and expected for types to implement both
`Default` and an empty `new` constructor. `new` is the constructor
convention in Rust, and users expect it to exist, so if it is
reasonable for the basic constructor to take no arguments, then it
should, even if it is functionally identical to `default`.
