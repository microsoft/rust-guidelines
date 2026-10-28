<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

# Agent Skill

The Pragmatic Rust Guidelines skill helps agents design, write, review, and refactor Rust code in your own project.
It contains instructions, category catalogs, individual guideline Markdown files, and supporting images.
The agent reads relevant references as needed rather than loading the entire book.

## Download and Install

Download the [pragmatic-rust-guidelines skill](pragmatic-rust-guidelines.zip).
Extract the archive into the skills directory supported by your agent.
Keep the complete `pragmatic-rust-guidelines` directory, including `SKILL.md`, `LICENSE.md`, and `references/`.

For GitHub Copilot, run this command from the root of your target Rust project.
Replace the archive path with the location of your downloaded file.

```bash
unzip /path/to/pragmatic-rust-guidelines.zip -d .github/skills
```

This creates `.github/skills/pragmatic-rust-guidelines/SKILL.md` and its bundled references in your project.
For other agents, use their documented skills directory.
See [GitHub's agent skill documentation](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills) for supported installation locations.

## Use the Skill

Ask your agent to use `pragmatic-rust-guidelines` when designing an API, writing Rust code, or reviewing an existing crate.
The skill directs the agent to read the relevant catalogs and individual guidelines.
It requires the agent to evaluate each guideline's rationale and to respect your project's compatibility and validation constraints.

The package works without a checkout of this book or network access to its references.
Draft guidelines remain investigation prompts, not established rules.
The agent must explain justified exceptions rather than applying every guideline mechanically.
Links between guidelines resolve to the bundled files.
If a source cross-reference names an unavailable guideline, the package links to an explicit reference note instead of inventing guidance.

## Updates and Source

Each published book build generates a new skill archive from the same guideline sources.
Keep a copy of the archive used by your project when you need reproducible advice.
The catalog records the book version.

The [skill template](https://github.com/microsoft/rust-guidelines/blob/main/skill/SKILL.md) contains the instructions used in the download.
Its reference files are bundled during packaging, not maintained as a second authored copy.
The package includes the project's MIT license.
