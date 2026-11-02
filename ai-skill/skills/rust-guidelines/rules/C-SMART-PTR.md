## Smart pointers do not add inherent methods (C-SMART-PTR)

For example, this is why the [`Box::into_raw`] function is defined the way it
is.

[`Box::into_raw`]: https://doc.rust-lang.org/std/boxed/struct.Box.html#method.into_raw

```
impl<T> Box<T> where T: ?Sized {
    fn into_raw(b: Box<T>) -> *mut T { /* ... */ }
}

let boxed_str: Box<str> = /* ... */;
let ptr = Box::into_raw(boxed_str);
```

If this were defined as an inherent method instead, it would be confusing at the
call site whether the method being called is a method on `Box<T>` or a method on
`T`.

```
impl<T> Box<T> where T: ?Sized {
    // Do not do this.
    fn into_raw(self) -> *mut T { /* ... */ }
}

let boxed_str: Box<str> = /* ... */;

// This is a method on str accessed through the smart pointer Deref impl.
boxed_str.chars()

// This is a method on Box<str>...?
boxed_str.into_raw()
```
