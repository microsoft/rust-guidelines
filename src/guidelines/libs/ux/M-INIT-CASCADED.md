<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Complex Type Initialization Hierarchies are Cascaded (M-INIT-CASCADED) { #M-INIT-CASCADED }

<why>To prevent misuse and accidental parameter mix ups.</why>
<guideline-status><draft/></guideline-status>

Types that require 4+ parameters should cascade their initialization via helper types.

```rust, ignore
# struct Transaction;
impl Transaction {
    // Easy to confuse parameters and signature generally unwieldy.
    pub fn new(from_bank: &str, from_customer: &str, to_bank: &str, to_customer: &str) -> Self { }
}
```

Instead of providing a long parameter list, parameters should be grouped semantically. When applying this guideline,
also check if [M-NEWTYPES-OVER-PRIMITIVES] is applicable:

```rust, ignore
# struct Transaction;
# struct Account;
impl Transaction {
    // Better, signature cleaner
    pub fn new(from: Account, to: Account) -> Self { }
}

impl Account {
    pub fn new_ok(bank: &str, customer: &str) -> Self { }
    pub fn new_even_better(bank: Bank, customer: Customer) -> Self { }
}
```

[M-NEWTYPES-OVER-PRIMITIVES]: /guidelines/libs/resilience/#M-NEWTYPES-OVER-PRIMITIVES
