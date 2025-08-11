<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Features are Additive  (M-FEATURES-ADDITIVE) { #M-FEATURES-ADDITIVE }

<why>To prevent compilation breakage in large and complex projects.</why>
<guideline-status><active>1.0</active></guideline-status>

All library features must be additive, and any combination must work, as long as the feature itself would work on the current platform. This implies:

- [ ] You must not introduce a `no-std` feature, use a `std` feature instead
- [ ] Adding any feature `foo` must not disable or modify any public item
  - Adding enum variants is fine if these enums are `#[non_exhaustive]`
- [ ] Features must not rely on other features to be manually enabled
- [ ] Features must not rely on their parent to skip-enable a feature in one of their children

Further Reading

- [Feature Unification](https://doc.rust-lang.org/cargo/reference/features.html#feature-unification)
- [Mutually Exclusive Features](https://doc.rust-lang.org/cargo/reference/features.html#mutually-exclusive-features)
