<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Applications target highest viable target-cpu (M-TARGET-CPU) { #M-TARGET-CPU }

<why>to improve fleet performance.</why>
<version>0.1</version>

Server applications should compile against the highest `target-cpu` that the deployment environment is guaranteed to support, rather than defaulting to the generic baseline. 

This can be achieved, for example, by setting inside `.cargo/config.toml`:

```toml
[target.x86_64-unknown-linux-gnu]
rustflags = ["-C", "target-cpu=x86-64-v3"]
```

Note this guideline applies only to applications, as target settings are ignored for libraries.
