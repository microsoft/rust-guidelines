<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Test Utilities are Feature Gated (M-TEST-UTIL) { #M-TEST-UTIL }

<why>To prevent production builds from accidentally bypassing safety checks.</why>
<version>0.2</version>

Testing functionality must be guarded behind a feature flag. This includes

- mocking functionality ([M-MOCKABLE-SYSCALLS]),
- the ability to inspect sensitive data,
- safety check overrides,
- fake data generation.

We recommend you use a single flag only, named `test-util`. In any case, the feature(s) must clearly communicate they are for testing purposes.

```rust, ignore
impl HttpClient {
    pub fn get() { ... }

    #[cfg(feature = "test-util")]
    pub fn bypass_certificate_checks() { ... }
}
```

[M-MOCKABLE-SYSCALLS]: /guidelines/libs/resilience/#M-MOCKABLE-SYSCALLS
