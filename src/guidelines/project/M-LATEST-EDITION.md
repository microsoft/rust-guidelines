<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## New crates target latest edition (M-LATEST-EDITION) { #M-LATEST-EDITION }

<why>access to the latest Rust features.</why>

When creating a new crate or workspace, set `edition` to the latest stable edition (at least `2024` at the time of writing); the `resolver` field is generally not needed.

Using an older edition generally has no upsides for new projects, but forces you to write 'old Rust' that is less idiomatic and has worse UX edge cases. Notably, using an older edition does _not_ grant any compatibility benefits with the rest of the ecosystem. An application based on `2015` can use libraries written for `2024` just fine.
