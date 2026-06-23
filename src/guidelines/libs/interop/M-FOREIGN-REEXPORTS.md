<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Items come from their original crate (M-FOREIGN-REEXPORTS) { #M-FOREIGN-REEXPORTS }

<why>to avoid type confusion.</why>
<version>0.1</version>

Crates should generally not re-export items from other crates. For example, if your crate contains a method `foo::download(url: bar::Url)`, you should not do `pub use bar::Url` from inside `foo`. This avoids having possibly dozens of aliases in context, which can get confusing for both users and agents, in particular if these are mixed with genuinely different types of the same name from other crates.

When a crate accepts or returns a type defined in some third-party crate, users are expected to depend on that third-party crate directly and import the type from there. That said, there are a few valid exceptions to this rule:

- Umbrella crates (compare [M-DONT-LEAK-TYPES](./#M-DONT-LEAK-TYPES)) by definition re-export other types
- Crates split for technical reasons (e.g., exporting `foo_core::Url` from `foo`)
- Macro use to provide stable paths, e.g., via some hidden `foo::__private::Url`
