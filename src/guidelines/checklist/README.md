<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

# Checklist

- **Universal**
  - [ ] Follow the Upstream Guidelines ([M-UPSTREAM-GUIDELINES])
  - [ ] Use Static Verification ([M-STATIC-VERIFICATION])
  - [ ] Lint Overrides Should Use `#[expect]` ([M-LINT-OVERRIDE-EXPECT])
  - [ ] Public Types are Debug ([M-PUBLIC-DEBUG])
  - [ ] Public Types Meant to be Read are Display ([M-PUBLIC-DISPLAY])
  - [ ] If in Doubt, Split the Crate ([M-SMALLER-CRATES])
  - [ ] Names are Free of Weasel Words ([M-CONCISE-NAMES])
  - [ ] Prefer Regular over Associated Functions ([M-REGULAR-FN])
  - [ ] Panic Means 'Stop the Program' ([M-PANIC-IS-STOP])
  - [ ] Detected Programming Bugs are Panics, Not Errors ([M-PANIC-ON-BUG])
  - [ ] All Magic Values and Behaviors are Documented ([M-DOCUMENTED-MAGIC])
- **Library / Interoperability**
  - [ ] Types are Send ([M-TYPES-SEND])
  - [ ] Native Escape Hatches ([M-ESCAPE-HATCHES])
  - [ ] Don't Leak External Types ([M-DONT-LEAK-TYPES])
- **Library / UX**
  - [ ] Abstractions Don't Visibly Nest ([M-SIMPLE-ABSTRACTIONS])
  - [ ] Avoid Smart Pointers and Wrappers in APIs ([M-AVOID-WRAPPERS])
  - [ ] Prefer Types over Generics, Generics over Dyn Traits ([M-DI-HIERARCHY])
  - [ ] Error are Canonical Structs ([M-ERRORS-CANONICAL-STRUCTS])
  - [ ] Complex Type Construction has Builders ([M-INIT-BUILDER])
  - [ ] Complex Type Initialization Hierarchies are Cascaded ([M-INIT-CASCADED])
  - [ ] Services are Clone ([M-SERVICES-CLONE])
  - [ ] Accept `impl AsRef<>` Where Feasible ([M-IMPL-ASREF])
  - [ ] Accept `impl RangeBounds<>` Where Feasible ([M-IMPL-RANGEBOUNDS])
  - [ ] Accept `impl 'IO'` Where Feasible ('Sans IO') ([M-IMPL-IO])
  - [ ] Essential Functionality Should be Inherent ([M-ESSENTIAL-FN-INHERENT])
- **Library / Resilience**
  - [ ] I/O and System Calls Are Mockable ([M-MOCKABLE-SYSCALLS])
  - [ ] Test Utilities are Feature Gated ([M-TEST-UTIL])
  - [ ] Use the Proper Type Family ([M-STRONG-TYPES])
  - [ ] Don't Glob Re-Export Items ([M-NO-GLOB-REEXPORTS])
  - [ ] Avoid Statics ([M-AVOID-STATICS])
- **Library / Building**
  - [ ] Libraries Work Out of the Box ([M-OOBE])
  - [ ] Native `-sys` Crates Compile Without Dependencies ([M-SYS-CRATES])
  - [ ] Features are Additive  ([M-FEATURES-ADDITIVE])
- **Applications**
  - [ ] Use Mimalloc for Apps ([M-MIMALLOC-APP])
  - [ ] Applications may use Anyhow or Derivatives ([M-APP-ERROR])
- **FFI**
  - [ ] Isolate DLL State Between FFI Libraries ([M-ISOLATE-DLL-STATE])
- **Safety**
  - [ ] Unsafe Needs Reason, Should be Avoided ([M-UNSAFE])
  - [ ] Unsafe Implies Undefined Behavior ([M-UNSAFE-IMPLIES-UB])
  - [ ] All Code Must be Sound ([M-UNSOUND])
- **Performance**
  - [ ] Optimize for Throughput, Avoid Empty Cycles ([M-THROUGHPUT])
  - [ ] Identify, Profile, Optimize the Hot Path Early ([M-HOTPATH])
  - [ ] Long-Running Tasks Should Have Yield Points. ([M-YIELD-POINTS])
- **Documentation**
  - [ ] First Sentence is One Line; Approx. 15 Words ([M-FIRST-DOC-SENTENCE])
  - [ ] Has Module Documentation ([M-MODULE-DOCS])
  - [ ] Documentation Has Canonical Sections ([M-CANONICAL-DOCS])
  - [ ] Mark `pub use` Items with `#[doc(inline)]` ([M-DOC-INLINE])

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
