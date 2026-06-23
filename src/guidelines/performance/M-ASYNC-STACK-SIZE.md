<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Hot `async` functions reduce stack size (M-ASYNC-STACK-SIZE) { #M-ASYNC-STACK-SIZE }

<why>small async stack sizes and low memcpy overhead.</why>

Functions marked `async` in the hot path should track their future sizes, and take one or more of the following steps to reduce their impact:

- reduction of parameter and rval type size,
- reduction of type size of items held across `.await` points,
- returning `impl Future` and extracting setup logic from `async {}` capture.

> ### <tip></tip> Future 'Stack' Sizes
>
> In Futures, what would naively be considered _their stack_, is actually part of a significantly more complicated machinery under their  hood.
>
> Regular locals, that only live momentarily between two `.await` points, still remain part of the runtime thread's regular stack. However, any locals that live across `.await` points, or parameters passed during construction, become part of that Future's state machine type, and the layout of this type is currently not as optimized as it could be.
>
> This not only can cause stack-to-heap memcpy operations when creating or boxing Futures, it can also force large upfront stack sizes of the hypothetical most deeply nested cross-async call stack of the involved async function (which, on a side note, is why they can't simply recurse).
>
> ```rust,ignore
> async fn foo(_large: Large) {
>     let within_future = [0_u8; 1024]; // Crosses .await below, embedded in `foo` type
>     let on_stack = [0_u8; 1024]; // Does not cross .await points, lives on stack
>     let sneaky = Droppable::with_size(1024); // Secretly crosses .await point!
>     dbg!(&on_stack, &sneaky);
>     bar(&within_future).await;
>     dbg!(&within_future);
>     // <- `sneaky` dropped here, despite otherwise not being used!
> }
> 
> let future = foo(Large::new()); // `Large` becomes embedded in `foo` type, 
>                                 // blowing up its size, despite it not even
>                                 // being used.
> 
> // Here, despite `foo` not running yet, we might consume up to `Large` + 
> // 2kb of this thread's stack memory. Once we spawn this is memcpy'ed 
> // to runtime Task structure:
> rt.spawn(future);
>```

For many async functions this isn't an issue, as their associated `Future`-cost is negligible. However, functions used along the hot path, that are either called or instantiated frequently (e.g., 1000's of calls per second or concurrent tasks) might benefit from monitoring and optimizations.

Hot futures should be tracked via `size_of_val`:

```rust,ignore
async fn hot() { ... }

#[test]
fn has_reasonable_size() {
    let f = hot();
    assert!(size_of_val(&f) < ...); // Determine value / limit at first run.
}
```

Then consider a combination of the following:

```rust,ignore
// 1) Return an `impl Future` instead, this prevents large arguments 
//    from infecting the future size, among others.
fn hot(args: Args) -> impl Future<Output = Result<T>> { 
    // 2) Process arguments outside async context if processing does
    //    not require async functionality.
    let args = args.do_something(); 

    if args.invalid() {
        // 3) Use `Either` to return a single `impl Future` type, as
        //    otherwise you'd have to invent a new type. 
        async { Err(InvalidArgs) }.left_future() 
    } else {
        // 4) Chain future invocations via future helpers, which again 
        //    prevents heavy locals from being passed through the state 
        //    machine.
        read(args).then(|x| foo(x)).right_future() 
    }
}
```
