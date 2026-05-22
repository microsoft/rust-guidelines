<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Shrink collections to fit after building (M-SHRINK-TO-FIT) { #M-SHRINK-TO-FIT }

<why>To reduce memory footprint.</why>
<version>0.1</version>

Where large, long-lived, growable collection such as `Vec`, `String` were built without an exact size reservation (compare M-INITIAL-CAPACITY), the resulting collection should be shrunk via `shrink_to_fit` before storing it.

Rust's collections grow by powers of two when iteratively adding elements. In the worst case a collection might therefore use ~2x of its needed memory. 

```rust
// Bad, long lived object might end up using 2x needed memory.
let mut long_lived = Vec::new();
for x in large_iter {
    long_lived.push(x);
}

// Good, frees up extra memory.
long_lived.shrink_to_fit();
```
Note, this does not apply to conversions done via `into_boxed_` and friends (compare M-BOX-DST), as these generally shrink before converting already.
