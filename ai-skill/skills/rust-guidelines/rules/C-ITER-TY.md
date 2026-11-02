## Iterator type names match the methods that produce them (C-ITER-TY)

A method called `into_iter()` should return a type called `IntoIter` and
similarly for all other methods that return iterators.

This guideline applies chiefly to methods, but often makes sense for functions
as well. For example the [`percent_encode`] function from the `url` crate
returns an iterator type called [`PercentEncode`][PercentEncode-type].

[PercentEncode-type]: https://docs.rs/url/1.4.0/url/percent_encoding/struct.PercentEncode.html

These type names make the most sense when prefixed with their owning module, for
example [`vec::IntoIter`].

[`vec::IntoIter`]: https://doc.rust-lang.org/std/vec/struct.IntoIter.html

### Examples from the standard library

* [`Vec::iter`] returns [`Iter`][slice::Iter]
* [`Vec::iter_mut`] returns [`IterMut`][slice::IterMut]
* [`Vec::into_iter`] returns [`IntoIter`][vec::IntoIter]
* [`BTreeMap::keys`] returns [`Keys`][btree_map::Keys]
* [`BTreeMap::values`] returns [`Values`][btree_map::Values]

[`Vec::iter`]: https://doc.rust-lang.org/std/vec/struct.Vec.html#method.iter
[slice::Iter]: https://doc.rust-lang.org/std/slice/struct.Iter.html
[`Vec::iter_mut`]: https://doc.rust-lang.org/std/vec/struct.Vec.html#method.iter_mut
[slice::IterMut]: https://doc.rust-lang.org/std/slice/struct.IterMut.html
[`Vec::into_iter`]: https://doc.rust-lang.org/std/vec/struct.Vec.html#method.into_iter
[vec::IntoIter]: https://doc.rust-lang.org/std/vec/struct.IntoIter.html
[`BTreeMap::keys`]: https://doc.rust-lang.org/std/collections/struct.BTreeMap.html#method.keys
[btree_map::Keys]: https://doc.rust-lang.org/std/collections/btree_map/struct.Keys.html
[`BTreeMap::values`]: https://doc.rust-lang.org/std/collections/struct.BTreeMap.html#method.values
[btree_map::Values]: https://doc.rust-lang.org/std/collections/btree_map/struct.Values.html

[`percent_encode`]: https://docs.rs/url/1.4.0/url/percent_encoding/fn.percent_encode.html
