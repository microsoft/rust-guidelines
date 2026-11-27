## Unsafe implies undefined behavior (M-UNSAFE-IMPLIES-UB)

Why: semantic consistency without warning fatigue.

The marker `unsafe` may only be applied to functions and traits if misuse implies the risk of undefined behavior (UB).
It must not be used to mark functions that are dangerous to call for other reasons.

```
// Valid use of unsafe
unsafe fn print_string(x: *const String) { }

// Invalid use of unsafe
unsafe fn delete_database() { }
```
