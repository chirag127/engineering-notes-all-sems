### Storage allocation in block structured language

- A block is a program segment that contains data declarations and statements. There can be nested blocks. A block structured language is a language that allows the definition of blocks, such as Pascal, C, and Java.
- Storage allocation in block structured language is the process of assigning memory locations to the variables declared in a block. The storage allocation scheme affects the efficiency and correctness of the program execution.
- The most common storage allocation scheme for block structured language is the **stack allocation** scheme. In this scheme, the storage is allocated sequentially in the stack beginning at one end. Storage should be freed in the reverse order of allocation so that a block of storage being released is always at the top of the stack.
- The stack allocation scheme has the following advantages and disadvantages:
  - Advantages:
    - It is simple and efficient to implement.
    - It supports recursion and dynamic scoping.
    - It allows the reuse of storage for different blocks.
  - Disadvantages:
    - It requires the allocation and deallocation of storage for each block entry and exit, which may incur overhead.
    - It limits the lifetime of variables to the block scope, which may prevent some optimizations.
- The stack allocation scheme requires the use of a **display** or an **access link** to access the variables in the outer blocks. A display is an array of pointers to the activation records of the currently active blocks. An access link is a pointer to the activation record of the lexically enclosing block. The display or the access link is updated on each block entry and exit.
- Some techniques have been proposed to improve the storage allocation scheme for block structured language by reducing the overhead of stack allocation and display or access link update. These techniques are based on analyzing the call graph of the program and identifying the blocks that can be allocated statically or in registers, or the blocks that can share the same display or access link. Some examples of these techniques are :
  - Static allocation: This technique allocates storage for a block at compile time if the block is not recursive and has a fixed size. This eliminates the need for stack allocation and display or access link update for the block.
  - Register allocation: This technique allocates storage for a block in registers if the block is not recursive and has a small size. This reduces the stack allocation and display or access link update overhead for the block.
  - Display caching: This technique caches the display or the access link for a block in a register if the block is frequently called. This avoids the display or access link update for the block.
  - Display sharing: This technique shares the same display or access link for a set of blocks that have the same lexical nesting level and are mutually exclusive in execution. This reduces the number of displays or access links needed for the program.