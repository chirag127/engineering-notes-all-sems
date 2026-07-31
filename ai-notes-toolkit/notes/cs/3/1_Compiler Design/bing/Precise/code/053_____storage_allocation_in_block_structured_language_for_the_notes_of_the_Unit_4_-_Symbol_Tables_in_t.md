### Storage Allocation in Block Structured Language

In block structured languages, the storage allocation for variables is done in a hierarchical manner. This means that the variables declared in an inner block have a local scope and are not accessible outside the block. On the other hand, variables declared in an outer block have a global scope and can be accessed from any inner block.

Here are some key points to remember about storage allocation in block structured languages:

1. The storage for local variables is allocated on the runtime stack when the block is entered and deallocated when the block is exited.
2. The storage for global variables is allocated in the static data area and remains allocated for the entire duration of the program.
3. The storage for variables declared in an inner block may overlap with the storage for variables declared in an outer block, as long as the inner block is not active.
4. The storage for variables declared in an inner block may also overlap with the storage for variables declared in a sibling block, as long as the two blocks are not active at the same time.

This hierarchical storage allocation scheme allows for efficient use of memory and also enables the implementation of recursive functions, where the same function can be called multiple times with different local variables.
