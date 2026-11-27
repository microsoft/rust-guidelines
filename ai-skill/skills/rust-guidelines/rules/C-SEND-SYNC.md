## Types are `Send` and `Sync` where possible (C-SEND-SYNC)

[`Send`] and [`Sync`] are automatically implemented when the compiler determines
it is appropriate.

[`Send`]: https://doc.rust-lang.org/std/marker/trait.Send.html
[`Sync`]: https://doc.rust-lang.org/std/marker/trait.Sync.html

In types that manipulate raw pointers, be vigilant that the `Send` and `Sync`
status of your type accurately reflects its thread safety characteristics. Tests
like the following can help catch unintentional regressions in whether the type
implements `Send` or `Sync`.

```
#[test]
fn test_send() {
    fn assert_send<T: Send>() {}
    assert_send::<MyStrangeType>();
}

#[test]
fn test_sync() {
    fn assert_sync<T: Sync>() {}
    assert_sync::<MyStrangeType>();
}
```
