<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Tests do not assert ground truth (M-TAUTOLOGICAL-TESTS) { #M-TAUTOLOGICAL-TESTS }

<why>to avoid adding noise without value.</why>
<version>0.1</version>

Unit tests should verify meaningful behavior instead of repeating foundational definitions.

Agents frequently produce tests that re-state the expected value from the same logic the code under test uses, or that simply mirror the implementation's branches. Such tests pass by construction, provide virtually no value, but increase the noise floor of subsequent changes:

```rust
const CHECKPOINTS: [u32; 4] = [0, 90, 180, 270];

#[test]
fn checkpoints_are_correct() {
    assert_eq!(CHECKPOINTS, [0, 90, 180, 270]);
}
```

Where these are used to satisfy mutation tests, the mutation test should be skipped instead.

Instead, a meaningful test would check a property the constants are supposed to satisfy, for example that they are evenly spaced, monotonically increasing, or impose some direction in related logic.
