## Input syntax is evocative of the output (C-EVOCATIVE)

Rust macros let you dream up practically whatever input syntax you want. Aim to
keep input syntax familiar and cohesive with the rest of your users' code by
mirroring existing Rust syntax where possible. Pay attention to the choice and
placement of keywords and punctuation.

A good guide is to use syntax, especially keywords and punctuation, that is
similar to what will be produced in the output of the macro.

For example if your macro declares a struct with a particular name given in the
input, preface the name with the keyword `struct` to signal to readers that a
struct is being declared with the given name.

```
// Prefer this...
bitflags! {
    struct S: u32 { /* ... */ }
}

// ...over no keyword...
bitflags! {
    S: u32 { /* ... */ }
}

// ...or some ad-hoc word.
bitflags! {
    flags S: u32 { /* ... */ }
}
```

Another example is semicolons vs commas. Constants in Rust are followed by
semicolons so if your macro declares a chain of constants, they should likely be
followed by semicolons even if the syntax is otherwise slightly different from
Rust's.

```
// Ordinary constants use semicolons.
const A: u32 = 0b000001;
const B: u32 = 0b000010;

// So prefer this...
bitflags! {
    struct S: u32 {
        const C = 0b000100;
        const D = 0b001000;
    }
}

// ...over this.
bitflags! {
    struct S: u32 {
        const E = 0b010000,
        const F = 0b100000,
    }
}
```

Macros are so diverse that these specific examples won't be relevant, but think
about how to apply the same principles to your situation.
