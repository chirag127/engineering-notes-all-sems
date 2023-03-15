### Addresses in the Target Code

- Addresses in the target code are the locations where the values of variables, constants, temporaries, and parameters are stored in the memory or registers of the target machine.
- Addresses in the target code can be classified into four types: absolute, relative, indirect, and immediate.
- Absolute addresses are fixed locations in the memory, such as global variables or static data. They are usually represented by a label or a number.
- Relative addresses are offsets from a base address, such as local variables or parameters in a stack frame. They are usually represented by a register name and a displacement, such as R1+8 or SP-4.
- Indirect addresses are pointers to other locations in the memory, such as dynamic data or arrays. They are usually represented by a register name or a memory location that contains the address, such as R2 or M[R3].
- Immediate addresses are constants or literals that are embedded in the instruction, such as 5 or 'a'. They are usually represented by a hash sign and a value, such as #5 or #'a'.
- The code generator is responsible for assigning addresses in the target code for the operands of the intermediate code, such as three-address code .
- The code generator can use different strategies for allocating registers and memory locations for the operands, such as static allocation, local allocation, global allocation, and graph coloring.
- The code generator can also perform optimizations on the target code, such as peephole optimization, instruction selection, instruction scheduling, and register allocation.
- The code generator can use different techniques for generating target code for different types of statements, such as assignments, arithmetic operations, conditional jumps, loops, function calls, and returns .