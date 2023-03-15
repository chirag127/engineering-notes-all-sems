### Implementation of simple stack allocation scheme for the notes of the Unit 4 - Symbol Tables in the subject of Compiler Design

A stack allocation scheme is a memory management technique used in compilers to allocate and deallocate memory for variables in a program. This scheme is commonly used for managing the memory of local variables in a function.

Here are the steps involved in implementing a simple stack allocation scheme for symbol tables in a compiler:

1. **Initialize the stack pointer**: The stack pointer is a register that points to the top of the stack. It is initialized to the base address of the stack.

2. **Allocate memory for a variable**: When a new local variable is declared in a function, the compiler generates code to allocate memory for the variable on the stack. This is done by decrementing the stack pointer by the size of the variable.

3. **Access the variable**: To access the value of the variable, the compiler generates code to compute the address of the variable by adding the offset of the variable to the base address of the stack.

4. **Deallocate memory for the variable**: When the function returns, the compiler generates code to deallocate the memory for the local variables by resetting the stack pointer to its original value.

This simple stack allocation scheme has several advantages, including fast allocation and deallocation of memory and efficient use of memory. However, it also has some limitations, such as the inability to deallocate memory for individual variables and the requirement that the size of the stack be known at compile time.