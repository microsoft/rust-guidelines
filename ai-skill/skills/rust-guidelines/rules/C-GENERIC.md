## Functions minimize assumptions about parameters by using generics (C-GENERIC)

The fewer assumptions a function makes about its inputs, the more widely usable
it becomes.

Prefer

```
fn foo<I: IntoIterator<Item = i64>>(iter: I) { /* ... */ }
```

over any of

```
fn foo(c: &[i64]) { /* ... */ }
fn foo(c: &Vec<i64>) { /* ... */ }
fn foo(c: &SomeOtherCollection<i64>) { /* ... */ }
```

if the function only needs to iterate over the data.

More generally, consider using generics to pinpoint the assumptions a function
needs to make about its arguments.

### Advantages of generics

* _Reusability_. Generic functions can be applied to an open-ended collection of
  types, while giving a clear contract for the functionality those types must
  provide.

* _Static dispatch and optimization_. Each use of a generic function is
  specialized ("monomorphized") to the particular types implementing the trait
  bounds, which means that (1) invocations of trait methods are static, direct
  calls to the implementation and (2) the compiler can inline and otherwise
  optimize these calls.

* _Inline layout_. If a `struct` and `enum` type is generic over some type
  parameter `T`, values of type `T` will be laid out inline in the
  `struct`/`enum`, without any indirection.

* _Inference_. Since the type parameters to generic functions can usually be
  inferred, generic functions can help cut down on verbosity in code where
  explicit conversions or other method calls would usually be necessary.

* _Precise types_. Because generics give a _name_ to the specific type
  implementing a trait, it is possible to be precise about places where that
  exact type is required or produced. For example, a function

  ```
  fn binary<T: Trait>(x: T, y: T) -> T
  ```

  is guaranteed to consume and produce elements of exactly the same type `T`; it
  cannot be invoked with parameters of different types that both implement
  `Trait`.

### Disadvantages of generics

* _Code size_. Specializing generic functions means that the function body is
  duplicated. The increase in code size must be weighed against the performance
  benefits of static dispatch.

* _Homogeneous types_. This is the other side of the "precise types" coin: if
  `T` is a type parameter, it stands for a _single_ actual type. So for example
  a `Vec<T>` contains elements of a single concrete type (and, indeed, the
  vector representation is specialized to lay these out in line). Sometimes
  heterogeneous collections are useful; see [trait objects][C-OBJECT].

* _Signature verbosity_. Heavy use of generics can make it more difficult to
  read and understand a function's signature.

[C-OBJECT]: C-OBJECT.md

### Examples from the standard library

- [`std::fs::File::open`] takes an argument of generic type `AsRef<Path>`. This
  allows files to be opened conveniently from a string literal `"f.txt"`, a
  [`Path`], an [`OsString`], and a few other types.

[`std::fs::File::open`]: https://doc.rust-lang.org/std/fs/struct.File.html#method.open
[`Path`]: https://doc.rust-lang.org/std/path/struct.Path.html
[`OsString`]: https://doc.rust-lang.org/std/ffi/struct.OsString.html
