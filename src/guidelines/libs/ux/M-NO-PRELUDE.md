<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Don't define preludes (M-NO-PRELUDE) { #M-NO-PRELUDE }

<why>To avoid namespace pollution and downstream compilation issues.</why>

Crates must not define a `prelude` or any namespace intended to be imported as `use foo::*`.

While the Rust Standard Library successfully uses [preludes](https://doc.rust-lang.org/std/prelude/index.html) to define edition items, preludes in crates cause more harm than good. Given today's IDE support they are not needed, and once multiple preludes are used from different crates there is potential for conflicts:

```rust,ignore
use foo::prelude::*;
use bar::prelude::*;
use baz::prelude::*;

_ = Client::new();

// error[E0659]: `Client` is ambiguous
//   --> src/lib.rs:17:13
//    |
// 17 |     _ = Client; 
//    |         ^^^^^^ ambiguous name
//    |
//    = note: ambiguous because of multiple glob imports of a name in the same module
```

Preludes in particular do not resolve bad module design. If it looks like a prelude would make the crate easier to use or understand, this is almost always an indication that the existing module system needs restructuring, see [M-BALANCED-MODULES](./#M-BALANCED-MODULES).
