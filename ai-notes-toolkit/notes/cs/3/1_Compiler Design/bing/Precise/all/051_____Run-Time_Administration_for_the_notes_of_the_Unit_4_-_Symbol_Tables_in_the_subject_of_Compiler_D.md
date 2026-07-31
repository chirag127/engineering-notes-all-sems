### Run-Time Administration

Run-time administration is a crucial aspect of the compilation process. It involves managing the resources of the target machine during the execution of the compiled code. This includes the allocation and deallocation of memory, the management of the runtime stack, and the handling of input and output operations.

1. **Memory allocation and deallocation**: During the execution of the compiled code, memory must be allocated for variables and data structures. This memory must also be deallocated when it is no longer needed. The compiler must generate code to manage this process.

2. **Runtime stack management**: The runtime stack is used to store information about the current state of the program, including the values of local variables and the return addresses of function calls. The compiler must generate code to manage the runtime stack, including pushing and popping values as needed.

3. **Input and output operations**: The compiler must generate code to handle input and output operations, such as reading from the keyboard or writing to the screen. This may involve interfacing with the operating system or other system libraries.

Run-time administration is closely related to the symbol table, as the symbol table is used to keep track of information about variables and data structures that are needed during the execution of the compiled code. The symbol table is used to determine the memory addresses of variables and data structures, and to generate the appropriate code for accessing them.