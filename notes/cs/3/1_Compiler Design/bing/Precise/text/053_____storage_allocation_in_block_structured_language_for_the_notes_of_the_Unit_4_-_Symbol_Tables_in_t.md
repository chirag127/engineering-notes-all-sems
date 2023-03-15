### Storage Allocation in Block Structured Language

In block-structured languages, the storage allocation for variables is done in a hierarchical manner. This means that the variables declared within a block are allocated storage only for the duration of that block. When the block is exited, the storage for those variables is deallocated.

Here are some key points to remember about storage allocation in block-structured languages:

1. **Static allocation**: In this method, the storage for variables is allocated at compile-time. This means that the amount of storage required for the variables is determined before the program is executed. This method is used for global variables and for variables declared in the outermost block of the program.

2. **Stack allocation**: In this method, the storage for variables is allocated at runtime on the stack. This means that the storage is allocated when the block is entered and deallocated when the block is exited. This method is used for local variables declared within a block.

3. **Heap allocation**: In this method, the storage for variables is allocated at runtime on the heap. This means that the storage is allocated dynamically when it is needed and deallocated when it is no longer needed. This method is used for dynamically allocated variables, such as those created using the `new` keyword in C++ or the `malloc` function in C.

In summary, storage allocation in block-structured languages is done in a hierarchical manner, with different methods used for different types of variables. Understanding these methods is important for understanding how programs written in block-structured languages work.