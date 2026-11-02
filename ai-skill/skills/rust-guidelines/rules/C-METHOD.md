## Functions with a clear receiver are methods (C-METHOD)

Prefer

```
impl Foo {
    pub fn frob(&self, w: widget) { /* ... */ }
}
```

over

```
pub fn frob(foo: &Foo, w: widget) { /* ... */ }
```

for any operation that is clearly associated with a particular type.

Methods have numerous advantages over functions:

* They do not need to be imported or qualified to be used: all you need is a
  value of the appropriate type.
* Their invocation performs autoborrowing (including mutable borrows).
* They make it easy to answer the question "what can I do with a value of type
  `T`" (especially when using rustdoc).
* They provide `self` notation, which is more concise and often more clearly
  conveys ownership distinctions.
