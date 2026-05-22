<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Collections are created with sufficient initial capacity (M-INITIAL-CAPACITY) { #M-INITIAL-CAPACITY }

<why>To avoid performance penalties when creating collections.</why>
<version>0.1</version>

Where the final or approximate size of a collection (`Vec`, `String`, `HashMap`, `HashSet`, etc.) is known at construction time, it should be created via   `with_capacity` rather than `new` or `default`. 

Collections created without capacity may be re-allocated multiple times during their initialization, which also includes copying their content. Creating them with sufficient capacity an entirely avoid this needless overhead.

```rust
// Bad, probably re-allocates and copies concent over multiple times.
let mut rval = Vec::new();
for x in &other {
    rval.push(convert(x));
}

// Better, creates collection with sufficient capacity upfront.
let mut rval = Vec::with_capacity(other.len());
for x in &other {
    rval.push(convert(x));
}
```

Iterator-driven construction (`collect`) inherits this behavior via `size_hint` and should be preferred over manual `push` loops when possible:

```rust
// Ideal, looks nicer and is performant
let rval: Vec<_> = other.iter().map(convert).collect();
```
