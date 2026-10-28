---
name: pragmatic-rust-guidelines
description: Apply Pragmatic Rust Guidelines when designing, writing, reviewing, or refactoring Rust applications and libraries. Select relevant guidelines for APIs, ownership, errors, async code, documentation, testing, FFI, performance, and project structure, then assess their rationale against the user's code.
license: MIT
---

# Pragmatic Rust Guidelines

Use this skill on the user's Rust project, not on the book repository.
Resolve all reference paths from this skill's directory.
The package contains its Markdown references and images.
It does not require the book checkout or network access to those references.

## Select Relevant Guidelines

Read only the catalogs relevant to the task.
Use [the catalog overview](references/CATALOG.md) when the task crosses categories.
Each catalog lists guideline identifiers, descriptions, search terms, and draft status.

| Area | Catalog |
| --- | --- |
| General Rust design, naming, formatting, and automated checks | [Universal](references/catalogs/universal.md) |
| Library design overview | [Libraries](references/catalogs/libs.md) |
| External types, traits, and runtime interoperability | [Library Interoperability](references/catalogs/libs/interop.md) |
| Public APIs, builders, errors, modules, and async functions | [Library UX](references/catalogs/libs/ux.md) |
| Invariants, testability, state, and resilience | [Library Resilience](references/catalogs/libs/resilience.md) |
| Features, dependencies, and native library builds | [Library Building](references/catalogs/libs/building.md) |
| Declarative and procedural macros | [Macros](references/catalogs/macros.md) |
| Application errors, allocation, and processor targets | [Applications](references/catalogs/apps.md) |
| Foreign interfaces and native library boundaries | [FFI](references/catalogs/ffi.md) |
| Panics, soundness, and unsafe code | [Correctness](references/catalogs/correctness.md) |
| Allocation, data layout, throughput, and profiling | [Performance](references/catalogs/performance.md) |
| Workspaces, editions, and supported Rust versions | [Project](references/catalogs/project.md) |
| API documentation and examples | [Documentation](references/catalogs/docs.md) |
| AI-readable code, visibility, and meaningful tests | [AI](references/catalogs/ai.md) |

Follow the catalog links to the individual guidelines needed for the task.
Read linked guidelines when their rationale affects the same decision.
Do not load the entire reference collection.
If the code reveals another relevant area, read that area's catalog.

## Apply the Guidelines

1. Establish the crate's role, public API commitments, supported platforms, and compatibility requirements.
2. Read the relevant code, tests, and project instructions before recommending a change.
3. Use the project's configured automated checks for issues those tools already cover.
4. Read the selected guidelines and evaluate their rationale against the actual code.
5. Distinguish required rules from recommendations that permit justified exceptions.
6. If changes are requested, make the smallest change that addresses the identified issue.
7. Preserve behavior and public compatibility unless the user requests a change.
8. Follow the user's execution policy and use the project's existing validation tools.
9. Report the guideline identifiers, affected project locations, evidence, and any justified exceptions.

For code that is not yet written, use the guidelines to compare design choices before choosing an implementation.
For reviews, report actionable findings rather than applying every guideline mechanically.
Do not rewrite unrelated code solely to satisfy a guideline.

## Interpret Scope and Evidence

Apply the spirit of a guideline rather than its wording alone.
If a guideline conflicts with its underlying motivation, explain the conflict instead of following it blindly.
Treat guidelines marked as drafts as investigation prompts, not established rules.
If a source cross-reference names an unavailable guideline, report it rather than inventing guidance.

For unsafe code, explain the invariants and the evidence that supports them.
For performance changes, distinguish measured improvements from hypotheses.
Do not replace an implementation solely because a reference names a different crate.
State missing evidence and unresolved risks instead of claiming that a guideline proves correctness or performance.
