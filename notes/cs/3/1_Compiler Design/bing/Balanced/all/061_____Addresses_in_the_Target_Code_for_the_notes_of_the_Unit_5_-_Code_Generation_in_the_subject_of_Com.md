# Addresses in the Target Code

- Addresses in the target code are the locations where the values of the variables, constants, temporaries, and labels are stored in the memory or registers of the target machine.
- The code generator is responsible for assigning addresses to the operands and instructions of the target code, and for generating the appropriate load and store instructions to access them.
- There are different types of addresses in the target code, such as absolute addresses, relative addresses, indirect addresses, and register addresses.
- Absolute addresses are the actual memory locations where the operands or instructions are stored. They are usually used for global variables, constants, and labels.
- Relative addresses are the offsets from a base address, such as the beginning of the code segment, the data segment, or the stack segment. They are usually used for local variables, parameters, and temporaries.
- Indirect addresses are the addresses that contain the actual address of the operand or instruction. They are usually used for pointers, arrays, and dynamic memory allocation.
- Register addresses are the names or numbers of the registers where the operands or instructions are stored. They are usually used for optimizing the performance of the target code by reducing the memory access time.
- The code generator can use different strategies for allocating registers to the operands and instructions, such as static allocation, local allocation, global allocation, and graph coloring.
- The code generator can also use different techniques for optimizing the target code, such as peephole optimization, instruction selection, instruction scheduling, and register allocation.