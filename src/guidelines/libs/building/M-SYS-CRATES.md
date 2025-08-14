<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Native `-sys` Crates Compile Without Dependencies (M-SYS-CRATES) { #M-SYS-CRATES }

<why>To have libraries that 'just work' on all platforms.</why>
<version>0.2</version>

If you author a pair of `foo` and `foo-sys` crates wrapping a native `foo.lib`, you are likely to run into the issues described
in [M-OOBE].

Follow these steps to produce a crate that _just works_ across platforms:

- [ ] fully govern the build of `foo.lib` from `build.rs` inside `foo-sys`. Only use hand-crafted compilation via the
  [cc](https://crates.io/crates/cc) crate, do _not_ run Makefiles or external build scripts, as that will require the installation of external dependencies,
- [ ] make all external tools optional, such as `nasm`,
- [ ] embed the upstream source code in your crate,
- [ ] make the embedded sources verifiable (e.g., include Git URL + hash),
- [ ] pre-generate `bindgen` glue if possible,
- [ ] support both static linking, and dynamic linking via [libloading](https://crates.io/crates/libloading/0.8.6).

Deviations from these points can work, and can be considered on a case-by-case basis:

If the native build system is available as an _OOBE_ crate, that can be used instead of `cc` invocations. The same applies to external tools.

Source code might have to be downloaded if it does not fit crates.io size limitations. In any case, only servers with an availability
comparable to crates.io should be used. In addition, the specific hashes of acceptable downloads should be stored in the crate and verified.

Downloading sources can fail on hermetic build environments, therefore alternative source roots should also be specifiable (e.g., via environment variables).

[M-OOBE]: ./#M-OOBE
