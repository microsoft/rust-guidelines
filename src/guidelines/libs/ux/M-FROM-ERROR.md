<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Canonical error conversion uses `From`, not `map_err` (M-FROM-ERROR) { #M-FROM-ERROR }

<why>To ensure idiomatic error handling.</why>
<version>0.1</version>

Where an `Error` type is owned, it should `impl From<Other> for Error {}` instead of handling the conversion throughout the code via `.map_error()`. Calling `.map_error()` is only appropriate when dealing with foreign error types, or if contextual information needs to be preserved.

```rust,ignore
// Bad, repeats the same conversion at every call site and obscures the happy path.
fn load() -> Result<Config, MyError> {
    let bytes = read("config.toml").map_err(|e| MyError::Io(e))?;
    let text = str::from_utf8(&bytes).map_err(|e| MyError::Utf8(e))?;
    let cfg = toml::from_str(text).map_err(|e| MyError::Parse(e))?;
    Ok(cfg)
}

// Good, define the conversion once and let `?` apply it.
impl From<std::io::Error> for MyError { ... }
impl From<std::str::Utf8Error> for MyError { ... }
impl From<toml::de::Error> for MyError { ... }

fn load() -> Result<Config, MyError> {
    let bytes = read("config.toml")?;
    let text = str::from_utf8(&bytes)?;
    let cfg = toml::from_str(text)?;
    Ok(cfg)
}
```
