## Shrink collections to fit after building (M-SHRINK-TO-FIT)

Why: a minimal memory footprint.

Where large, long-lived, growable collections such as `Vec` or `String` were built without an exact size reservation (compare [M-INITIAL-CAPACITY](M-INITIAL-CAPACITY.md)), the resulting collection should be shrunk via `shrink_to_fit` before storing it.

Many Rust collections grow by powers of two when iteratively adding elements. In the worst case a collection might therefore use ~2x of its needed memory.

```
// Bad, long lived object might end up using 2x needed memory.
let mut long_lived = Vec::new();
for x in large_iter {
    long_lived.push(x);
}

// Good, frees up extra memory.
long_lived.shrink_to_fit();
```

Note that this does not apply to conversions done via `into_boxed_*` and friends (compare [M-BOX-DST](M-BOX-DST.md)), as these generally shrink before converting already.
