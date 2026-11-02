## Casing conforms to RFC 430 (C-CASE)

Basic Rust naming conventions are described in [RFC 430].

In general, Rust tends to use `UpperCamelCase` for "type-level" constructs (types and
traits) and `snake_case` for "value-level" constructs. More precisely:

| Item | Convention |
| ---- | ---------- |
| Crates | [unclear](https://github.com/rust-lang/api-guidelines/issues/29) |
| Modules | `snake_case` |
| Types | `UpperCamelCase` |
| Traits | `UpperCamelCase` |
| Enum variants | `UpperCamelCase` |
| Functions | `snake_case` |
| Methods | `snake_case` |
| General constructors | `new` or `with_more_details` |
| Conversion constructors | `from_some_other_type` |
| Macros | `snake_case!` |
| Local variables | `snake_case` |
| Statics | `SCREAMING_SNAKE_CASE` |
| Constants | `SCREAMING_SNAKE_CASE` |
| Type parameters | concise `UpperCamelCase`, usually single uppercase letter: `T` |
| Lifetimes | short `lowercase`, usually a single letter: `'a`, `'de`, `'src` |
| Features | [unclear](https://github.com/rust-lang/api-guidelines/issues/101) but see [C-FEATURE] |

In `UpperCamelCase`, acronyms and contractions of compound words count as one word: use `Uuid` rather than `UUID`, `Usize` rather than `USize` or `Stdin` rather than `StdIn`. In `snake_case`, acronyms and contractions are lower-cased: `is_xid_start`.

In `snake_case` or `SCREAMING_SNAKE_CASE`, a "word" should never consist of a
single letter unless it is the last "word". So, we have `btree_map` rather than
`b_tree_map`, but `PI_2` rather than `PI2`.

Crate names should not use `-rs` or `-rust` as a suffix or prefix. Every crate
is Rust! It serves no purpose to remind users of this constantly.

[RFC 430]: https://github.com/rust-lang/rfcs/blob/master/text/0430-finalizing-naming-conventions.md
[C-FEATURE]: C-FEATURE.md

### Examples from the standard library

The whole standard library. This guideline should be easy!
