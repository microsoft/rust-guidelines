## Builders validate in final `.build()` (M-BUILD-RESULT)

Why: clean builder error handling.

A builder's per-field setters should accept input without failing, final validation should be done by `.build()`.

Fallible setters add noise, and still don't guard against interdependent error conditions. Where builders are fallible they should offer a `Result`-carrying `.build()` instead.

```
// Bad, forces repeated error checks that provide no value.
Foo::builder()
    .name("Foo")?
    .distance(42)?
    .build();

// Good, consolidates sanity checking and allows for cross-checks 
// between properties.
Foo::builder()
    .name("Foo")
    .distance(42)
    .build()?;
```

That said, individual settings should prefer strong types carrying their own validation where applicable, compare M-STRONG-TYPES-GUARD.
