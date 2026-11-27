## Newtypes encapsulate implementation details (C-NEWTYPE-HIDE)

A newtype can be used to hide representation details while making precise
promises to the client.

For example, consider a function `my_transform` that returns a compound iterator
type.

```
use std::iter::{Enumerate, Skip};

pub fn my_transform<I: Iterator>(input: I) -> Enumerate<Skip<I>> {
    input.skip(3).enumerate()
}
```

We wish to hide this type from the client, so that the client's view of the
return type is roughly `Iterator<Item = (usize, T)>`. We can do so using the
newtype pattern:

```
use std::iter::{Enumerate, Skip};

pub struct MyTransformResult<I>(Enumerate<Skip<I>>);

impl<I: Iterator> Iterator for MyTransformResult<I> {
    type Item = (usize, I::Item);

    fn next(&mut self) -> Option<Self::Item> {
        self.0.next()
    }
}

pub fn my_transform<I: Iterator>(input: I) -> MyTransformResult<I> {
    MyTransformResult(input.skip(3).enumerate())
}
```

Aside from simplifying the signature, this use of newtypes allows us to promise
less to the client. The client does not know _how_ the result iterator is
constructed or represented, which means the representation can change in the
future without breaking client code.

Rust 1.26 also introduces the [`impl Trait`][] feature, which is more concise
than the newtype pattern but with some additional trade offs, namely with `impl
Trait` you are limited in what you can express.  For example, returning an
iterator that impls `Debug` or `Clone` or some combination of the other iterator
extension traits can be problematic.  In summary `impl Trait` as a return type
is probably great for internal APIs and may even be appropriate for public APIs,
but probably not in all cases.  See the ["`impl Trait` for returning complex
types with ease"][impl-trait-2] section of the Edition Guide for more details.

[`impl Trait`]: https://github.com/rust-lang/rfcs/blob/master/text/1522-conservative-impl-trait.md
[impl-trait-2]: https://rust-lang.github.io/edition-guide/rust-2018/trait-system/impl-trait-for-returning-complex-types-with-ease.html

```
pub fn my_transform<I: Iterator>(input: I) -> impl Iterator<Item = (usize, I::Item)> {
    input.skip(3).enumerate()
}
```
