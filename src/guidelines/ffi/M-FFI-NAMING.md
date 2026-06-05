<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## FFI crates follow established naming conventions (M-FFI-NAMING) { #M-FFI-NAMING }

<why>to make the role of crates immediately recognizable across projects.</why>
<version>0.1</version>

Crates used for FFI should follow established naming practices:

- `-sys` for crates defining items to call into existing (C-style) libraries 
- `-ffi` for crates defining (C-style) items when called from existing applications 

There are slight variations of this scheme (e.g., `-sys2` when a previous `-sys` crate was abandoned and using `-` vs `_`), but overall one clearly defines 'export' libraries, the other one 'import' ones.
