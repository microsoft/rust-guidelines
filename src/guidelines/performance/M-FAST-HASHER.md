<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Use a fast hasher where possible (M-FAST-HASHER) { #M-FAST-HASHER }

<why>to improve performance.</why>
<version>0.1</version>

When hashing trusted, internal keys, prefer a fast non-cryptographic hasher (e.g., `foldhash`, `FxHash`) over the standard library default.

Rust's default hasher is reasonably DoS safe on untrusted user input, but this comes at a performance penalty. If you can trust that keys are not maliciously crafted to overflow individual buckets, a custom fast hasher can yield significant performance gains.

```rust,ignore
// Bad, uses default hasher for keys we control.
let lookup = HashMap::<UserID, Data>::with_capacity(1024);

// Good, uses faster foldhash for internal keys.
let lookup = foldhash::HashMap<UserID, Data>::with_capacity(1024);
