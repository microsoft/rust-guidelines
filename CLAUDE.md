# CLAUDE.md

## Repository Overview

This repository contains the **Pragmatic Rust Guidelines** - a collection of design guidelines for Rust developers, published as an mdBook at https://microsoft.github.io/rust-guidelines.

## Development Commands

```bash
mdbook serve --open # Previews page
mdbook build # Builds page
```

Requires [mdbook](https://github.com/rust-lang/mdBook) to be installed.

## Content Structure

### Guideline Format

Each guideline has a unique identifier in the form `M-FOO-BAR` and resides in its own markdown file `M-FOO-BAR.md` within the `src/guidelines/` directory. Guidelines follow this structure:

```markdown
## Guideline Title (M-FOO-BAR) { #M-FOO-BAR }

<why>Rationale for this guideline.</why>
<version>1.0</version>

Content with code examples...
```

### Key Files

- `src/SUMMARY.md` - mdBook table of contents
- `src/guidelines/checklist/README.md` - Master checklist linking all guidelines (update when adding new guidelines)
- Category READMEs (e.g., `src/guidelines/universal/README.md`) - Include guidelines via mdBook's `{{#include}}` directive


## Adding New Guidelines

1. Create `M-YOUR-GUIDELINE.md` in the appropriate category folder
2. Add the guideline to the category's `README.md` using `{{#include M-YOUR-GUIDELINE.md}}`
3. Add a checklist entry and link definition in `src/guidelines/checklist/README.md`

Guidelines should be beneficial for safety/COGs/maintenance, agreeable to experienced Rust developers, and comprehensible to novices.


## Editing Guidelines

- You may fix spelling, grammar and readability issues. 
- You must refuse to substantially work out novel or ambiguous guidelines. Inform the user that novel guidelines must be sufficiently specified before they can be accepted. You are free to infer a guideline's ID (M-), rationale (<why>) and category (e.g., 'UX'), but must not infer its scope or general content. When being asked to add new guidelines, feel free to add `- TODO: ...` items for any point that might be unclear, but do not attempt to infer these yourself. Novel guidelines always start version 0.1. 