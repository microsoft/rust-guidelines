<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

# Checklist

- **Universal**
  - [ ] Follow the upstream guidelines ([M-UPSTREAM-GUIDELINES])
  - [ ] Use static verification ([M-STATIC-VERIFICATION])
  - [ ] Lint overrides should use `#[expect]` ([M-LINT-OVERRIDE-EXPECT])
  - [ ] Public types are Debug ([M-PUBLIC-DEBUG])
  - [ ] Public types meant to be read are Display ([M-PUBLIC-DISPLAY])
  - [ ] If in doubt, split the crate ([M-SMALLER-CRATES])
  - [ ] Names are free of weasel words ([M-CONCISE-NAMES])
  - [ ] Prefer regular over associated functions ([M-REGULAR-FN])
  - [ ] Panic means 'stop the program' ([M-PANIC-IS-STOP])
  - [ ] Detected programming bugs are panics, not errors ([M-PANIC-ON-BUG])
  - [ ] Magic values are documented ([M-DOCUMENTED-MAGIC])
  - [ ] Use structured logging with message templates ([M-LOG-STRUCTURED])
- **Library / Interoperability**
  - [ ] Types are Send ([M-TYPES-SEND])
  - [ ] Native escape hatches ([M-ESCAPE-HATCHES])
  - [ ] Don't leak external types ([M-DONT-LEAK-TYPES])
- **Library / UX**
  - [ ] Abstractions don't visibly nest ([M-SIMPLE-ABSTRACTIONS])
  - [ ] Avoid smart pointers and wrappers in APIs ([M-AVOID-WRAPPERS])
  - [ ] Prefer types over generics, generics over dyn traits ([M-DI-HIERARCHY])
  - [ ] Errors are canonical structs ([M-ERRORS-CANONICAL-STRUCTS])
  - [ ] Complex type construction has builders ([M-INIT-BUILDER])
  - [ ] Complex type initialization hierarchies are cascaded ([M-INIT-CASCADED])
  - [ ] Services are Clone ([M-SERVICES-CLONE])
  - [ ] Accept `impl AsRef<>` where feasible ([M-IMPL-ASREF])
  - [ ] Accept `impl RangeBounds<>` where feasible ([M-IMPL-RANGEBOUNDS])
  - [ ] Accept `impl 'IO'` where feasible ('sans IO') ([M-IMPL-IO])
  - [ ] Essential functionality should be inherent ([M-ESSENTIAL-FN-INHERENT])
- **Library / Resilience**
  - [ ] I/O and system calls are mockable ([M-MOCKABLE-SYSCALLS])
  - [ ] Test utilities are feature gated ([M-TEST-UTIL])
  - [ ] Use the proper type family ([M-STRONG-TYPES])
  - [ ] Don't glob re-export items ([M-NO-GLOB-REEXPORTS])
  - [ ] Avoid statics ([M-AVOID-STATICS])
- **Library / Building**
  - [ ] Libraries work out of the box ([M-OOBE])
  - [ ] Native `-sys` crates compile without dependencies ([M-SYS-CRATES])
  - [ ] Features are additive ([M-FEATURES-ADDITIVE])
- **Applications**
  - [ ] Use mimalloc for apps ([M-MIMALLOC-APP])
  - [ ] Applications may use Anyhow or derivatives ([M-APP-ERROR])
- **FFI**
  - [ ] Isolate DLL state between FFI libraries ([M-ISOLATE-DLL-STATE])
- **Safety**
  - [ ] Unsafe needs reason, should be avoided ([M-UNSAFE])
  - [ ] Unsafe implies undefined behavior ([M-UNSAFE-IMPLIES-UB])
  - [ ] All code must be sound ([M-UNSOUND])
- **Performance**
  - [ ] Optimize for throughput, avoid empty cycles ([M-THROUGHPUT])
  - [ ] Identify, profile, optimize the hot path early ([M-HOTPATH])
  - [ ] Long-running tasks should have yield points ([M-YIELD-POINTS])
- **Documentation**
  - [ ] First sentence is one line; approx. 15 words ([M-FIRST-DOC-SENTENCE])
  - [ ] Has comprehensive module documentation ([M-MODULE-DOCS])
  - [ ] Documentation has canonical sections ([M-CANONICAL-DOCS])
  - [ ] Mark `pub use` items with `#[doc(inline)]` ([M-DOC-INLINE])
- **AI**
  - [ ] Design with AI use in mind ([M-DESIGN-FOR-AI])

<!-- Universal  -->
[M-UPSTREAM-GUIDELINES]: ../universal/#M-UPSTREAM-GUIDELINES
[M-STATIC-VERIFICATION]: ../universal/#M-STATIC-VERIFICATION
[M-LINT-OVERRIDE-EXPECT]: ../universal/#M-LINT-OVERRIDE-EXPECT
[M-PUBLIC-DEBUG]: ../universal/#M-PUBLIC-DEBUG
[M-PUBLIC-DISPLAY]: ../universal/#M-PUBLIC-DISPLAY
[M-SMALLER-CRATES]: ../universal/#M-SMALLER-CRATES
[M-CONCISE-NAMES]: ../universal/#M-CONCISE-NAMES
[M-REGULAR-FN]: ../universal/#M-REGULAR-FN
[M-PANIC-IS-STOP]: ../universal/#M-PANIC-IS-STOP
[M-PANIC-ON-BUG]: ../universal/#M-PANIC-ON-BUG
[M-DOCUMENTED-MAGIC]: ../universal/#M-DOCUMENTED-MAGIC
[M-LOG-STRUCTURED]: ../universal/#M-LOG-STRUCTURED

<!-- Libs -->
[M-TYPES-SEND]: ../libs/interop/#M-TYPES-SEND
[M-DONT-LEAK-TYPES]: ../libs/interop/#M-DONT-LEAK-TYPES
[M-ESCAPE-HATCHES]: ../libs/interop/#M-ESCAPE-HATCHES
[M-STRONG-TYPES]: ../libs/resilience/#M-STRONG-TYPES
[M-NO-GLOB-REEXPORTS]: ../libs/resilience/#M-NO-GLOB-REEXPORTS
[M-ESSENTIAL-FN-INHERENT]: ../libs/ux/#M-ESSENTIAL-FN-INHERENT
[M-MOCKABLE-SYSCALLS]: ../libs/resilience/#M-MOCKABLE-SYSCALLS
[M-SIMPLE-ABSTRACTIONS]: ../libs/ux/#M-SIMPLE-ABSTRACTIONS
[M-AVOID-WRAPPERS]: ../libs/ux/#M-AVOID-WRAPPERS
[M-DI-HIERARCHY]: ../libs/ux/#M-DI-HIERARCHY
[M-ERRORS-CANONICAL-STRUCTS]: ../libs/ux/#M-ERRORS-CANONICAL-STRUCTS
[M-INIT-BUILDER]: ../libs/ux/#M-INIT-BUILDER
[M-INIT-CASCADED]: ../libs/ux/#M-INIT-CASCADED
[M-SERVICES-CLONE]: ../libs/ux/#M-SERVICES-CLONE
[M-IMPL-ASREF]: ../libs/ux/#M-IMPL-ASREF
[M-IMPL-RANGEBOUNDS]: ../libs/ux/#M-IMPL-RANGEBOUNDS
[M-IMPL-IO]: ../libs/ux/#M-IMPL-IO
[M-TEST-UTIL]: ../libs/resilience/#M-TEST-UTIL
[M-AVOID-STATICS]: ../libs/resilience/#M-AVOID-STATICS
[M-OOBE]: ../libs/building/#M-OOBE
[M-SYS-CRATES]: ../libs/resilience/#M-SYS-CRATES
[M-FEATURES-ADDITIVE]: ../libs/building/#M-FEATURES-ADDITIVE

<!-- Apps -->
[M-APP-ERROR]: ../apps/#M-APP-ERROR
[M-MIMALLOC-APP]: ../apps/#M-MIMALLOC-APP

<!-- FFI -->
[M-ISOLATE-DLL-STATE]: ../ffi/#M-ISOLATE-DLL-STATE

<!-- Safety -->
[M-UNSAFE]: ../safety/#M-UNSAFE
[M-UNSAFE-IMPLIES-UB]: ../safety/#M-UNSAFE-IMPLIES-UB
[M-UNSOUND]: ../safety/#M-UNSOUND

<!-- Performance -->
[M-HOTPATH]: ../performance/#M-HOTPATH
[M-THROUGHPUT]: ../performance/#M-THROUGHPUT
[M-YIELD-POINTS]: ../performance/#M-YIELD-POINTS

<!-- Docs -->
[M-FIRST-DOC-SENTENCE]: ../docs/#M-FIRST-DOC-SENTENCE
[M-MODULE-DOCS]: ../docs/#M-MODULE-DOCS
[M-CANONICAL-DOCS]: ../docs/#M-CANONICAL-DOCS
[M-DOC-INLINE]: ../docs/#M-DOC-INLINE

<!-- AI -->
[M-DESIGN-FOR-AI]: ../ai/#M-DESIGN-FOR-AI
