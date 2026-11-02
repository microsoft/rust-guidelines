## Newtypes provide static distinctions (C-NEWTYPE)

Newtypes can statically distinguish between different interpretations of an
underlying type.

For example, a `f64` value might be used to represent a quantity in miles or in
kilometers. Using newtypes, we can keep track of the intended interpretation:

```
struct Miles(pub f64);
struct Kilometers(pub f64);

impl Miles {
    fn to_kilometers(self) -> Kilometers { /* ... */ }
}
impl Kilometers {
    fn to_miles(self) -> Miles { /* ... */ }
}
```

Once we have separated these two types, we can statically ensure that we do not
confuse them. For example, the function

```
fn are_we_there_yet(distance_travelled: Miles) -> bool { /* ... */ }
```

cannot accidentally be called with a `Kilometers` value. The compiler will
remind us to perform the conversion, thus averting certain [catastrophic bugs].

[catastrophic bugs]: http://en.wikipedia.org/wiki/Mars_Climate_Orbiter
