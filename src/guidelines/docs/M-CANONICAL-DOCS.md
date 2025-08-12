<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Documentation Has Canonical Sections (M-CANONICAL-DOCS) { #M-CANONICAL-DOCS }

<why>To follow established and expected Rust best practices.</why>
<version>1.0</version>

Public library items must contain the canonical doc sections. The summary sentence must always be present. Extended documentation and examples
are strongly encouraged. The other sections must be present when applicable.

```rust
/// Summary sentence < 15 words.
///
/// Extended documentation in free form.
///
/// # Examples
/// One or more examples that show API usage like so.
///
/// # Errors
/// If fn returns `Result`, list known error conditions
///
/// # Panics
/// If fn may panic, list when this may happen
///
/// # Safety
/// If fn is `unsafe` or may otherwise cause UB, this section must list
/// all conditions a caller must uphold.
///
/// # Abort
/// If fn may abort the process, list when this may happen.
pub fn foo() {}
```

In contrast to other languages, you should not create a table of parameters. Instead parameter use is explained in plain text. In other words, do not

```rust,ignore
/// Copies a file.
///
/// # Parameters
/// - src: The source.
/// - dst: The destination.
fn copy(src: File, dst: File) {}
```

but instead:

```rust,ignore
/// Copies a file from `src` to `dst`.
fn copy(from: File, to: File) {}
```

### Related Reading

- Function docs include error, panic, and safety considerations ([C-FAILURE](https://rust-lang.github.io/api-guidelines/documentation.html#c-failure))
