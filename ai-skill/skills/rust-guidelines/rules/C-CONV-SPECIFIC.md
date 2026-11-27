## Conversions live on the most specific type involved (C-CONV-SPECIFIC)

When in doubt, prefer `to_`/`as_`/`into_` to `from_`, because they are more
ergonomic to use (and can be chained with other methods).

For many conversions between two types, one of the types is clearly more
"specific": it provides some additional invariant or interpretation that is not
present in the other type. For example, [`str`] is more specific than `&[u8]`,
since it is a UTF-8 encoded sequence of bytes.

[`str`]: https://doc.rust-lang.org/std/primitive.str.html

Conversions should live with the more specific of the involved types. Thus,
`str` provides both the [`as_bytes`] method and the [`from_utf8`] constructor
for converting to and from `&[u8]` values. Besides being intuitive, this
convention avoids polluting concrete types like `&[u8]` with endless conversion
methods.

[`as_bytes`]: https://doc.rust-lang.org/std/primitive.str.html#method.as_bytes
[`from_utf8`]: https://doc.rust-lang.org/std/str/fn.from_utf8.html
