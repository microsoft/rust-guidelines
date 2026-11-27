## Conversions use the standard traits `From`, `AsRef`, `AsMut` (C-CONV-TRAITS)

The following conversion traits should be implemented where it makes sense:

- [`From`](https://doc.rust-lang.org/std/convert/trait.From.html)
- [`TryFrom`](https://doc.rust-lang.org/std/convert/trait.TryFrom.html)
- [`AsRef`](https://doc.rust-lang.org/std/convert/trait.AsRef.html)
- [`AsMut`](https://doc.rust-lang.org/std/convert/trait.AsMut.html)

The following conversion traits should never be implemented:

- [`Into`](https://doc.rust-lang.org/std/convert/trait.Into.html)
- [`TryInto`](https://doc.rust-lang.org/std/convert/trait.TryInto.html)

These traits have a blanket impl based on `From` and `TryFrom`. Implement those
instead.

### Examples from the standard library

- `From<u16>` is implemented for `u32` because a smaller integer can always be
  converted to a bigger integer.
- `From<u32>` is *not* implemented for `u16` because the conversion may not be
  possible if the integer is too big.
- `TryFrom<u32>` is implemented for `u16` and returns an error if the integer is
  too big to fit in `u16`.
- [`From<Ipv6Addr>`] is implemented for [`IpAddr`], which is a type that can
  represent both v4 and v6 IP addresses.

[`From<Ipv6Addr>`]: https://doc.rust-lang.org/std/net/struct.Ipv6Addr.html
[`IpAddr`]: https://doc.rust-lang.org/std/net/enum.IpAddr.html
