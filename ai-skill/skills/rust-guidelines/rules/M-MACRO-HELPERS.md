## Third party items come from hidden `_private` module (M-MACRO-HELPERS)

Why: predictable compilation.

When a macro expansion needs to refer to third-party items, the host crate should re-export those from a hidden module, and the macro should emit fully-qualified paths through that module rather than expecting the user's crate to depend on the third-party crate directly.

For example, a crate `foo` requiring `bar` traits would do:

```
#[doc(hidden)]
pub mod _private {
    pub use ::bar::Bar;
}

pub use foo_proc::my_macro;
```

The `my_macro!` implementation would then rely on its presence in its emitted code:

```
impl ::foo::_private::Bar for MyType { ... }
```
