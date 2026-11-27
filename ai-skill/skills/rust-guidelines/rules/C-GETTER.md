## Getter names follow Rust convention (C-GETTER)

With a few exceptions, the `get_` prefix is not used for getters in Rust code.

```
pub struct S {
    first: First,
    second: Second,
}

impl S {
    // Not get_first.
    pub fn first(&self) -> &First {
        &self.first
    }

    // Not get_first_mut, get_mut_first, or mut_first.
    pub fn first_mut(&mut self) -> &mut First {
        &mut self.first
    }
}
```

The `get` naming is used only when there is a single and obvious thing that
could reasonably be gotten by a getter. For example [`Cell::get`] accesses the
content of a `Cell`.

[`Cell::get`]: https://doc.rust-lang.org/std/cell/struct.Cell.html#method.get

For getters that do runtime validation such as bounds checking, consider adding
unsafe `_unchecked` variants. Typically those will have the following
signatures.

```
fn get(&self, index: K) -> Option<&V>;
fn get_mut(&mut self, index: K) -> Option<&mut V>;
unsafe fn get_unchecked(&self, index: K) -> &V;
unsafe fn get_unchecked_mut(&mut self, index: K) -> &mut V;
```

The difference between getters and conversions ([C-CONV](C-CONV.md)) can be subtle
and is not always clear-cut. For example [`TempDir::path`] can be understood as
a getter for the filesystem path of the temporary directory, while
[`TempDir::into_path`] is a conversion that transfers responsibility for
deleting the temporary directory to the caller. Since `path` is a getter, it
would not be correct to call it `get_path` or `as_path`.

[`TempDir::path`]: https://docs.rs/tempdir/0.3.5/tempdir/struct.TempDir.html#method.path
[`TempDir::into_path`]: https://docs.rs/tempdir/0.3.5/tempdir/struct.TempDir.html#method.into_path

### Examples from the standard library

- [`std::io::Cursor::get_mut`](https://doc.rust-lang.org/std/io/struct.Cursor.html#method.get_mut)
- [`std::pin::Pin::get_mut`](https://doc.rust-lang.org/std/pin/struct.Pin.html#method.get_mut)
- [`std::sync::PoisonError::get_mut`](https://doc.rust-lang.org/std/sync/struct.PoisonError.html#method.get_mut)
- [`std::sync::atomic::AtomicBool::get_mut`](https://doc.rust-lang.org/std/sync/atomic/struct.AtomicBool.html#method.get_mut)
- [`std::collections::hash_map::OccupiedEntry::get_mut`](https://doc.rust-lang.org/std/collections/hash_map/struct.OccupiedEntry.html#method.get_mut)
- [`<[T]>::get_unchecked`](https://doc.rust-lang.org/std/primitive.slice.html#method.get_unchecked)
