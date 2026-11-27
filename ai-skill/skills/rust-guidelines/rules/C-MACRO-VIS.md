## Item macros support visibility specifiers (C-MACRO-VIS)

Follow Rust syntax for visibility of items produced by a macro. Private by
default, public if `pub` is specified.

```
bitflags! {
    struct PrivateFlags: u8 {
        const A = 0b0001;
        const B = 0b0010;
    }
}

bitflags! {
    pub struct PublicFlags: u8 {
        const C = 0b0100;
        const D = 0b1000;
    }
}
```
