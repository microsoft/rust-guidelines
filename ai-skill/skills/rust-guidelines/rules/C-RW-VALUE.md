## Generic reader/writer functions take `R: Read` and `W: Write` by value (C-RW-VALUE)

The standard library contains these two impls:

```
impl<'a, R: Read + ?Sized> Read for &'a mut R { /* ... */ }

impl<'a, W: Write + ?Sized> Write for &'a mut W { /* ... */ }
```

That means any function that accepts `R: Read` or `W: Write` generic parameters
by value can be called with a mut reference if necessary.

In the documentation of such functions, briefly remind users that a mut
reference can be passed. New Rust users often struggle with this. They may have
opened a file and want to read multiple pieces of data out of it, but the
function to read one piece consumes the reader by value, so they are stuck. The
solution would be to leverage one of the above impls and pass `&mut f` instead
of `f` as the reader parameter.

### Examples

- [`flate2::read::GzDecoder::new`]
- [`flate2::write::GzEncoder::new`]
- [`serde_json::from_reader`]
- [`serde_json::to_writer`]

[`flate2::read::GzDecoder::new`]: https://docs.rs/flate2/0.2/flate2/read/struct.GzDecoder.html#method.new
[`flate2::write::GzEncoder::new`]: https://docs.rs/flate2/0.2/flate2/write/struct.GzEncoder.html#method.new
[`serde_json::from_reader`]: https://docs.serde.rs/serde_json/fn.from_reader.html
[`serde_json::to_writer`]: https://docs.serde.rs/serde_json/fn.to_writer.html
