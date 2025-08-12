<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Types are Send (M-TYPES-SEND) { #M-TYPES-SEND }

<why>To enable the use of types in Tokio and behind runtime abstractions</why>
<version>1.0</version>

Public types should be `Send` for compatibility reasons:

- All futures produced (explicitly or implicitly) must be `Send`
- Most other types should be `Send`, but there might be exceptions

### Futures

When declaring a future explicitly you should ensure it is, and remains, `Send`.

```rust
# use std::future::Future;
# use std::pin::Pin;
# use std::task::{Context, Poll};
#
struct Foo {}

impl Future for Foo {
    // Explicit implementation of `Future` for your type
    # type Output = ();
    #
    # fn poll(self: Pin<&mut Self>, _: &mut Context<'_>) -> Poll<<Self as Future>::Output> { todo!() }
}

// You should assert your type is `Send`
const fn assert_send<T: Send>() {}
const _: () = assert_send::<Foo>();
```

When returning futures implicitly through `async` method calls, you should make sure these are `Send` too.
You do not have to test every single method, but you should at least validate your main entry points.

```rust,edition2021
async fn foo() { }

// TODO: We want this as a macro as well
fn assert_send<T: Send>(_: T) {}
_ = assert_send(foo());
```

### Regular Types

Most regular types should be `Send`, as they otherwise infect futures turning them `!Send` if held across `.await` points.

```rust,edition2021
# use std::rc::Rc;
# async fn read_file(x: &str) {}
#
async fn foo() {
    let rc = Rc::new(123);      // <-- Holding this across an .await point prevents
    read_file("foo.txt").await; //     the future from being `Send`.
    dbg!(rc);
}
```

That said, if the default use of your type is _instantaneous_, and there is no reason for it to be otherwise held across `.await` boundaries, it may be `!Send`.

```rust,edition2021
# use std::rc::Rc;
# struct Telemetry; impl Telemetry { fn ping(&self, _: u32) {} }
# fn telemetry() -> Telemetry  { Telemetry }
# async fn read_file(x: &str) {}
#
async fn foo() {
    // Here a hypothetical instance Telemetry is summoned
    // and used ad-hoc. It may be ok for Telemetry to be !Send.
    telemetry().ping(0);
    read_file("foo.txt").await;
    telemetry().ping(1);
}
```

> ### <tip></tip> The Cost of Send
>
> Ideally, there would be abstractions that are `Send` in work-stealing runtimes, and `!Send` in thread-per-core models based on non-atomic
> types like `Rc` and `RefCell` instead.
>
> Practically these abstractions don't exist, preventing Tokio compatibility in the non-atomic case. That in turn means you would have to
> "reinvent the world" to get anything done in a thread-per-core universe.
>
> The good news is, in most cases atomics and uncontended locks only have a measurable impact if accessed more frequently than every 64 words or so.
>
> <div style="background-color:white;">
>
> ![TEXT](M-TYPES-SEND.svg)
>
> </div>
>
> Working with a large `Vec<AtomicUsize>` in a hot loop is a bad idea, but doing the occasional uncontended atomic operation from otherwise thread-per-core
> async code has no performance impact, but gives you widespread ecosystem compatibility.
