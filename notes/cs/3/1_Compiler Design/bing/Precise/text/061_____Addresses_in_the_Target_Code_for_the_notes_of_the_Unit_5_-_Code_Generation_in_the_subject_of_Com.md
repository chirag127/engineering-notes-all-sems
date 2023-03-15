### Addresses in the Target Code

In the process of code generation, the compiler must generate code to access the memory locations where the data objects are stored. These memory locations are referred to as addresses in the target code.

1. **Absolute Addresses:** An absolute address is a fixed address in memory. It is specified as a constant value in the target code. This type of address is used for global data objects and static data objects.

2. **Base-Displacement Addresses:** A base-displacement address is specified as the sum of a base address and a displacement. The base address is typically the address of a register that contains the address of the base of an array or a record. The displacement is an offset from the base address.

3. **Register Addresses:** A register address refers to a location in a register. This type of address is used for temporary data objects that are stored in registers.

4. **Indexed Addresses:** An indexed address is specified as the sum of a base address and an index. The base address is typically the address of a register that contains the address of the base of an array. The index is the value of an index register that is multiplied by the size of the array element.

5. **Indirect Addresses:** An indirect address is specified as the contents of a memory location or a register. This type of address is used for pointers and for passing parameters by reference.

6. **Stack Addresses:** A stack address refers to a location on the runtime stack. This type of address is used for local data objects and for passing parameters by value.

These are the different types of addresses that can be used in the target code during the code generation phase of the compilation process. Each type of address has its own advantages and disadvantages, and the choice of address type depends on the specific requirements of the target machine and the program being compiled.