<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

# About

A collection of pragmatic design guidelines helping service developers to produce idiomatic Rust that scales.

## Meta Design Principles

We build on existing high-quality guidelines, most notably the [Rust API Guidelines](https://rust-lang.github.io/api-guidelines/checklist.html),
addressing topics often encountered by Rust developers. For a guideline to make it into this book, we expect it to meet the following criteria:

- [ ] It positively affects { safety, COGs, maintenance }; i.e., it must where applicable
  - [ ] promote **safety best-practices** and prevent sources of risk
  - [ ] lead to **high throughput**, **low latency**, and **low memory usage**
  - [ ] make code **readable and understandable**
- [ ] A majority of experienced (3+ years) **Rust developers would agree with the guideline**.
- [ ] The guideline is **reasonably comprehensible** to Rust novices (4+ weeks).
- [ ] It is **pragmatic**, as unrealistic guidelines won't be followed.

## Applicability

Guidelines declared _must_ are supposed to always hold, where _should_ guidelines indicate more flexibility.

That said, teams are free to adopt these guidelines as they see fit, and you occasionally might have good reasons to do things differently.

We recommend you try to apply all items to your project. If an item does not make sense, get in touch. Either the item has
issues and we should update it, or it does not apply (and we might update it anyway to point these edge cases out).

> ### <tip></tip> The Golden Rule
>
> Each item here exists for a reason; and it is the spirit that counts, not the letter.
>
> Before attempting to work around a guideline, you should understand why it exists and what it tries to safeguard.
> Likewise, you should not blindly follow a guideline if it becomes apparent that doing so would violate its underlying motivation!

## Guideline Maturity

Since the guidelines are under active development, each is marked to indicate its maturity:

- <active>X.Y</active> guidelines are meant to be _taken seriously_, and teams should treat them as enabled lints. Active guidelines come with a semantic
version `X.Y`, where `Y` will be incremented if the guideline changed in a significant way, and `X` if the guideline would be outright conflicting with its
previous version. Minor changes and clarifications are not tracked.
- <draft></draft> guidelines have been newly added. You should attempt to apply them, but not at a significant refactoring cost yet. If you run into issues
please let us know.
- <deprecated></deprecated> guidelines are not active anymore and preserved for archeological reasons.

## Submitting New Guidelines

Do you have a practical guideline that leads to better safety, COGS or maintainability? We'd love to hear from you!
Here is the process you should follow:

- Check if your guideline follows the [meta design principles](#meta-design-principles) above.
- Check if your suggestion is not already covered by the [API Guidelines](https://rust-lang.github.io/api-guidelines/checklist.html) or [Clippy](https://rust-lang.github.io/rust-clippy/master/?groups).
- File a [PR or issue](https://github.com/microsoft/rust-guidelines).
