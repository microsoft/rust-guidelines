## Arguments convey meaning through types, not `bool` or `Option` (C-CUSTOM-TYPE)

Prefer

```
let w = Widget::new(Small, Round)
```

over

```
let w = Widget::new(true, false)
```

Core types like `bool`, `u8` and `Option` have many possible interpretations.

Use a deliberate type (whether enum, struct, or tuple) to convey interpretation
and invariants. In the above example, it is not immediately clear what `true`
and `false` are conveying without looking up the argument names, but `Small` and
`Round` are more suggestive.

Using custom types makes it easier to expand the options later on, for example
by adding an `ExtraLarge` variant.

See the newtype pattern ([C-NEWTYPE]) for a no-cost way to wrap existing types
with a distinguished name.

[C-NEWTYPE]: C-NEWTYPE.md
