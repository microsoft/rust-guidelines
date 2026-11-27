## Names use a consistent word order (C-WORD-ORDER)

Here are some error types from the standard library:

- [`JoinPathsError`](https://doc.rust-lang.org/std/env/struct.JoinPathsError.html)
- [`ParseBoolError`](https://doc.rust-lang.org/std/str/struct.ParseBoolError.html)
- [`ParseCharError`](https://doc.rust-lang.org/std/char/struct.ParseCharError.html)
- [`ParseFloatError`](https://doc.rust-lang.org/std/num/struct.ParseFloatError.html)
- [`ParseIntError`](https://doc.rust-lang.org/std/num/struct.ParseIntError.html)
- [`RecvTimeoutError`](https://doc.rust-lang.org/std/sync/mpsc/enum.RecvTimeoutError.html)
- [`StripPrefixError`](https://doc.rust-lang.org/std/path/struct.StripPrefixError.html)

All of these use verb-object-error word order. If we were adding an error to
represent an address failing to parse, for consistency we would want to name it
in verb-object-error order like `ParseAddrError` rather than `AddrParseError`.

The particular choice of word order is not important, but pay attention to
consistency within the crate and consistency with similar functionality in the
standard library.
