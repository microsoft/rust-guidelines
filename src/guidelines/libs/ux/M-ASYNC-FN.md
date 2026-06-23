<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Functions are `async` over returning a Future (M-ASYNC-FN) { #M-ASYNC-FN }

<why>simpler code and easier-to-understand APIs.</why>

Functions should be declared `async fn foo()` over `fn foo() -> impl Future` when both are viable.

Functions marked `async` are more idiomatic and easier to read. An explicit `Future`-returning signature should only be used when required, for example inside traits or for _hot 'n heavy_ async functions, compare [M-ASYNC-STACK-SIZE](../../performance/#M-ASYNC-STACK-SIZE).

```rust,ignore
impl Foo {
    // Bad, signature is noisier and the body needs an extra `async` block
    fn foo() -> impl Future<Output = Result<T, E>> { async { Ok(t) } }

    // Good, method and implementation reads normally
    async fn foo() -> Result<T, E> { Ok(t) }
}
```
