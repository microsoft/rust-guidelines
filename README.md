# Pragmatic Rust Guidelines

A collection of pragmatic design guidelines helping developers to produce idiomatic Rust that scales.

👉 [**Pragmatic Rust Guidelines**](https://microsoft.github.io/rust-guidelines)

## Use with GitHub Copilot

This repository is also a Copilot plugin marketplace with one plugin,
`rust-guidelines`, containing one skill of the same name. The plugin lives in
[`ai-skill`](ai-skill); the discovery catalog is
[`.github/plugin/marketplace.json`](.github/plugin/marketplace.json).
The skill bundles a trigger index and individual `rules/<ID>.md` files, loading
only the guidelines applicable to the current task. It works offline after
installation; the rules do not need to be fetched from the web.

The skill is adapted from rust-dev's
[`rust-core-guidelines`](https://github.com/agency-microsoft/playground/tree/0dca309355d50ee610b1b3c45f283019592b40d1/plugins/rust-dev/skills/rust-core-guidelines):
the index and all 144 rule files are retained, the skill is renamed to
`rust-guidelines`, and the dependency on the separate `rust-task-docs` skill is
removed. The bundled rules cover the Pragmatic Rust Guidelines and the Rust API
Guidelines. Their original
[license notices](ai-skill/skills/rust-guidelines/licenses) are included.
The rule files are a verbatim snapshot; their local Markdown lint configuration
preserves upstream formatting without relaxing linting for the skill entry point.

### Copilot CLI

With a current [GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli)
installed and signed in, register this fork's marketplace and install the plugin:

```shell
copilot plugin marketplace add Vaiz/rust-guidelines
copilot plugin install rust-guidelines@pragmatic-rust-guidelines
```

Start a new Copilot session and run `/skills list` to confirm that
`rust-guidelines` is available. Ask Copilot to use the skill, for example:

```text
Use the rust-guidelines skill to review the Rust code in this project.
```

To try a local checkout before publishing, register the repository root as a
local marketplace instead of the GitHub repository:

```shell
copilot plugin marketplace add .
copilot plugin install rust-guidelines@pragmatic-rust-guidelines
```

Run these commands from the repository root. Local marketplace plugins load
directly from the checkout; start a new session after editing the skill.

### Other Copilot clients

In a Copilot client that supports plugin marketplaces, add
`https://github.com/Vaiz/rust-guidelines` as a marketplace and install
`rust-guidelines`. See the
[client-specific installation instructions](https://docs.github.com/en/copilot/reference/plugin-and-marketplace-reference#use-plugins).
Marketplace support varies by client; this plugin contains a standard
`skills/rust-guidelines/SKILL.md` skill and does not require MCP servers or hooks.

## Development

The guidelines use [mdbook](https://github.com/rust-lang/mdBook). Once installed you can view them locally via

```bash
mdbook serve --open
```

To submit new guidelines, file a PR. They should be

- beneficial for { safety, COGs, maintenance },
- agreeable to a majority of experienced (3+ years) Rust developers,
- comprehensible to Rust novices (4+ weeks),
- practically applicable in real world scenarios.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft trademarks or logos is
subject to and must follow Microsoft’s Trademark & Brand Guidelines. Use of Microsoft trademarks or logos in modified versions of this
project must not cause confusion or imply Microsoft sponsorship. Any use of third-party trademarks or logos are subject to those
third-party’s policies.
