<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Use Newtypes if Primitives have Units (M-NEWTYPES-OVER-PRIMITIVES) { #M-NEWTYPES-OVER-PRIMITIVES }

<why>To prevent accidental API misuse.</why>
<guideline-status><draft/></guideline-status>

Wherever a primitive type (e.g., a number or bool), has a unit and could be ambiguous, it should become a newtype.

```rust,ignore
// Acceptable use of primitives
fn with_capacity(capacity: usize) { }
fn num_cores(n: usize) { }
fn is_open() -> bool { }

// Not acceptable (compare below)
fn create_object(public: bool) {}
fn after_duration(duration: u64) {}

// Do instead
fn create_object(access: Access) {}
fn after_duration(duration: Duration) {}
```

Also see upstream [C-CUSTOM-TYPE](https://rust-lang.github.io/api-guidelines/type-safety.html#arguments-convey-meaning-through-types-not-bool-or-option-c-custom-type).
