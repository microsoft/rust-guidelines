---
name: rust-guidelines
description: Always load when working on a Rust project.
---

# Rust guidelines

Scan the [index](#index) before Rust work. Automatically load applicable
`rules/<ID>.md` files, relative to this skill, as the task changes.

After loading a guideline, print `🦀 <ID> - <what in this task prompted the load>`.
Name the concrete change, code or request; do not repeat the index's generic trigger.
Report missing files; do not guess or refresh.

## Index

Format: `ID - trigger`

C-ANYWHERE - when defining or testing macros that expand to items in different scopes
C-BITFLAG - when an API accepts combinations of independent flags
C-BUILDER - when constructing values with many inputs, optional settings, or side effects
C-CALLER-CONTROL - when choosing owned or borrowed parameters, internal clones, or Copy bounds
C-CASE - when naming Rust items, variables, type parameters, lifetimes, or Cargo features
C-COLLECT - when adding collection types that can be built or extended from iterators
C-COMMON-TRAITS - when defining types and choosing their standard trait implementations
C-CONV - when naming conversions between representations or extracting wrapped values
C-CONV-SPECIFIC - when choosing which type owns a conversion method or constructor
C-CONV-TRAITS - when adding owned, borrowed, mutable, or fallible conversions between types
C-CRATE-DOC - when creating or revising a crate's top-level documentation
C-CTOR - when adding constructors, conversion constructors, or Default implementations
C-CUSTOM-TYPE - when API arguments use primitives or Option with ambiguous domain meanings
C-DEBUG - when adding or changing publicly exposed types
C-DEBUG-NONEMPTY - when implementing Debug, including for empty values
C-DEREF - when considering Deref or DerefMut for a wrapper or smart pointer
C-DTOR-BLOCK - when resource cleanup or Drop may perform blocking operations
C-DTOR-FAIL - when resource cleanup or Drop can fail or panic
C-EVOCATIVE - when designing macro input syntax for generated Rust constructs
C-EXAMPLE - when adding public items or revising their rustdoc usage examples
C-FAILURE - when functions or trait methods can fail, panic, or require safety invariants
C-FEATURE - when naming Cargo features, including optional dependencies and std support
C-GENERIC - when choosing concrete inputs, generic parameters, or trait bounds for functions
C-GETTER - when adding getters, mutable accessors, or checked and unchecked element access
C-GOOD-ERR - when designing errors returned by public APIs, including error trait objects
C-HIDDEN - when internal types, helpers, or trait impls appear in public rustdoc
C-INTERMEDIATE - when an operation computes related results that callers might otherwise recompute
C-ITER - when adding iteration methods to homogeneous collections
C-ITER-TY - when naming iterator types returned by methods or functions
C-LINK - when documentation mentions related types, methods, modules, or external resources
C-MACRO-ATTR - when item-generating macros need per-item attributes, cfg, or derives
C-MACRO-TY - when macros accept type fragments or emit them in a different scope
C-MACRO-VIS - when macros generate items whose visibility callers may need to control
C-METADATA - when creating or preparing a crate's Cargo.toml package metadata
C-METHOD - when placing an operation clearly associated with a particular receiver type
C-NEWTYPE - when the same underlying type represents distinct units or domain concepts
C-NEWTYPE-HIDE - when API return types expose implementation details or complex iterator composition
C-NO-OUT - when returning multiple values or considering mutable output parameters
C-NUM-FMT - when defining numeric or bitflag types used in bitwise operations
C-OBJECT - when designing traits that may be used through dyn Trait
C-OVERLOAD - when implementing operator traits such as Add, Mul, or BitOr
C-PERMISSIVE - when choosing crate licenses or dependencies for ecosystem distribution
C-QUESTION-MARK - when writing documentation examples that perform fallible operations
C-RELNOTES - when publishing crate versions or documenting significant and breaking changes
C-RW-VALUE - when designing or documenting functions accepting generic Read or Write inputs
C-SEALED - when public traits should only have implementations inside their defining crate
C-SEND-SYNC - when type changes, raw pointers, or tests affect Send and Sync guarantees
C-SERDE - when defining data structures callers may store, serialize, or exchange
C-SMART-PTR - when adding operations to smart pointers that also expose pointee methods
C-STABLE - when stabilizing a crate or exposing dependency types through public APIs or impls
C-STRUCT-BOUNDS - when adding generic data structures, derived traits, or type-level bounds
C-STRUCT-PRIVATE - when choosing field visibility for structs exposed to callers
C-VALIDATE - when API inputs have validity constraints or checked and unchecked entry points
C-WORD-ORDER - when naming related items, especially families of error types
M-APP-ERROR - when choosing error handling for applications and their app-only internal crates
M-ASYNC-FN - when choosing async fn versus an explicit Future-returning signature
M-ASYNC-STACK-SIZE - when async functions are called frequently or retain large data across await points
M-AVOID-INDIRECTION - when hot data structures use nested heap pointers or shared ownership
M-AVOID-STATICS - when library correctness depends on static or thread-local state
M-AVOID-WRAPPERS - when public APIs accept or return smart pointers or generic wrappers
M-BALANCED-MODULES - when organizing a library's crate root, public items, and submodules
M-BOX-DST - when storing many internal immutable owned strings or sequences
M-BUILD-RESULT - when builder settings need validation or can fail in combination
M-CANONICAL-DOCS - when documenting public library items and their error or safety contracts
M-CARGO-WORKSPACE - when configuring shared metadata, lints, dependencies, or features across crates
M-COLLECTION-TRAITS - when exposing custom collections and their iterators to downstream users
M-CRATES-FLAT-FOLDER - when adding crates or reorganizing a repository's workspace directories
M-CRATES-IN-WORKSPACE - when adding workspace members or dependencies between sibling crates
M-DESIGN-FOR-AI - when designing APIs, examples, or testability for human and agent consumers
M-DI-HIERARCHY - when injecting async dependencies or choosing concrete, generic, or dynamic services
M-DOC-INLINE - when re-exporting items and deciding how they appear in rustdoc
M-DOCUMENTED-MAGIC - when introducing or changing hardcoded production values or constants
M-DONT-LEAK-TYPES - when public library APIs expose types from dependency crates
M-ERRORS-CANONICAL-STRUCTS - when defining reusable library errors, their context, causes, or backtraces
M-ESCAPE-HATCHES - when wrapping native handles that callers may need to import or pass over FFI
M-ESSENTIAL-FN-INHERENT - when exposing a type's core functionality through inherent methods or traits
M-EXAMPLE-OVER-PROC - when choosing declarative versus procedural macros for code generation
M-FAST-HASHER - when hashing trusted internal keys or choosing hash collection implementations
M-FEATURES-ADDITIVE - when adding library features or changing feature-gated APIs and dependencies
M-FFI-NAMING - when naming crates that import native APIs or export Rust APIs over FFI
M-FFI-TRANSLATES - when exposing Rust business logic through C-compatible FFI entry points
M-FIRST-DOC-SENTENCE - when writing rustdoc summaries shown in module item listings
M-FOREIGN-REEXPORTS - when considering re-exports of items defined in other crates
M-FROM-ERROR - when converting upstream errors into owned error types or repeating map_err calls
M-HOTPATH - when developing or changing code with performance or operating-cost impact
M-IMPL-ASREF - when accepting strings, paths, or byte sequences and choosing reference bounds
M-IMPL-IO - when APIs parse, emit, or initialize data through synchronous or asynchronous I/O
M-IMPL-RANGEBOUNDS - when function parameters represent numeric ranges or bounds
M-INIT-BUILDER - when construction has many optional settings, required dependencies, or runtime variants
M-INIT-CASCADED - when constructors require four or more parameters or nested initialization
M-INITIAL-CAPACITY - when building collections with known or estimable sizes, including via iterators
M-INTEGRATION-TESTS - when adding tests that can exercise behavior through public APIs
M-ISOLATE-DLL-STATE - when exchanging data or services between separately compiled Rust dynamic libraries
M-LATEST-EDITION - when creating a Rust crate or workspace and choosing its edition
M-LINT-OVERRIDE-EXPECT - when suppressing project lints on items, modules, macros, or generated code
M-LOG-NOT-PRINT - when adding production diagnostics or distinguishing them from intentional CLI output
M-LOG-OVERHEAD - when libraries emit logs or metrics on hot paths or under sustained load
M-LOG-STRUCTURED - when adding log events, their names and properties, or potentially sensitive values
M-MACRO-HELPERS - when macro expansions refer to types or traits from third-party dependencies
M-MACRO-LAST-RESORT - when considering a macro to replace repeated or complex ordinary Rust code
M-MACRO-MAIN-CRATE - when procedural macros generate crate paths or are re-exported through a facade
M-MACRO-VERSION-PIN - when wiring or publishing companion proc-macro crates and their main library
M-MACROS-DONT-LIE - when macros transform item kinds, function signatures, or async behavior
M-MEM-REUSE - when repeated operations allocate buffers or APIs could let callers reuse resources
M-MIMALLOC-APPS - when creating applications or choosing their global memory allocator
M-MOCKABLE-SYSCALLS - when user-facing types access I/O, clocks, randomness, hardware, or external state
M-MODULE-DOCS - when adding public library modules or changing subsystem behavior and guarantees
M-MSRV - when creating libraries or adopting language features that raise compiler requirements
M-NO-GLOB-REEXPORTS - when re-exporting items from modules, dependencies, or platform-specific backends
M-NO-META-DESIGN-DOCUMENTATION - when writing crate or module docs after design work or refactoring
M-NO-PRELUDE - when designing convenience imports or a prelude namespace for a crate
M-OOBE - when adding library build steps, dependencies, code generation, or platform requirements
M-PANIC-CONTINUATION - when catching panics or designing request isolation and recovery
M-PANIC-IS-STOP - when deciding to panic, unwrap, or propagate a runtime failure
M-PANIC-MESSAGE - when adding explicit panics, assertions, or unreachable and unfinished-code markers
M-PANIC-ON-BUG - when distinguishing detected contract violations from expected input failures
M-PARAMETER-CONSISTENCY - when related functions share parameters or accept closures and common dependencies
M-PROC-IMPL - when implementing, organizing, or testing procedural macros
M-PROC-IMPLIED-ITEMS - when procedural macros introduce additional types or items into caller scopes
M-PUBLIC-DEBUG - when exposing types or implementing Debug, especially for sensitive data
M-PUBLIC-DISPLAY - when public types, errors, or string wrappers need human-readable formatting
M-REGULAR-FN - when placing helper computations without a clear receiver or constructor role
M-RUST-SHAPED - when porting code or architecture from object-oriented or other language ecosystems
M-SERVICES-CLONE - when service types or per-thread resources must be shared by multiple consumers
M-SHORT-NAMES - when naming items whose context may already be conveyed by a module or crate
M-SHRINK-TO-FIT - when storing large long-lived collections built without exact capacity reservations
M-SIMPLE-ABSTRACTIONS - when public types expose nested generics, complex bounds, or service abstractions
M-SINGLE-ITEM-PATH - when moving public items or constructing their re-export paths within a crate
M-SMALLER-CRATES - when modules could be consumed independently or crate boundaries affect build times
M-STATIC-VERIFICATION - when configuring Rust project checks, lint sets, or CI quality gates
M-STRONG-TYPES - when choosing standard types for domain data, especially OS paths and numeric APIs
M-STRONG-TYPES-GUARD - when constructing or converting newtypes whose valid values are restricted
M-SYS-CRATES - when building and packaging native library bindings in a sys crate
M-TARGET-CPU - when configuring server application builds for known deployment hardware
M-TAUTOLOGICAL-TESTS - when designing test assertions or tests to satisfy mutation coverage
M-TEST-UTIL - when exposing mocks, fake data, sensitive inspection, or test-only safety overrides
M-THROUGHPUT - when designing library work batching, shared state, task scheduling, or throughput
M-TYPES-SEND - when exposing library types or futures and changing data held across await points
M-UNSAFE - when introducing or modifying unsafe code, FFI calls, or unchecked operations
M-UNSAFE-IMPLIES-UB - when deciding whether a function or trait should be marked unsafe
M-UNSOUND - when safe interfaces rely on unsafe internals, module invariants, or manual Send/Sync
M-UPSTREAM-GUIDELINES - when reviewing Rust API conventions, style, design patterns, or safety guarantees
M-WEASEL-WORDS - when naming types or traits, or designing factories and repeated instantiation
M-YIELD-POINTS - when async tasks perform long CPU-bound work or process large batches
