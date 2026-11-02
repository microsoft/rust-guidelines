## Constructors are static, inherent methods (C-CTOR)

In Rust, "constructors" are just a convention. There are a variety of
conventions around constructor naming, and the distinctions are often
subtle.

A constructor in its most basic form is a `new` method with no arguments.

```
impl<T> Example<T> {
    pub fn new() -> Example<T> { /* ... */ }
}
```

Constructors are static (no `self`) inherent methods for the type that they
construct. Combined with the practice of fully importing type names, this
convention leads to informative but concise construction:

```
use example::Example;

// Construct a new Example.
let ex = Example::new();
```

The name `new` should generally be used for the primary method of instantiating
a type. Sometimes it takes no arguments, as in the examples above. Sometimes it
does take arguments, like [`Box::new`] which is passed the value to place in the
`Box`.

Some types' constructors, most notably I/O resource types, use distinct naming
conventions for their constructors, as in [`File::open`], [`Mmap::open`],
[`TcpStream::connect`], and [`UdpSocket::bind`]. In these cases names are chosen
as appropriate for the domain.

Often there are multiple ways to construct a type. It's common in these cases
for secondary constructors to be suffixed `_with_foo`, as in
[`Mmap::open_with_offset`]. If your type has a multiplicity of construction
options though, consider the builder pattern ([C-BUILDER]) instead.

Some constructors are "conversion constructors", methods that create a new type
from an existing value of a different type. These typically have names beginning
with `from_` as in [`std::io::Error::from_raw_os_error`]. Note also though the
`From` trait ([C-CONV-TRAITS]), which is quite similar. There are three
distinctions between a `from_`-prefixed conversion constructor and a `From<T>`
impl.

- A `from_` constructor can be unsafe; a `From` impl cannot. One example of this
  is [`Box::from_raw`].
- A `from_` constructor can accept additional arguments to disambiguate the
  meaning of the source data, as in [`u64::from_str_radix`].
- A `From` impl is only appropriate when the source data type is sufficient to
  determine the encoding of the output data type. When the input is just a bag
  of bits like in [`u64::from_be`] or [`String::from_utf8`], the conversion
  constructor name is able to identify their meaning.

[`Box::from_raw`]: https://doc.rust-lang.org/std/boxed/struct.Box.html#method.from_raw
[`u64::from_str_radix`]: https://doc.rust-lang.org/std/primitive.u64.html#method.from_str_radix
[`u64::from_be`]: https://doc.rust-lang.org/std/primitive.u64.html#method.from_be
[`String::from_utf8`]: https://doc.rust-lang.org/std/string/struct.String.html#method.from_utf8

Note that it is common and expected for types to implement both `Default` and a
`new` constructor. For types that have both, they should have the same behavior.
Either one may be implemented in terms of the other.

[C-BUILDER]: C-BUILDER.md
[C-CONV-TRAITS]: C-CONV-TRAITS.md

### Examples from the standard library

- [`std::io::Error::new`] is the commonly used constructor for an IO error.
- [`std::io::Error::from_raw_os_error`] is a conversion constructor
  based on an error code received from the operating system.
- [`Box::new`] creates a new container type, taking a single argument.
- [`File::open`] opens a file resource.
- [`Mmap::open_with_offset`] opens a memory-mapped file, with additional options.

[`File::open`]: https://doc.rust-lang.org/stable/std/fs/struct.File.html#method.open
[`Mmap::open`]: https://docs.rs/memmap/0.5.2/memmap/struct.Mmap.html#method.open
[`Mmap::open_with_offset`]: https://docs.rs/memmap/0.5.2/memmap/struct.Mmap.html#method.open_with_offset
[`TcpStream::connect`]: https://doc.rust-lang.org/stable/std/net/struct.TcpStream.html#method.connect
[`UdpSocket::bind`]: https://doc.rust-lang.org/stable/std/net/struct.UdpSocket.html#method.bind
[`std::io::Error::new`]: https://doc.rust-lang.org/std/io/struct.Error.html#method.new
[`std::io::Error::from_raw_os_error`]: https://doc.rust-lang.org/std/io/struct.Error.html#method.from_raw_os_error
[`Box::new`]: https://doc.rust-lang.org/stable/std/boxed/struct.Box.html#method.new
