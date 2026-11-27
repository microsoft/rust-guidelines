## Destructors that may block have alternatives (C-DTOR-BLOCK)

Similarly, destructors should not invoke blocking operations, which can make
debugging much more difficult. Again, consider providing a separate method for
preparing for an infallible, nonblocking teardown.
