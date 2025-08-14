<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Applications may use Anyhow or Derivatives (M-APP-ERROR) { #M-APP-ERROR }

<why>To simplify application-level error handling.</why>
<version>0.1</version>

> Note, this guideline is primarily a relaxation and clarification of [M-ERRORS-CANONICAL-STRUCTS].

Applications, and crates in your own repository exclusively used from your application, may use [anyhow](https://github.com/dtolnay/anyhow),
[eyre](https://github.com/eyre-rs/eyre) or similar application-level error crates instead of implementing their own types.

For example, in your application crates you may just re-export and use eyre's common `Result` type, which should be able to automatically
handle all third party library errors, in particular the ones following
[M-ERRORS-CANONICAL-STRUCTS].

```rust,ignore
use eyre::Result;

fn start_application() -> Result<()> {
    start_server()?;
    Ok(())
}
```

Once you selected your application error crate you should switch all application-level errors to that type, and you should not mix multiple
application-level error types.

Libraries (crates used by more than one crate) should always follow [M-ERRORS-CANONICAL-STRUCTS] instead.

[M-ERRORS-CANONICAL-STRUCTS]: ../libs/ux/#M-ERRORS-CANONICAL-STRUCTS
