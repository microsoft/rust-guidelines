## Functions expose intermediate results to avoid duplicate work (C-INTERMEDIATE)

Many functions that answer a question also compute interesting related data. If
this data is potentially of interest to the client, consider exposing it in the
API.

### Examples from the standard library

- [`Vec::binary_search`] does not return a `bool` of whether the value was
  found, nor an `Option<usize>` of the index at which the value was maybe found.
  Instead it returns information about the index if found, and also the index at
  which the value would need to be inserted if not found.

- [`String::from_utf8`] may fail if the input bytes are not UTF-8. In the error
  case it returns an intermediate result that exposes the byte offset up to
  which the input was valid UTF-8, as well as handing back ownership of the
  input bytes.

- [`HashMap::insert`] returns an `Option<T>` that returns the preexisting value
  for a given key, if any. For cases where the user wants to recover this value
  having it returned by the insert operation avoids the user having to do a second
  hash table lookup.

[`Vec::binary_search`]: https://doc.rust-lang.org/std/vec/struct.Vec.html#method.binary_search
[`String::from_utf8`]: https://doc.rust-lang.org/std/string/struct.String.html#method.from_utf8
[`HashMap::insert`]: https://doc.rust-lang.org/stable/std/collections/struct.HashMap.html#method.insert
