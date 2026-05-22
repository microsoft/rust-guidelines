<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Where possible functions are `async` over returning a Future (M-ASYNC-FN) { #M-ASYNC-FN }

<why>An `async fn` signature is shorter, infers lifetimes correctly by default, and reads as ordinary control flow; hand-written `-> impl Future<Output = ...>` returns add noise, frequently require explicit `+ '_` / `+ Send` bounds, and are easier to get subtly wrong.</why>
<version>0.1</version>

Prefer writing `async fn foo(...) -> T` over `fn foo(...) -> impl Future<Output = T>` (or a boxed future) when both are viable. Fall back to an explicit `Future`-returning signature only when the function genuinely cannot be `async` — for example, when extra `Send`/`Sync`/`'static` bounds, manual lifetime control, or returning a stored/boxed future is required.

- TODO: Enumerate the legitimate reasons to write a non-`async` future-returning signature (e.g., trait methods pre-`async fn in trait` stabilization, manually pinned futures, explicit `Send` bounds on the returned future, returning a `BoxFuture` for object safety).
- TODO: Clarify the rule for trait methods (use `async fn in trait` where available; document any MSRV constraints).
- TODO: Provide a concrete bad example (`fn load(&self) -> impl Future<Output = Result<T, E>> + '_ { async move { ... } }`).
- TODO: Provide a concrete good example (`async fn load(&self) -> Result<T, E> { ... }`).
- TODO: Note interaction with M-IMPL-IO, M-SERVICES-CLONE, and any project-wide `Send`-bound conventions.
