<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Library telemetry does not tank performance (M-LOG-OVERHEAD) { #M-LOG-OVERHEAD }

<why>To avoid compounding issues when using telemetry to diagnose problems.</why>
<version>0.1</version>

Library code that emits telemetry should ensure that doing so does not meaningfully impact throughput or latency on the hot path. 

Crates offered to 3rd parties emitting logs or metrics should assume telemetry will be permanently enabled, or under load. Care should therefore be taken that the volume and overhead of emitted events is reasonable, and will not cause excessive performance degradation. 

Hot, inner loops should preferably stay free of telemetry emission entirely. If it can't be avoided, the events emitted should be lightweight and avoid allocations (e.g., `format!` string concatenation).

```rust
// Bad, logs each message and invokes allocation-based formatting.
for m in messages {
    log(format!("Emitting message {}", m.id()))
}

// Better, avoids per-message allocations.
for m in messages {
    log(("Emitting message", m.id())
}

// Best: If possible, let telemetry users reconstruct what happened offline 
log(("Processing message batch", messages.batch_id())
for m in messages { ... }
```
