<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Parameter ordering is consistent (M-PARAMETER-CONSISTENCY) { #M-PARAMETER-CONSISTENCY }

<why>To reduce development friction.</why>

When the same conceptual parameters appear in multiple functions (within a crate or across crates in the same ecosystem), they should appear in the same order everywhere:

- important or call-specific parameters should generally go first,
- ubiquitous parameters rather go last (e.g., `&logger`),
- closures always go last (functions should not accept more than one closure).

```rust,ignore
// Bad, the order of `user_id` and `tenant_id` flips between functions, and
// the logger sometimes appears first, sometimes last.
fn create_user(logger: &Logger, user_id: UserId, tenant_id: TenantId) -> Result<()> { ... }
fn delete_user(tenant_id: TenantId, user_id: UserId, logger: &Logger) -> Result<()> { ... }
fn rename_user(user_id: UserId, new_name: &str, tenant_id: TenantId, logger: &Logger) -> Result<()> { ... }

// Good, call-specific parameters first in a consistent order, ubiquitous
// `logger` always last.
fn create_user(tenant_id: TenantId, user_id: UserId, logger: &Logger) -> Result<()> { ... }
fn delete_user(tenant_id: TenantId, user_id: UserId, logger: &Logger) -> Result<()> { ... }
fn rename_user(tenant_id: TenantId, user_id: UserId, new_name: &str, logger: &Logger) -> Result<()> { ... }
```
