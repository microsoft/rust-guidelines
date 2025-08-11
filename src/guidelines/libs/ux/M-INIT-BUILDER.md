<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Complex Type Construction has Builders (M-INIT-BUILDER) { #M-INIT-BUILDER }

<why>To future-proof type construction in complex scenarios.</why>
<guideline-status><draft/></guideline-status>

Types that could support 4 or more arbitrary initialization permutations should provide builders. In other words, types with up to
2 optional initialization parameters can be constructed via inherent methods:

```rust
# struct A;
# struct B;
struct Foo;

// Supports 2 optional construction parameters, inherent methods ok.
impl Foo {
    pub fn new() -> Self { Self }
    pub fn with_a(a: A) -> Self { Self }
    pub fn with_b(b: B) -> Self { Self }
    pub fn with_a_b(a: A, b: B) -> Self { Self }
}
```

Beyond that, types should provide a builder:

```rust, ignore
# struct A;
# struct B;
# struct C;
# struct Foo;
# struct FooBuilder;
impl Foo {
    pub fn new() -> Self { ... }
    pub fn builder() -> FooBuilder { ... }
}

impl FooBuilder {
    pub fn a(mut self, a: A) -> Self { ... }
    pub fn b(mut self, b: B) -> Self { ... }
    pub fn c(mut self, c: C) -> Self { ... }
    pub fn build(self) -> Foo { ... }
}

```

The proper name for a builder that builds `Foo` is `FooBuilder`. Its methods must be chainable, with the final method called
`.build()`. The buildable struct must have a shortcut `Foo::builder()`, while the builder itself should _not_ have a public
`FooBuilder::new()`. Builder methods that set a value `x` are called `x()`, not `set_x()` or similar.

### Builders and Required Parameters

Required parameters should be passed when creating the builder, not as setter methods. For builders with multiple required
parameters, encapsulate them into a parameters struct and use the `args: impl Into<Args>` pattern to provide flexibility:

> **Note:** A dedicated args struct is not required if the builder has no required parameters or only a single simple parameter. However,
> for backward compatibility and API evolution, it's preferable to use a dedicated struct for args even in simple cases, as it makes it
> easier to add new required parameters in the future without breaking existing code.

```rust, ignore
#[derive(Debug, Clone)]
pub struct FooArgs {
    pub logger: Logger,
    pub config: Config,
}

impl From<(Logger, Config)> for FooArgs { ... }
impl From<Logger> for FooArgs { ... } // In case we could use default Config instance

impl Foo {
    pub fn builder(args: impl Into<FooArgs>) -> FooBuilder { ... }
}
```

This pattern allows for convenient usage:

- `Foo::builder(logger)` - when only the logger is needed
- `Foo::builder((logger, config))` - when both parameters are needed
- `Foo::builder(FooArgs { logger, config })` - explicit struct construction

### Runtime-Specific Builders

For types that are runtime-specific or require runtime-specific configuration, provide dedicated builder creation methods that accept the appropriate runtime parameters:

```rust, ignore
#[cfg(feature="smol")]
#[derive(Debug, Clone)]
pub struct SmolArgs {
    pub clock: Clock,
    pub io_context: Context,
}

#[cfg(feature="tokio")]
#[derive(Debug, Clone)]
pub struct TokioArgs {
    pub clock: Clock,
}

impl Foo {
    #[cfg(feature="smol")]
    pub fn builder_smol(args: impl Into<SmolArgs>) -> FooBuilder { ... }

    #[cfg(feature="tokio")]
    pub fn builder_tokio(args: impl Into<TokioArgs>) -> FooBuilder { ... }
}
```

This approach ensures type safety at compile time and makes the runtime dependency explicit in the API surface. The resulting
builder methods follow the pattern `builder_{runtime}(args)` where `{runtime}` indicates the specific runtime or execution environment.

### Further Reading

- [Builder pattern in Rust: self vs. &mut self, and method vs. associated function](https://users.rust-lang.org/t/builder-pattern-in-rust-self-vs-mut-self-and-method-vs-associated-function/72892)
