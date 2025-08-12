<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## First Sentence is One Line; Approx. 15 Words (M-FIRST-DOC-SENTENCE) { #M-FIRST-DOC-SENTENCE }

<why>To make API docs easily skimmable.</why>
<version>1.0</version>

When you document your item, the first sentence becomes the "summary sentence" that is extracted and shown in the module summary:

```rust
/// This is the summary sentence, shown in the module summary.
///
/// This is other documentation. It is only shown in that item's detail view.
/// Sentences here can be as long as you like and it won't cause any issues.
fn some_item() { }
```

Since Rust API documentation is rendered with a fixed max width, there is a naturally preferred sentence length you should not
exceed to keep things tidy on most screens.

If you keep things in a line, your docs will become easily skimmable. Compare, for example, the standard library:

![TEXT](M-FIRST-DOC-SENTENCE_GOOD.png)

Otherwise, you might end up with _widows_ and a generally unpleasant reading flow:

![TEXT](M-FIRST-DOC-SENTENCE_BAD.png)

As a rule of thumb, the first sentence should not exceed **15 words**.
