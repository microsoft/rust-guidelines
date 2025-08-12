<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Public Types Meant to be Read are Display (M-PUBLIC-DISPLAY) { #M-PUBLIC-DISPLAY }

<why>To improve usability.</why>
<version>1.0</version>

If your type is expected to be read by upstream consumers, be it developers or end users, it should implement `Display`. This in particular includes:

- Error types, which are mandated by `std::error::Error` to implement `Display`
- Wrappers around string-like data

Implementations of `Display` should follow Rust customs; this includes rendering newlines and escape sequences.
The handling of sensitive data outlined in [M-PUBLIC-DEBUG] applies analogously.

[M-PUBLIC-DEBUG]: /guidelines/universal/#M-PUBLIC-DEBUG
