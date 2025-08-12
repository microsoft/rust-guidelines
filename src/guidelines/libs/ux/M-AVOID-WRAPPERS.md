<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Avoid Smart Pointers and Wrappers in APIs (M-AVOID-WRAPPERS) { #M-AVOID-WRAPPERS }

<why>To reduce cognitive load and improve API ergonomics.</why>
<version>1.0</version>

As a specialization of [M-ABSTRACTIONS-DONT-NEST], generic wrappers and smart pointers like
`Rc<T>`, `Arc<T>`, `Box<T>`, or `RefCell<T>` should be avoided in public APIs.

From a user perspective these are mostly implementation details, and introduce infectious complexity that users have to
resolve. In fact, these might even be impossible to resolve once multiple crates disagree about the required type of wrapper.

If wrappers are needed internally, they should be hidden behind a clean API that uses simple types like `&T`, `&mut T`, or `T` directly. Compare:

```rust,ignore
// Good: simple API
pub fn process_data(data: &Data) -> State { ... }
pub fn store_config(config: Config) -> Result<(), Error> { ... }

// Bad: Exposing implementation details
pub fn process_shared(data: Arc<Mutex<Shared>>) -> Box<Processed> { ... }
pub fn initialize(config: Rc<RefCell<Config>>) -> Arc<Server> { ... }
```

Smart pointers in APIs are acceptable when:

- The smart pointer is fundamental to the API's purpose (e.g., a new container lib)

- The smart pointer, based on benchmarks, significantly improves performance and the complexity is justified.

[M-ABSTRACTIONS-DONT-NEST]: /guidelines/libs/ux/#M-ABSTRACTIONS-DONT-NEST
