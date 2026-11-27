## Traits are object-safe if they may be useful as a trait object (C-OBJECT)

Trait objects have some significant limitations: methods invoked through a trait
object cannot use generics, and cannot use `Self` except in receiver position.

When designing a trait, decide early on whether the trait will be used as an
object or as a bound on generics.

If a trait is meant to be used as an object, its methods should take and return
trait objects rather than use generics.

A `where` clause of `Self: Sized` may be used to exclude specific methods from
the trait's object. The following trait is not object-safe due to the generic
method.

```
trait MyTrait {
    fn object_safe(&self, i: i32);

    fn not_object_safe<T>(&self, t: T);
}
```

Adding a requirement of `Self: Sized` to the generic method excludes it from the
trait object and makes the trait object-safe.

```
trait MyTrait {
    fn object_safe(&self, i: i32);

    fn not_object_safe<T>(&self, t: T) where Self: Sized;
}
```

### Advantages of trait objects

* _Heterogeneity_. When you need it, you really need it.
* _Code size_. Unlike generics, trait objects do not generate specialized
  (monomorphized) versions of code, which can greatly reduce code size.

### Disadvantages of trait objects

* _No generic methods_. Trait objects cannot currently provide generic methods.
* _Dynamic dispatch and fat pointers_. Trait objects inherently involve
  indirection and vtable dispatch, which can carry a performance penalty.
* _No Self_. Except for the method receiver argument, methods on trait objects
  cannot use the `Self` type.

### Examples from the standard library

- The [`io::Read`] and [`io::Write`] traits are often used as objects.
- The [`Iterator`] trait has several generic methods marked with `where Self:
  Sized` to retain the ability to use `Iterator` as an object.

[`io::Read`]: https://doc.rust-lang.org/std/io/trait.Read.html
[`io::Write`]: https://doc.rust-lang.org/std/io/trait.Write.html
[`Iterator`]: https://doc.rust-lang.org/std/iter/trait.Iterator.html
