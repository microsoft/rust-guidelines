## Ad-hoc conversions follow `as_`, `to_`, `into_` conventions (C-CONV)

Conversions should be provided as methods, with names prefixed as follows:

| Prefix | Cost | Ownership |
| ------ | ---- | --------- |
| `as_` | Free | borrowed -\> borrowed |
| `to_` | Expensive | borrowed -\> borrowed; borrowed -\> owned (non-Copy types); owned -\> owned (Copy types) |
| `into_` | Variable | owned -\> owned (non-Copy types) |

For example:

- [`str::as_bytes()`] gives a view of a `str` as a slice of UTF-8 bytes, which
  is free. The input is a borrowed `&str` and the output is a borrowed `&[u8]`.
- [`Path::to_str`] performs an expensive UTF-8 check on the bytes of an
  operating system path. The input and output are both borrowed. It would not be
  correct to call this `as_str` because this method has nontrivial cost at
  runtime.
- [`str::to_lowercase()`] produces the Unicode-correct lowercase equivalent of a
  `str`, which involves iterating through characters of the string and may
  require memory allocation. The input is a borrowed `&str` and the output is an
  owned `String`.
- [`f64::to_radians()`] converts a floating point quantity from degrees to
  radians. The input is `f64`. Passing a reference `&f64` is not warranted
  because `f64` is cheap to copy. Calling the function `into_radians` would be
  misleading because the input is not consumed.
- [`String::into_bytes()`] extracts the underlying `Vec<u8>` of a `String`,
  which is free. It takes ownership of a `String` and returns an owned
  `Vec<u8>`.
- [`BufReader::into_inner()`] takes ownership of a buffered reader and extracts
  out the underlying reader, which is free. Data in the buffer is discarded.
- [`BufWriter::into_inner()`] takes ownership of a buffered writer and extracts
  out the underlying writer, which requires a potentially expensive flush of any
  buffered data.

[`str::as_bytes()`]: https://doc.rust-lang.org/std/primitive.str.html#method.as_bytes
[`Path::to_str`]: https://doc.rust-lang.org/std/path/struct.Path.html#method.to_str
[`str::to_lowercase()`]: https://doc.rust-lang.org/std/primitive.str.html#method.to_lowercase
[`f64::to_radians()`]: https://doc.rust-lang.org/std/primitive.f64.html#method.to_radians
[`String::into_bytes()`]: https://doc.rust-lang.org/std/string/struct.String.html#method.into_bytes
[`BufReader::into_inner()`]: https://doc.rust-lang.org/std/io/struct.BufReader.html#method.into_inner
[`BufWriter::into_inner()`]: https://doc.rust-lang.org/std/io/struct.BufWriter.html#method.into_inner

Conversions prefixed `as_` and `into_` typically _decrease abstraction_, either
exposing a view into the underlying representation (`as`) or deconstructing data
into its underlying representation (`into`). Conversions prefixed `to_`, on the
other hand, typically stay at the same level of abstraction but do some work to
change from one representation to another.

When a type wraps a single value to associate it with higher-level semantics,
access to the wrapped value should be provided by an `into_inner()` method. This
applies to wrappers that provide buffering like [`BufReader`], encoding or
decoding like [`GzDecoder`], atomic access like [`AtomicBool`], or any similar
semantics.

[`BufReader`]: https://doc.rust-lang.org/std/io/struct.BufReader.html#method.into_inner
[`GzDecoder`]: https://docs.rs/flate2/0.2.19/flate2/read/struct.GzDecoder.html#method.into_inner
[`AtomicBool`]: https://doc.rust-lang.org/std/sync/atomic/struct.AtomicBool.html#method.into_inner

If the `mut` qualifier in the name of a conversion method constitutes part of
the return type, it should appear as it would appear in the type. For example
[`Vec::as_mut_slice`] returns a mut slice; it does what it says. This name is
preferred over `as_slice_mut`.

[`Vec::as_mut_slice`]: https://doc.rust-lang.org/std/vec/struct.Vec.html#method.as_mut_slice

```
// Return type is a mut slice.
fn as_mut_slice(&mut self) -> &mut [T];
```

##### More examples from the standard library

- [`Result::as_ref`](https://doc.rust-lang.org/std/result/enum.Result.html#method.as_ref)
- [`RefCell::as_ptr`](https://doc.rust-lang.org/std/cell/struct.RefCell.html#method.as_ptr)
- [`slice::to_vec`](https://doc.rust-lang.org/std/primitive.slice.html#method.to_vec)
- [`Option::into_iter`](https://doc.rust-lang.org/std/option/enum.Option.html#method.into_iter)
