## Data structures implement Serde's `Serialize`, `Deserialize` (C-SERDE)

Types that play the role of a data structure should implement [`Serialize`] and
[`Deserialize`].

[`Serialize`]: https://docs.serde.rs/serde/trait.Serialize.html
[`Deserialize`]: https://docs.serde.rs/serde/trait.Deserialize.html

There is a continuum of types between things that are clearly a data structure
and things that are clearly not, with gray area in between. [`LinkedHashMap`]
and [`IpAddr`] are data structures. It would be completely reasonable for
somebody to want to read in a `LinkedHashMap` or `IpAddr` from a JSON file, or
send one over IPC to another process. [`LittleEndian`] is not a data structure.
It is a marker used by the `byteorder` crate to optimize at compile time for
bytes in a particular order, and in fact an instance of `LittleEndian` can never
exist at runtime. So these are clear-cut examples; the #rust or #serde IRC
channels can help assess more ambiguous cases if necessary.

[`LinkedHashMap`]: https://docs.rs/linked-hash-map/0.4.2/linked_hash_map/struct.LinkedHashMap.html
[`IpAddr`]: https://doc.rust-lang.org/std/net/enum.IpAddr.html
[`LittleEndian`]: https://docs.rs/byteorder/1.0.0/byteorder/enum.LittleEndian.html

If a crate does not already depend on Serde for other reasons, it may wish to
gate Serde impls behind a Cargo cfg. This way downstream libraries only need to
pay the cost of compiling Serde if they need those impls to exist.

For consistency with other Serde-based libraries, the name of the Cargo cfg
should be simply `"serde"`. Do not use a different name for the cfg like
`"serde_impls"` or `"serde_serialization"`.

The canonical implementation looks like this when not using derive:

```toml
[dependencies]
serde = { version = "1.0", optional = true }
```

```
pub struct T { /* ... */ }

#[cfg(feature = "serde")]
impl Serialize for T { /* ... */ }

#[cfg(feature = "serde")]
impl<'de> Deserialize<'de> for T { /* ... */ }
```

And when using derive:

```toml
[dependencies]
serde = { version = "1.0", optional = true, features = ["derive"] }
```

```
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub struct T { /* ... */ }
```
