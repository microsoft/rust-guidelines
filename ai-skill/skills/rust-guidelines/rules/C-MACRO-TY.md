## Type fragments are flexible (C-MACRO-TY)

If your macro accepts a type fragment like `$t:ty` in the input, it should be
usable with all of the following:

- Primitives: `u8`, `&str`
- Relative paths: `m::Data`
- Absolute paths: `::base::Data`
- Upward relative paths: `super::Data`
- Generics: `Vec<String>`

As a simple example of how things can go wrong, this macro works great with
primitives and absolute paths but fails with relative paths.

```
macro_rules! broken {
    ($m:ident => $t:ty) => {
        pub mod $m {
            pub struct Wrapper($t);
        }
    }
}

broken!(a => u8); // okay

broken!(b => ::std::marker::PhantomData<()>); // okay

struct S;
broken!(c => S); // fails to compile
```
