## Functions do not take out-parameters (C-NO-OUT)

Prefer

```
fn foo() -> (Bar, Bar)
```

over

```
fn foo(output: &mut Bar) -> Bar
```

for returning multiple `Bar` values.

Compound return types like tuples and structs are efficiently compiled and do
not require heap allocation. If a function needs to return multiple values, it
should do so via one of these types.

The primary exception: sometimes a function is meant to modify data that the
caller already owns, for example to re-use a buffer:

```
fn read(&mut self, buf: &mut [u8]) -> io::Result<usize>
```
