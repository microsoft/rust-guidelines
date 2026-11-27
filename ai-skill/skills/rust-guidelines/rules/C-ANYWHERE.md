## Item macros work anywhere that items are allowed (C-ANYWHERE)

Rust allows items to be placed at the module level or within a tighter scope
like a function. Item macros should work equally well as ordinary items in all
of these places. The test suite should include invocations of the macro in at
least the module scope and function scope.

```
#[cfg(test)]
mod tests {
    test_your_macro_in_a!(module);

    #[test]
    fn anywhere() {
        test_your_macro_in_a!(function);
    }
}
```

As a simple example of how things can go wrong, this macro works great in a
module scope but fails in a function scope.

```
macro_rules! broken {
    ($m:ident :: $t:ident) => {
        pub struct $t;
        pub mod $m {
            pub use super::$t;
        }
    }
}

broken!(m::T); // okay, expands to T and m::T

fn g() {
    broken!(m::U); // fails to compile, super::U refers to the containing module not g
}
```
