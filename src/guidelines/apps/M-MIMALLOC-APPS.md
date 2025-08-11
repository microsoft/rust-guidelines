<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Use Mimalloc for Apps (M-MIMALLOC-APPS) { #M-MIMALLOC-APPS }

<why>To get significant performance for free.</why>
<guideline-status><draft/></guideline-status>

Applications should set [mimalloc](https://crates.io/crates/mimalloc) as their global allocator. This usually results in notable performance
increases along allocating hot paths; we have seen up to 25% benchmark improvements.

Changing the allocator only takes a few lines of code. Add mimalloc to your `Cargo.toml` like so:

```toml
[dependencies]
mimalloc = { version = "0.1" } # Or later version if available
```

Then use it from your `main.rs`:

```rust,ignore
use mimalloc::MiMalloc;

#[global_allocator]
static GLOBAL: MiMalloc = MiMalloc;
```
