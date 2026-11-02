## Prose contains hyperlinks to relevant things (C-LINK)

Regular links can be added inline with the usual markdown syntax of
`[text](https://rust-lang.github.io/api-guidelines/url)`. Links to other types can be added by marking them with
``[`text`]``, then adding the link target in a new line at the end of
the docstring with ``[`text`]: <target>``, where `<target>` is
described below.

Link targets to methods within the same type usually look like this:

```md
[`serialize_struct`]: #method.serialize_struct
```

Link targets to other types usually look like this:

```md
[`Deserialize`]: trait.Deserialize.html
```

Link targets may also point to a parent or child module:

```md
[`Value`]: ../enum.Value.html
[`DeserializeOwned`]: de/trait.DeserializeOwned.html
```

This guideline is officially recommended by RFC 1574 under the heading ["Link
all the things"].

["Link all the things"]: https://github.com/rust-lang/rfcs/blob/master/text/1574-more-api-documentation-conventions.md#link-all-the-things
