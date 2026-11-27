## Feature names are free of placeholder words (C-FEATURE)

Do not include words in the name of a [Cargo feature] that convey zero meaning,
as in `use-abc` or `with-abc`. Name the feature `abc` directly.

[Cargo feature]: http://doc.crates.io/manifest.html#the-features-section

This arises most commonly for crates that have an optional dependency on the
Rust standard library. The canonical way to do this correctly is:

```toml
# In Cargo.toml

[features]
default = ["std"]
std = []
```

```
// In lib.rs
#![no_std]

#[cfg(feature = "std")]
extern crate std;
```

Do not call the feature `use-std` or `with-std` or any creative name that is not
`std`. This naming convention aligns with the naming of implicit features
inferred by Cargo for optional dependencies. Consider crate `x` with optional
dependencies on Serde and on the Rust standard library:

```toml
[package]
name = "x"
version = "0.1.0"

[features]
std = ["serde/std"]

[dependencies]
serde = { version = "1.0", optional = true }
```

When we depend on `x`, we can enable the optional Serde dependency with
`features = ["serde"]`. Similarly we can enable the optional standard library
dependency with `features = ["std"]`. The implicit feature inferred by Cargo for
the optional dependency is called `serde`, not `use-serde` or `with-serde`, so
we like for explicit features to behave the same way.

As a related note, Cargo requires that features are additive so a feature named
negatively like `no-abc` is practically never correct.
