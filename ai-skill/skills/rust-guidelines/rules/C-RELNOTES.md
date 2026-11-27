## Release notes document all significant changes (C-RELNOTES)

Users of the crate can read the release notes to find a summary of what
changed in each published release of the crate. A link to the release notes,
or the notes themselves, should be included in the crate-level documentation
and/or the repository linked in Cargo.toml.

Breaking changes (as defined in [RFC 1105]) should be clearly identified in the
release notes.

If using Git to track the source of a crate, every release published to
*crates.io* should have a corresponding tag identifying the commit that was
published. A similar process should be used for non-Git VCS tools as well.

```bash
# Tag the current commit
GIT_COMMITTER_DATE=$(git log -n1 --pretty=%aD) git tag -a -m "Release 0.3.0" 0.3.0
git push --tags
```

Annotated tags are preferred because some Git commands ignore unannotated tags
if any annotated tags exist.

[RFC 1105]: https://github.com/rust-lang/rfcs/blob/master/text/1105-api-evolution.md

### Examples

- [Serde 1.0.0 release notes](https://github.com/serde-rs/serde/releases/tag/v1.0.0)
- [Serde 0.9.8 release notes](https://github.com/serde-rs/serde/releases/tag/v0.9.8)
- [Serde 0.9.0 release notes](https://github.com/serde-rs/serde/releases/tag/v0.9.0)
- [Diesel change log](https://github.com/diesel-rs/diesel/blob/master/CHANGELOG.md)
