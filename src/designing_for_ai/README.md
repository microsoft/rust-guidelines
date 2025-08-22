<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

# Designing for AI

It's becoming increasingly important to design APIs and components that can easily be understood and programmed
using AI coding agents. As a general rule, making APIs easier to use for humans also makes them easier to use by
AI, so if you're following the guidelines in this book, you'll be in good shape.

With that said, there are a few guidelines which are particularly important to help make AI coding in Rust more effective:

* **Create Idiomatic Rust API Patterns**. The more your APIs, whether public or internal, look and feel like the majority of
Rust code in the world, the better it is for AI. Follow the guidelines from the [Rust API Guidelines](https://rust-lang.github.io/api-guidelines/checklist.html)
along with the guidelines from [Library / UX](../guidelines/libs/ux).

* **Provide Thorough Docs**. AI agents love good detailed docs. Include docs for all of your modules and all the public items in your crates.
Assume the reader has a solid, but not expert, level of understanding of Rust and that the reader understands the standard library.
Follow
[C-CRATE-DOC](https://rust-lang.github.io/api-guidelines/checklist.html#c-crate-doc),
[C-FAILURE](https://rust-lang.github.io/api-guidelines/checklist.html#c-failure),
[C-LINK](https://rust-lang.github.io/api-guidelines/checklist.html#c-link), and
[M-MODULE-DOCS](../guidelines/docs/#M-MODULE-DOCS)
[M-CANONICAL-DOCS](../guidelines/docs/#M-CANONICAL-DOCS).

* **Provide Thorough Examples**. Your documentation should have many directly usable examples, and the repository should include additional fuller examples.
Follow
[C-EXAMPLE](https://rust-lang.github.io/api-guidelines/checklist.html#c-example)
[C-QUESTION-MARK](https://rust-lang.github.io/api-guidelines/checklist.html#c-question-mark).

* **Use Strong Types**. Avoid [primitive obsession](https://refactoring.guru/smells/primitive-obsession) by using strong types with strict well-documented semantics.
Follow
[C-NEWTYPE](https://rust-lang.github.io/api-guidelines/checklist.html#c-newtype).

* **Use Errors Instead of Panicking**. Panics should be reserved for programming error and not be part of the normal
control flow for a production application. Parsers should usually not panic, I/O failures should not lead to a panic.
Instead, use return robust errors following the normal Rust conventions.

* **Make Your APIs Testable**. Design APIs which allow your customers to test their use of your API in unit tests. This might involve introducing some mocks, fakes,
or cargo features. AI agents need to be able to iterate quickly to prove that the code they are writing that calls your API is working
correctly.
