## Only smart pointers implement `Deref` and `DerefMut` (C-DEREF)

The `Deref` traits are used implicitly by the compiler in many circumstances,
and interact with method resolution. The relevant rules are designed
specifically to accommodate smart pointers, and so the traits should be used
only for that purpose.

### Examples from the standard library

- [`Box<T>`](https://doc.rust-lang.org/std/boxed/struct.Box.html)
- [`String`](https://doc.rust-lang.org/std/string/struct.String.html) is a smart
  pointer to [`str`](https://doc.rust-lang.org/std/primitive.str.html)
- [`Rc<T>`](https://doc.rust-lang.org/std/rc/struct.Rc.html)
- [`Arc<T>`](https://doc.rust-lang.org/std/sync/struct.Arc.html)
- [`Cow<'a, T>`](https://doc.rust-lang.org/std/borrow/enum.Cow.html)

[`str`]: https://doc.rust-lang.org/std/primitive.str.html
