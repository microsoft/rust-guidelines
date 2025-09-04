<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Complex Type Initialization Hierarchies are Cascaded (M-INIT-CASCADED) { #M-INIT-CASCADED }

<why>To prevent misuse and accidental parameter mix ups.</why>
<version>1.0</version>

Types that require 4+ parameters should cascade their initialization via helper types.

```rust, ignore
# struct Deposit;
impl Deposit {
    // Easy to confuse parameters and signature generally unwieldy.
    pub fn new(bank_name: &str, customer_name: &str, currency_name: &str, currency_amount: u64) -> Self { }
}
```

Instead of providing a long parameter list, parameters should be grouped semantically. When applying this guideline,
also check if [C-NEWTYPE] is applicable:

```rust, ignore
# struct Deposit;
# struct Account;
# struct Currency
impl Deposit {
    // Better, signature cleaner
    pub fn new(account: Account, amount: Currency) -> Self { }
}

impl Account {
    pub fn new_ok(bank: &str, customer: &str) -> Self { }
    pub fn new_even_better(bank: Bank, customer: Customer) -> Self { }
}
```

[C-NEWTYPE]: https://rust-lang.github.io/api-guidelines/type-safety.html#c-newtype
