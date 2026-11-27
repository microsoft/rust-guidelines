## Operator overloads are unsurprising (C-OVERLOAD)

Operators with built in syntax (`*`, `|`, and so on) can be provided for a type
by implementing the traits in [`std::ops`]. These operators come with strong
expectations: implement `Mul` only for an operation that bears some resemblance
to multiplication (and shares the expected properties, e.g. associativity), and
so on for the other traits.

[`std::ops`]: https://doc.rust-lang.org/std/ops/index.html#traits
