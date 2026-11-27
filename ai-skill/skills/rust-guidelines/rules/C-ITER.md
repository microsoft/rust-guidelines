## Methods on collections that produce iterators follow `iter`, `iter_mut`, `into_iter` (C-ITER)

Per [RFC 199].

For a container with elements of type `U`, iterator methods should be named:

```
fn iter(&self) -> Iter             // Iter implements Iterator<Item = &U>
fn iter_mut(&mut self) -> IterMut  // IterMut implements Iterator<Item = &mut U>
fn into_iter(self) -> IntoIter     // IntoIter implements Iterator<Item = U>
```

This guideline applies to data structures that are conceptually homogeneous
collections. As a counterexample, the `str` type is slice of bytes that are
guaranteed to be valid UTF-8. This is conceptually more nuanced than a
homogeneous collection so rather than providing the
`iter`/`iter_mut`/`into_iter` group of iterator methods, it provides
[`str::bytes`] to iterate as bytes and [`str::chars`] to iterate as chars.

[`str::bytes`]: https://doc.rust-lang.org/std/primitive.str.html#method.bytes
[`str::chars`]: https://doc.rust-lang.org/std/primitive.str.html#method.chars

This guideline applies to methods only, not functions. For example
[`percent_encode`] from the `url` crate returns an iterator over percent-encoded
string fragments. There would be no clarity to be had by using an
`iter`/`iter_mut`/`into_iter` convention.

[`percent_encode`]: https://docs.rs/url/1.4.0/url/percent_encoding/fn.percent_encode.html
[RFC 199]: https://github.com/rust-lang/rfcs/blob/master/text/0199-ownership-variants.md

### Examples from the standard library

- [`Vec::iter`](https://doc.rust-lang.org/std/vec/struct.Vec.html#method.iter)
- [`Vec::iter_mut`](https://doc.rust-lang.org/std/vec/struct.Vec.html#method.iter_mut)
- [`Vec::into_iter`](https://doc.rust-lang.org/std/vec/struct.Vec.html#method.into_iter)
- [`BTreeMap::iter`](https://doc.rust-lang.org/std/collections/struct.BTreeMap.html#method.iter)
- [`BTreeMap::iter_mut`](https://doc.rust-lang.org/std/collections/struct.BTreeMap.html#method.iter_mut)

[`Vec::iter`]: https://doc.rust-lang.org/std/vec/struct.Vec.html#method.iter
[`Vec::iter_mut`]: https://doc.rust-lang.org/std/vec/struct.Vec.html#method.iter_mut
[`Vec::into_iter`]: https://doc.rust-lang.org/std/vec/struct.Vec.html#method.into_iter
