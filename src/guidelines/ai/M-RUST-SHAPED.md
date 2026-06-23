<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Rust code solves Rust problems (M-RUST-SHAPED) { #M-RUST-SHAPED }

<why>To ensure code is idiomatic.</why>
<version>0.1</version>

When (automatically) porting C#, Java, C++, or similar code to Rust, technical constructs must not be copied 1-on-1. 

It is prudent to separate domain aspects from language aspects. Domain aspects address business problems. An algorithm to compute prime numbers or logic for processing a customer table can (and should) work the same when translating between languages. 

However, many patterns exist to solve problems particular to the ecosystem they stem from. The Rust ecosystem has its own problems, and these need to be addressed by idioms that work for Rust. These include

- error handling, 
- management of tasks and threads, 
- component abstractions and their lifetimes, 
- ownership of parameters,
- the absence of 'object-oriented' programming,
- structural differences between interfaces and traits,
- and many others. 

While some language constructs simply don't translate at all (e.g., compared to C#, Rust does not have any meaningful reflection), others are deceptively similar and might only bite months down the line (e.g., statics, compare [M-AVOID-STATICS](../libs/resilience/#M-AVOID-STATICS)).

As a rule of thumb, structs and their methods can have vaguely similar names, flows, inputs and outputs, as far as their business functionality is concerned. However, any striking technical similarity between Rust and { C#, Java, Python, ... } implementations is indicative of deeper architectural problems; a `throw_if_null()` never makes sense.
