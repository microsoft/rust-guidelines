## Functions validate their arguments (C-VALIDATE)

Rust APIs do _not_ generally follow the [robustness principle]: "be conservative
in what you send; be liberal in what you accept".

[robustness principle]: http://en.wikipedia.org/wiki/Robustness_principle

Instead, Rust code should _enforce_ the validity of input whenever practical.

Enforcement can be achieved through the following mechanisms (listed in order of
preference).

### Static enforcement

Choose an argument type that rules out bad inputs.

For example, prefer

```
fn foo(a: Ascii) { /* ... */ }
```

over

```
fn foo(a: u8) { /* ... */ }
```

where `Ascii` is a _wrapper_ around `u8` that guarantees the highest bit is
zero; see newtype patterns ([C-NEWTYPE]) for more details on creating typesafe
wrappers.

Static enforcement usually comes at little run-time cost: it pushes the costs to
the boundaries (e.g. when a `u8` is first converted into an `Ascii`). It also
catches bugs early, during compilation, rather than through run-time failures.

On the other hand, some properties are difficult or impossible to express using
types.

[C-NEWTYPE]: C-NEWTYPE.md

### Dynamic enforcement

Validate the input as it is processed (or ahead of time, if necessary). Dynamic
checking is often easier to implement than static checking, but has several
downsides:

1. Runtime overhead (unless checking can be done as part of processing the
   input).
2. Delayed detection of bugs.
3. Introduces failure cases, either via `panic!` or `Result`/`Option` types,
   which must then be dealt with by client code.

#### Dynamic enforcement with `debug_assert!`

Same as dynamic enforcement, but with the possibility of easily turning off
expensive checks for production builds.

#### Dynamic enforcement with opt-out

Same as dynamic enforcement, but adds sibling functions that opt out of the
checking.

The convention is to mark these opt-out functions with a suffix like
`_unchecked` or by placing them in a `raw` submodule.

The unchecked functions can be used judiciously in cases where (1) performance
dictates avoiding checks and (2) the client is otherwise confident that the
inputs are valid.
