<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Reuse allocations where possible (M-MEM-REUSE) { #M-MEM-REUSE }

<why>To reduce allocation overhead and improve performance in hot paths.</why>

When designing APIs you should allow users to hold onto reusable resources. Inside your code you should make use of them where available.

The cost of repeated allocations inside hot loops can be significant, and from a user's perspective they can be invisible unless profiled:

```rust,ignore
// Bad, API design forces new allocation per element.
for id in ids {
    let value = db.get(id);
}
```

While this style of API may exist for convenience, it should be auxiliary. Instead, the core APIs should allow users to own the underlying object and re-use it:

```rust,ignore
// Good, allows users to decide whether a new allocation is needed.
let mut value = Value::new();
for id in ids {
    db.get_in(id, &mut value);
}
```

The canonical method on reusable types to reuse them is `.clear()`, as can be found on many `std` items. Multiple flavors of this pattern exist. In simple cases user-owned types can hold a preexisting, reusable collection directly:

```rust
struct Value {
    data: Vec<u8>
}
```

In heavyweight, deeply nested libraries it can be worthwhile to either pass a bump-style `Arena`, or to encapsulate one inside the user types, so it can be used throughout the call stack:

```rust,ignore
struct Query {
    arena: Arena,
    request: Request,
    data: Vec<u8>    
}

fn client_do_work(query: &mut Query) {
    let request = rewrite_request(&query.request, &query.arena);
    get_in(request, &mut query.data);
}
```
