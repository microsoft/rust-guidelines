<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Names of items are short (M-SHORT-NAMES) { #M-SHORT-NAMES }

<why>Short names read faster, fit on one line at call sites, and discourage smuggling implementation detail or hedge words into identifiers; the surrounding type and module context usually carries the rest of the meaning.</why>
<version>0.1</version>

Identifiers for items (functions, methods, types, fields, modules) should stay short, leaning on context — the enclosing module, type, or trait — to disambiguate rather than encoding it into the name itself.

- TODO: Give a concrete length guideline or heuristic (e.g., prefer one or two words for methods on a type; avoid restating the type name in its methods).
- TODO: Specify when longer names are warranted (rare public free functions where disambiguation is unavoidable, low-level safety-critical APIs).
- TODO: Clarify the relationship to M-WEASEL-WORDS (which targets weasel words) — this rule is about overall length, not specifically filler words.
- TODO: Provide a concrete bad example (`UserService::get_user_by_id_from_database`).
- TODO: Provide a concrete good example (`UserService::get(id)` or `Users::find(id)`).
- TODO: Note interaction with the Rust API Guidelines naming conventions and M-WEASEL-WORDS.
