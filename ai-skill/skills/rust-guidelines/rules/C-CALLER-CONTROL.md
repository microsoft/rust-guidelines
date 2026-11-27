## Caller decides where to copy and place data (C-CALLER-CONTROL)

If a function requires ownership of an argument, it should take ownership of the
argument rather than borrowing and cloning the argument.

```
// Prefer this:
fn foo(b: Bar) {
    /* use b as owned, directly */
}

// Over this:
fn foo(b: &Bar) {
    let b = b.clone();
    /* use b as owned after cloning */
}
```

If a function *does not* require ownership of an argument, it should take a
shared or exclusive borrow of the argument rather than taking ownership and
dropping the argument.

```
// Prefer this:
fn foo(b: &Bar) {
    /* use b as borrowed */
}

// Over this:
fn foo(b: Bar) {
    /* use b as borrowed, it is implicitly dropped before function returns */
}
```

The `Copy` trait should only be used as a bound when absolutely needed, not as a
way of signaling that copies should be cheap to make.
