<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Important parameters go first, closures last (M-PARAMETER-ORDER) { #M-PARAMETER-ORDER }

<why>A predictable parameter order keeps the most relevant arguments visible at the call site and avoids the awkward formatting that occurs when a long closure precedes plain arguments; following this convention also makes APIs scan-readable across a crate.</why>
<version>0.1</version>

Order function parameters from most to least important, and place closures (and other large/inline-defined arguments such as `impl FnMut`, `impl Fn`, builder lambdas) at the end of the signature.

- TODO: Define "importance" concretely (e.g., the conceptual subject of the operation comes first; configuration knobs follow; optional/contextual data later).
- TODO: Clarify how this interacts with methods that already have a `self` receiver (the receiver is always first; the rule applies to the remaining parameters).
- TODO: Specify the rule for multiple closures (e.g., `map_or_else(default, f)`) — does any closure count as "last", or only single-closure APIs?
- TODO: Provide a concrete bad example (a function taking a closure followed by an integer count).
- TODO: Provide a concrete good example (`fn retry(count: usize, f: impl FnMut() -> Result<T, E>) -> ...`).
- TODO: Note interaction with M-PARAMETER-CONSISTENCY (which governs cross-crate consistency of the chosen order).
