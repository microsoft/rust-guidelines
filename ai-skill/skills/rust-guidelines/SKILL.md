---
name: rust-guidelines
description: Apply the Pragmatic Rust Guidelines when writing, refactoring, or reviewing Rust code, designing Rust APIs, or changing Rust tests, documentation, Cargo workspaces, unsafe code, or FFI.
license: MIT
---

# Pragmatic Rust Guidelines

Use the [Pragmatic Rust Guidelines](https://microsoft.github.io/rust-guidelines/)
as the source of truth. This skill covers both application and library code.

## Workflow

1. Read the repository's instructions and the code affected by the task.
   Identify the intended behavior, public contracts, and supported Rust version.
2. Read the [applicability and golden rule](https://microsoft.github.io/rust-guidelines/guidelines/).
   Distinguish requirements from recommendations and respect their exceptions.
3. Use the topic map below to read the relevant guidelines before changing or
   reviewing code. Start with universal guidelines; add topics as needed.
   Use the [checklist](https://microsoft.github.io/rust-guidelines/guidelines/checklist/)
   for broader reviews, not as a substitute for reading a guideline's rationale.
4. Apply the relevant guidance to each changed type, signature, implementation,
   and test. Preserve existing behavior unless the task calls for changing it.
5. Run the repository's appropriate formatting, lint, and targeted test commands.
   Report concrete findings and any validation that could not be completed.

## Topic map

All links point to the public book. Read only the topics needed for the task.

| Topic | Reference | Focus |
| --- | --- | --- |
| Baseline | [Universal](https://microsoft.github.io/rust-guidelines/guidelines/universal/) | Idioms, names, diagnostics, lint exceptions, public types |
| AI-assisted code | [AI](https://microsoft.github.io/rust-guidelines/guidelines/ai/) | Idiomatic APIs, focused paths, meaningful tests |
| Errors and panics | [Correctness](https://microsoft.github.io/rust-guidelines/guidelines/correctness/) | Expected failures versus bugs, panic contracts, soundness |
| Ownership and API design | [Library UX](https://microsoft.github.io/rust-guidelines/guidelines/libs/ux/) | Simple abstractions, builders, canonical errors, async APIs |
| Types and testability | [Library resilience](https://microsoft.github.io/rust-guidelines/guidelines/libs/resilience/) | Strong types and guarded invariants, injectable I/O, integration tests |
| Conversions and interoperability | [Library interoperability](https://microsoft.github.io/rust-guidelines/guidelines/libs/interop/) | Standard traits, borrowed views, ranges, Send, exposed dependencies |
| Cargo and features | [Library building](https://microsoft.github.io/rust-guidelines/guidelines/libs/building/) | Additive features, usable defaults, native dependencies |
| Workspace layout and toolchain | [Project](https://microsoft.github.io/rust-guidelines/guidelines/project/) | Workspaces, crate layout, edition, MSRV |
| Unsafe code | [Correctness](https://microsoft.github.io/rust-guidelines/guidelines/correctness/) | Safety obligations, undefined behavior, sound abstractions |
| FFI | [FFI](https://microsoft.github.io/rust-guidelines/guidelines/ffi/) | Boundary translation, names, isolated library state |
| Performance and concurrency | [Performance](https://microsoft.github.io/rust-guidelines/guidelines/performance/) | Measured hot paths, allocation, throughput, async stacks and yield points |
| Documentation | [Documentation](https://microsoft.github.io/rust-guidelines/guidelines/docs/) | Canonical docs, first sentences, inline and module documentation |
| Macros | [Macros](https://microsoft.github.io/rust-guidelines/guidelines/macros/) | Simpler alternatives, predictable expansion, procedural macro structure |
| Applications | [Applications](https://microsoft.github.io/rust-guidelines/guidelines/apps/) | Application errors, allocator and target choices |

For a task spanning many topics, the complete
[agent-readable guidelines](https://microsoft.github.io/rust-guidelines/agents/all.txt)
are available as plain text. Prefer topic pages when the full document is not
needed. Follow relevant Rust API Guidelines links from the book as appropriate.

## Applying and reviewing guidance

- Check applicability before enforcing a rule. Explain a repository-policy
  conflict or a justified exception rather than silently overriding it.
- Use the guideline's actual identifier, such as `M-STRONG-TYPES`, when explaining
  a design choice or reporting a violation. Do not invent identifiers.
- For a finding, identify the affected file and location, the guideline, the
  concrete consequence, and the smallest useful correction. Distinguish defects
  from recommendations; do not report a preference as a correctness failure.
- Inspect constructors, conversions, deserialization, and mutation when checking
  invariants. Inspect error paths and tests as well as the happy path.
- Keep fixes within scope. Reuse existing abstractions and avoid gratuitous
  dependency changes, migrations, or unrelated cleanup.
- Verify dependency APIs against the project's pinned versions. A guideline or
  upstream example does not establish that an API exists in the version in use.
- If a referenced page cannot be read, say which guidance is unavailable. Use
  accessible repository documentation, but do not claim to have checked unread
  guidelines or reconstruct their contents from their names.

The book remains authoritative; this skill intentionally links to it instead of
maintaining a second, potentially divergent set of Rust rules.
