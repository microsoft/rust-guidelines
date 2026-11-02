## Destructors never fail (C-DTOR-FAIL)

Destructors are executed while panicking, and in that context a failing
destructor causes the program to abort.

Instead of failing in a destructor, provide a separate method for checking for
clean teardown, e.g. a `close` method, that returns a `Result` to signal
problems. If that `close` method is not called, the `Drop` implementation
should do the teardown and ignore or log/trace any errors it produces.
