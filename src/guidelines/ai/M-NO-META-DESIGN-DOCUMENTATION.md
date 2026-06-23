<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Avoid meta design documentation (M-NO-META-DESIGN-DOCUMENTATION) { #M-NO-META-DESIGN-DOCUMENTATION }

<why>to avoid confusing users with information not relevant to them.</why>

Crate and module documentation must be free of meta design narratives that were only relevant during the creation of a crate. In other words, it is the end-state that is to be documented, not the design journey.

Agents frequently produce sections that describe how a change was designed, "why we picked X over Y" essays, and design journals inside user-facing documentation. These artifacts might be interesting diagnostics while working on the project, but they are mostly meaningless to end users.

For example, an agent might append a self-report like this, summarizing which guidelines it claims to have followed:

```text
| Rule | Applied | Where |
| --- | :---: | --- |
| M-SHORT-NAMES | ✅ | Shortened method names across the data-access and HTTP handler layers. |
| M-WEASEL-WORDS | ✅ | Removed weasel words from type and field names throughout the public API. |
| M-PUBLIC-DISPLAY | ✅ | Added `Display` impls for all user-facing identifier and error types. |
| M-ASYNC-FN | ✅ | Migrated I/O-facing APIs from `impl Future` returns to `async fn`. |
```

This kind of content describes process, not behaviour, and goes stale over time. That said, it is of course perfectly reasonable to have a _Design Principles_ or similar section in the project's README, that on a high level describes the enduring architectural goals that are relevant to end users (e.g., a crate being allocation free, having an OSI architecture, or being designed with `#[no_std]` in mind).
