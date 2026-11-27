## Prefer 'macros by example' over proc macros (M-EXAMPLE-OVER-PROC)

Why: easy macro inspection and fast compilation.

When a 'macro by example' can do the job, it should be preferred over proc macros.

Proc macros are more powerful, but their expansion can't easily be inspected. Where this versatility isn't needed, a simple 'macro by example' is the better option.

```
// Bad, attribute macro requires proc macro machinery, can be hard to 
// inspect in some IDEs, and isn't needed here.
#[make_new_id]
struct MyId;

// Good, easier to write, maintain and inspect, faster compilation speed.
make_new_id!(MyId);
```
