<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Long-Running Tasks Should Have Yield Points. (M-YIELD-POINTS) { #M-YIELD-POINTS }

<why>To ensure you don't starve other tasks of CPU time.</why>
<version>0.2</version>

If you perform long running computations, they should contain `yield().await` points.

Your future might be executed in a runtime that cannot work around blocking or long-running tasks. Even then, such tasks are
considered bad design and cause runtime overhead. If your complex task performs I/O regularly it will simply utilize these await points to preempt itself:

```rust, ignore
async fn process_items(items: &[items]) {
    // Keep processing items, the runtime will preempt you automatically.
    for i in items {
        read_item(i).await;
    }
}
```

If your task performs long-running CPU operations without intermixed I/O, it should instead cooperatively yield at regular intervals, to not starve concurrent operations:

```rust, ignore
async fn process_items(zip_file: File) {
    let items = zip_file.read().async;
    for i in items {
        decompress(i);
        yield().await;
    }
}
```

If the number and duration of your individual operations are unpredictable you should use APIs such as `has_budget_remaining()` and
related APIs to query your hosting runtime.

> ### <tip></tip> Yield how often?
>
> In a thread-per-core model the overhead of task switching must be balanced against the systemic effects of starving unrelated tasks.
>
> Under the assumption that runtime task switching takes 100's of ns, in addition to the overhead of lost CPU caches,
> continuous execution in between should be long enough that the switching cost becomes negligible (<1%).
>
> Thus, performing 10 - 100μs of CPU-bound work between yield points would be a good starting point.
