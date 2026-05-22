<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Custom panics have a helpful message (M-PANIC-MESSAGE) { #M-PANIC-MESSAGE }

<why>to lower the time it takes to understand bugs.</why>
<version>0.1</version>

When code panics intentionally (via `panic!`, `assert!`, `unreachable!`, `todo!`, or similar), a message must be present to clearly state what went wrong and, where applicable, include relevant values.

```rust
// Bad, the panic gives the developer little to act on.
assert!(buffer.len() >= HEADER_SIZE);

// Good, message contains reason and actual values.
assert!(buffer.len() >= HEADER_SIZE, "buffer too small for header: got {} bytes, need {HEADER_SIZE}", buffer.len());
```
