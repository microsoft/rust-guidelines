<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Nested type hierarchies should avoid needless indirection (M-AVOID-INDIRECTION) { #M-AVOID-INDIRECTION }

<why>To avoid costly stalls waiting for DRAM.</why>
<version>0.1</version>

Hot types should avoid nested heap indirection and consider lifting hot, cacheable deep fields to improve cache utilization.  

While the gold standard is to benchmark, a pattern that emerges repeatedly when porting code C# code to Rust is to reflexively `Arc`ing nested types, often multiple layers deep. Although this can make sense on very wide or heavyweight types that genuinely need to be shared by multiple owners, this pattern can ruin access latency when multiple rounds of DRAM lookup have to be performed sequentially. 

Where nested, shared ownership isn't strictly needed, it is usually better to start with local, embedded data, and lifted cacheable fields.

```rust
// Bad, `print` (assuming it is reasonably hot) needs 2 indirections 
// to query whether it is enabled. 
struct Item {
    config: Arc<Config>,
    payload: Payload,
}

struct Config {
    feature: Arc<Feature>
}

impl Item {
    fn print(&self) {
        if self.config.feature.is_enabled() { ... }
    }
}

// Better: `enabled` resides nearby and is likely immediately available 
// once `print` is called.
struct Item {
    config: Arc<Config>,
    payload: Payload,
    enabled: bool,
}

impl Item {
    fn print(&self) {
        if self.enabled { ... }
    }
}

```
