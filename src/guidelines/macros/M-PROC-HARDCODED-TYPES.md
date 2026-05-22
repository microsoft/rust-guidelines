<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Proc macros don't hardcode types (M-PROC-HARDCODED-TYPES) { #M-PROC-HARDCODED-TYPES }

<why>To avoid confusing errors, hygiene and visibility issues.</why>
<version>0.1</version>

Macros should not define magic types on their own, in particular not public ones, or ones that don't rely on namespace tricks. 

Some macro want to define types, for example

```rust
#[my_macro]
struct UserType;

// would expand to

struct UserType;
struct ExtraType; 

impl UserType {
    fn foo() -> ExtraType { ... };
}
```

This is almost always a bad idea for several reasons:

- they can conflict with existing user-defined types inside the same module,
- if done naively, they can conflict with other expansions of the same macro,
- they can clash with the user's naming conventions,
- they are invisible at source code level and easily forgotten to be re-exported where needed.

While it is possible for users to work around these limitations somewhat, these are paper cuts your users will have to deal with, possibly months after the fact when refactoring otherwise unrelated code. 

Note that there is one exception to this rule that has generally acceptable UX, the overloaded use of [namespaces](https://doc.rust-lang.org/reference/names/namespaces.html) made prominent by crates like Rocket:

```rust
#[my_macro]
fn foo() { ... }

// would expand to

fn foo() { ... }

struct foo;
impl SomeTrait for foo { ... }
```

Here a new type `foo` is introduced with the same name as the function `foo`. Due to Rust's namespace rules they can co-exit and are automatically re-exported with their parent, and due to [Rust's casing rules (C-CASE)](https://rust-lang.github.io/api-guidelines/naming.html#casing-conforms-to-rfc-430-c-case) these are highly unlikely to clash with user-defined types. However, they would still not make for a pretty _public_ type, and are therefore mainly used inside root crates to define request handlers or FFI functions.

> ### <tip></tip> Namespaces != Modules
>
> Namespaces in Rust have nothing to do with namespaces in other languages. A namespace in C# is approximately a module in Rust. A namespace in Rust 
is an esoteric property of names (e.g., `fn foo`, `struct Bar {}`, `moo!`) that decides which 'naming bucket' it lives in inside a module.
