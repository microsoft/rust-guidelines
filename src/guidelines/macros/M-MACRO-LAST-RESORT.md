<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Macros are a last resort (M-MACRO-LAST-RESORT) { #M-MACRO-LAST-RESORT }

<why>To avoid complexity where it can be avoided.</why>
<version>0.1</version>

Macros should only be used if no other viable solution exists, compare this adage:

> As @littlecalculist always told me, “macros are for when you run out of language”. If you still have language left — and Rust gives you a lot of language — use the language first.
> 
> @pcwalton

Macros are powerful, but come with several downsides. They

- are magic, and it can be impossible to predict what they do, or how they do it,
- disproportionally increase compilation time in projects that otherwise don't rely on them,
- can cause subtle breakage at edition boundaries where Rust syntax and semantics can change.

Counterintuitively, the more structurally complex the result of a macro expansion is, the worse an idea it is to use macros for that in the first place. The ideal macro makes your users go "_I know exactly what this will generate, but I don't want to write all of that by hand_".
