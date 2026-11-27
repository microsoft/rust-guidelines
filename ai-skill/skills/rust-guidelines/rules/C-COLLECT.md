## Collections implement `FromIterator` and `Extend` (C-COLLECT)

[`FromIterator`] and [`Extend`] enable collections to be used conveniently with
the following iterator methods:

[`FromIterator`]: https://doc.rust-lang.org/std/iter/trait.FromIterator.html
[`Extend`]: https://doc.rust-lang.org/std/iter/trait.Extend.html

- [`Iterator::collect`](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.collect)
- [`Iterator::partition`](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.partition)
- [`Iterator::unzip`](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.unzip)

`FromIterator` is for creating a new collection containing items from an
iterator, and `Extend` is for adding items from an iterator onto an existing
collection.

### Examples from the standard library

- [`Vec<T>`] implements both `FromIterator<T>` and `Extend<T>`.

[`Vec<T>`]: https://doc.rust-lang.org/std/vec/struct.Vec.html
