### Addresses in the Target Code

In the process of code generation, the compiler must generate code to access the memory locations where the data objects are stored. These memory locations are referred to as addresses in the target code.

1. **Absolute Addresses:** An absolute address is a fixed address in memory. The compiler can generate code to access an absolute address directly, without the need for any additional calculations.

2. **Relative Addresses:** A relative address is an offset from a base address. The base address is typically the address of a data segment or the address of the stack. The compiler generates code to calculate the absolute address by adding the relative address to the base address.

3. **Register Addresses:** A register address refers to a location in a register. The compiler generates code to access the data stored in the register directly, without the need for any memory access.

4. **Indirect Addresses:** An indirect address is an address that is stored in a memory location or a register. The compiler generates code to first access the memory location or register to retrieve the address, and then access the data stored at that address.

These are the different types of addresses that can be used in the target code during the code generation phase of the compilation process. Each type of address has its own advantages and disadvantages, and the compiler must choose the most appropriate type of address for each data object based on the requirements of the target machine and the characteristics of the program being compiled.