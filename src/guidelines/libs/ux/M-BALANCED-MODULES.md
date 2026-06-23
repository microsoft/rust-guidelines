<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Modules are balanced in size and scope (M-BALANCED-MODULES) { #M-BALANCED-MODULES }

<why>discoverable functionality and clear API usage.</why>

Your module design should approximately follow established UX practices of menu design: A _reasonable_ number of your most important items should be placed in the crate root, and a comprehensible grouping of the remaining functionality into subordinate modules.

Two violations of that rule are encountered most frequently: flat module roots containing dozens of items without clear ordering, or the excessive use of submodules without items in the crate root. While there are crates where this makes sense (e.g., automatically generated `-sys` crates defining 100s of C items, or umbrella crates like `std` and `tokio`), the majority of library crates are not among them.

When designing your module layout, consider these factors:

- Essential items users must find in order to use a crate should go into its root. For example, a `foo_client` crate should probably have its main `Client` struct inside the root.
- Other items should be grouped semantically by use case. Modules named `traits` and `errors` don't help anyone, but `account`, `network` and `status` do.
- Also take into account that modules are the perfect place for module-level documentation that further explains the respective subsystem.
