## All items have a rustdoc example (C-EXAMPLE)

Every public module, trait, struct, enum, function, method, macro, and type
definition should have an example that exercises the functionality.

This guideline should be applied within reason.

A link to an applicable example on another item may be sufficient. For example
if exactly one function uses a particular type, it may be appropriate to write a
single example on either the function or the type and link to it from the other.

The purpose of an example is not always to show *how to use* the item. Readers
can be expected to understand how to invoke functions, match on enums, and other
fundamental tasks. Rather, an example is often intended to show *why someone
would want to use* the item.

```
// This would be a poor example of using clone(). It mechanically shows *how* to
// call clone(), but does nothing to show *why* somebody would want this.
fn main() {
    let hello = "hello";

    hello.clone();
}
```
