## Builders enable construction of complex values (C-BUILDER)

Some data structures are complicated to construct, due to their construction
needing:

* a large number of inputs
* compound data (e.g. slices)
* optional configuration data
* choice between several flavors

which can easily lead to a large number of distinct constructors with many
arguments each.

If `T` is such a data structure, consider introducing a `T` _builder_:

1. Introduce a separate data type `TBuilder` for incrementally configuring a `T`
   value. When possible, choose a better name: e.g. [`Command`] is the builder
   for a [child process], [`Url`] can be created from a [`ParseOptions`].
2. The builder constructor should take as parameters only the data _required_ to
   make a `T`.
3. The builder should offer a suite of convenient methods for configuration,
   including setting up compound inputs (like slices) incrementally. These
   methods should return `self` to allow chaining.
4. The builder should provide one or more "_terminal_" methods for actually
   building a `T`.

[`Command`]: https://doc.rust-lang.org/std/process/struct.Command.html
[child process]: https://doc.rust-lang.org/std/process/struct.Child.html
[`Url`]: https://docs.rs/url/1.4.0/url/struct.Url.html
[`ParseOptions`]: https://docs.rs/url/1.4.0/url/struct.ParseOptions.html

The builder pattern is especially appropriate when building a `T` involves side
effects, such as spawning a task or launching a process.

In Rust, there are two variants of the builder pattern, differing in the
treatment of ownership, as described below.

### Non-consuming builders (preferred)

In some cases, constructing the final `T` does not require the builder itself to
be consumed. The following variant on [`std::process::Command`] is one example:

[`std::process::Command`]: https://doc.rust-lang.org/std/process/struct.Command.html

```
// NOTE: the actual Command API does not use owned Strings;
// this is a simplified version.

pub struct Command {
    program: String,
    args: Vec<String>,
    cwd: Option<String>,
    // etc
}

impl Command {
    pub fn new(program: String) -> Command {
        Command {
            program: program,
            args: Vec::new(),
            cwd: None,
        }
    }

    /// Add an argument to pass to the program.
    pub fn arg(&mut self, arg: String) -> &mut Command {
        self.args.push(arg);
        self
    }

    /// Add multiple arguments to pass to the program.
    pub fn args(&mut self, args: &[String]) -> &mut Command {
        self.args.extend_from_slice(args);
        self
    }

    /// Set the working directory for the child process.
    pub fn current_dir(&mut self, dir: String) -> &mut Command {
        self.cwd = Some(dir);
        self
    }

    /// Executes the command as a child process, which is returned.
    pub fn spawn(&self) -> io::Result<Child> {
        /* ... */
    }
}
```

Note that the `spawn` method, which actually uses the builder configuration to
spawn a process, takes the builder by shared reference. This is possible because
spawning the process does not require ownership of the configuration data.

Because the terminal `spawn` method only needs a reference, the configuration
methods take and return a mutable borrow of `self`.

#### The benefit

By using borrows throughout, `Command` can be used conveniently for both
one-liner and more complex constructions:

```
// One-liners
Command::new("/bin/cat").arg("file.txt").spawn();

// Complex configuration
let mut cmd = Command::new("/bin/ls");
if size_sorted {
    cmd.arg("-S");
}
cmd.arg(".");
cmd.spawn();
```

### Consuming builders

Sometimes builders must transfer ownership when constructing the final type `T`,
meaning that the terminal methods must take `self` rather than `&self`.

```
impl TaskBuilder {
    /// Name the task-to-be.
    pub fn named(mut self, name: String) -> TaskBuilder {
        self.name = Some(name);
        self
    }

    /// Redirect task-local stdout.
    pub fn stdout(mut self, stdout: Box<io::Write + Send>) -> TaskBuilder {
        self.stdout = Some(stdout);
        self
    }

    /// Creates and executes a new child task.
    pub fn spawn<F>(self, f: F) where F: FnOnce() + Send {
        /* ... */
    }
}
```

Here, the `stdout` configuration involves passing ownership of an `io::Write`,
which must be transferred to the task upon construction (in `spawn`).

When the terminal methods of the builder require ownership, there is a basic
tradeoff:

* If the other builder methods take/return a mutable borrow, the complex
  configuration case will work well, but one-liner configuration becomes
  impossible.

* If the other builder methods take/return an owned `self`, one-liners continue
  to work well but complex configuration is less convenient.

Under the rubric of making easy things easy and hard things possible, all
builder methods for a consuming builder should take and return an owned
`self`. Then client code works as follows:

```
// One-liners
TaskBuilder::new("my_task").spawn(|| { /* ... */ });

// Complex configuration
let mut task = TaskBuilder::new();
task = task.named("my_task_2"); // must re-assign to retain ownership
if reroute {
    task = task.stdout(mywriter);
}
task.spawn(|| { /* ... */ });
```

One-liners work as before, because ownership is threaded through each of the
builder methods until being consumed by `spawn`. Complex configuration, however,
is more verbose: it requires re-assigning the builder at each step.
