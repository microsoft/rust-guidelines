## Types for a set of flags are `bitflags`, not enums (C-BITFLAG)

Rust supports `enum` types with explicitly specified discriminants:

```
enum Color {
    Red = 0xff0000,
    Green = 0x00ff00,
    Blue = 0x0000ff,
}
```

Custom discriminants are useful when an `enum` type needs to be serialized to an
integer value compatibly with some other system/language. They support
"typesafe" APIs: by taking a `Color`, rather than an integer, a function is
guaranteed to get well-formed inputs, even if it later views those inputs as
integers.

An `enum` allows an API to request exactly one choice from among many. Sometimes
an API's input is instead the presence or absence of a set of flags. In C code,
this is often done by having each flag correspond to a particular bit, allowing
a single integer to represent, say, 32 or 64 flags. Rust's [`bitflags`] crate
provides a typesafe representation of this pattern.

[`bitflags`]: https://github.com/bitflags/bitflags

```
use bitflags::bitflags;

bitflags! {
    struct Flags: u32 {
        const FLAG_A = 0b00000001;
        const FLAG_B = 0b00000010;
        const FLAG_C = 0b00000100;
    }
}

fn f(settings: Flags) {
    if settings.contains(Flags::FLAG_A) {
        println!("doing thing A");
    }
    if settings.contains(Flags::FLAG_B) {
        println!("doing thing B");
    }
    if settings.contains(Flags::FLAG_C) {
        println!("doing thing C");
    }
}

fn main() {
    f(Flags::FLAG_A | Flags::FLAG_C);
}
```
