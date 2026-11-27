## Binary number types provide `Hex`, `Octal`, `Binary` formatting (C-NUM-FMT)

- [`std::fmt::UpperHex`](https://doc.rust-lang.org/std/fmt/trait.UpperHex.html)
- [`std::fmt::LowerHex`](https://doc.rust-lang.org/std/fmt/trait.LowerHex.html)
- [`std::fmt::Octal`](https://doc.rust-lang.org/std/fmt/trait.Octal.html)
- [`std::fmt::Binary`](https://doc.rust-lang.org/std/fmt/trait.Binary.html)

These traits control the representation of a type under the `{:X}`, `{:x}`,
`{:o}`, and `{:b}` format specifiers.

Implement these traits for any number type on which you would consider doing
bitwise manipulations like `|` or `&`. This is especially appropriate for
bitflag types. Numeric quantity types like `struct Nanoseconds(u64)` probably do
not need these.
