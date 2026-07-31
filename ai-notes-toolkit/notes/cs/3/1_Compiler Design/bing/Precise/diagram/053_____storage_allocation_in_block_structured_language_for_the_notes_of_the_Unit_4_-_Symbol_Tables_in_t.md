### Storage Allocation in Block Structured Language

In block structured languages, the storage allocation for variables is done in a hierarchical manner. This means that the variables declared in an inner block have a local scope and are not accessible outside of that block. On the other hand, variables declared in an outer block have a global scope and can be accessed from any inner block.

Here are some key points to remember about storage allocation in block structured languages:

1. **Static allocation**: In this method, the memory for variables is allocated at compile time. This means that the memory is reserved for the entire duration of the program execution. This method is used for global variables and for variables declared in the outermost block.

2. **Stack allocation**: In this method, the memory for variables is allocated at runtime on the stack. This means that the memory is reserved only for the duration of the block execution. This method is used for local variables and for variables declared in inner blocks.

3. **Heap allocation**: In this method, the memory for variables is allocated at runtime on the heap. This means that the memory is reserved until it is explicitly deallocated by the programmer. This method is used for dynamic memory allocation.

In summary, storage allocation in block structured languages is done in a hierarchical manner, with different methods used for global, local, and dynamic variables. This allows for efficient memory management and helps to prevent errors such as variable name conflicts.