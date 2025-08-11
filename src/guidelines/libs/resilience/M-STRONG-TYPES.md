<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Use the Proper Type Family (M-STRONG-TYPES) { #M-STRONG-TYPES }

<why>To have and maintain the right data and safety variants, at the right time.</why>
<guideline-status><active>1.0</active></guideline-status>

Use the appropriate `std` type for your task. In general you should use the strongest type available, as early as possible in your API flow. Common offenders are

| Do not use ... | use instead ... | Explanation |
| --- | --- | --- |
| `String`* | `PathBuf`* | Anything dealing with the OS should be `Path`-like |

That said, you should also follow common Rust `std` conventions. Purely numeric types at public API boundaries (e.g., `window_size()`) are expected to
be regular numbers, not `Saturating<usize>`, `NonZero<usize>`, or similar.

<footnotes>

<sup>*</sup> Including their siblings, e.g., `&str`, `Path`, ...

</footnotes>
