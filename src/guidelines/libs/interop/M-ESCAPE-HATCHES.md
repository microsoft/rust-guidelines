<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Native Escape Hatches (M-ESCAPE-HATCHES) { #M-ESCAPE-HATCHES }

<why>To allow users to work around unsupported use cases until alternatives are available.</why>
<version>0.1</version>

Types wrapping native handles should provide `unsafe` escape hatches. In interop scenarios your users might have gotten a native handle from somewhere
else, or they might have to pass your wrapped handle over FFI. To enable these use cases you should provide `unsafe` conversion methods.

```rust
# type HNATIVE = *const u8;
pub struct Handle(HNATIVE);

impl Handle {
    pub fn new() -> Self {
        // Safely creates handle via API calls
        # todo!()
    }

    // Constructs a new Handle from a native handle the user got elsewhere.
    // This method  should then also document all safety requirements that
    // must be fulfilled.
    pub unsafe fn from_native(native: HNATIVE) -> Self {
        Self(native)
    }

    // Various extra methods to permanently or temporarily obtain
    // a native handle.
    pub unsafe fn into_native(self) -> HNATIVE { self.0 }
    pub unsafe fn to_native(&self) -> HNATIVE { self.0 }
}
```
