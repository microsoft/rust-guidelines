## Examples use `?`, not `try!`, not `unwrap` (C-QUESTION-MARK)

Like it or not, example code is often copied verbatim by users. Unwrapping an
error should be a conscious decision that the user needs to make.

A common way of structuring fallible example code is the following. The lines
beginning with `#` are compiled by `cargo test` when building the example but
will not appear in user-visible rustdoc.

```
/// ```rust
/// # use std::error::Error;
/// #
/// # fn main() -> Result<(), Box<dyn Error>> {
/// your;
/// example?;
/// code;
/// #
/// #     Ok(())
/// # }
/// ```
```
