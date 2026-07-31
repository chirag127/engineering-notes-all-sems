### Storage allocation in block structured language

- A block is a program segment that contains data declarations and statements. There can be nested blocks, which means a block can contain other blocks as subprograms or subroutines.
- A block structured language is a language that supports the concept of blocks, such as ALGOL, PL/I, Pascal, C, etc.
- The storage allocation for block structured languages is usually done using a stack, which is a linear data structure that follows the last-in first-out (LIFO) principle.
- The stack is divided into activation records, which are the units of storage that store the information related to a block or a procedure call, such as parameters, local variables, return address, etc.
- The stack pointer (SP) is a register that points to the top of the stack, where the current activation record is located.
- The storage is allocated sequentially in the stack beginning at one end when a block or a procedure is entered. The SP is incremented by the size of the activation record.
- The storage is released when the block or the procedure is exited. The SP is decremented by the size of the activation record.
- If the block or the procedure is invoked recursively, the previously allocated storage is pushed down upon entry, and the latest allocation of storage is popped up when each generation terminates.
- To access the non-local variables of a block or a procedure, a display is used, which is an array of pointers that point to the activation records of the enclosing blocks or procedures.
- The display is updated whenever a block or a procedure is entered or exited, so that the correct activation record can be accessed.
- The storage allocation scheme for block structured languages can be improved by analyzing the call graph of a program, which is a graph that shows the possible calls between procedures.
- By using the call graph, some techniques can be applied to eliminate or reduce the stack allocation and display update operations from many call sequences, such as static links, stack caching, stack allocation elimination, etc .
- These techniques can improve the performance and efficiency of the storage management for block structured languages .