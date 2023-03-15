# General Registers Organization

- General registers organization is a type of CPU organization that uses multiple general-purpose registers instead of a single accumulator register.
- General-purpose registers can store operands, intermediate results, addresses, or any other data that is needed for the execution of instructions.
- General registers organization can have two or three address fields in the instruction format, depending on the number of operands required for each operation.
- General registers organization can be further classified into two types: register-memory reference architecture and register-register reference architecture.

## Register-memory reference architecture

- In this architecture, source 1 is always required in the register, source 2 can be present either in the register or in memory, and the destination can be either in the register or in memory.
- This architecture has the advantage of allowing direct access to memory operands without loading them into registers first, which reduces the number of instructions and memory cycles.
- However, this architecture also has some disadvantages, such as the need for a large instruction word to specify the address modes and the register numbers, and the limited number of registers available for fast data manipulation.

## Register-register reference architecture

- In this architecture, all the operands and the destination are required to be in the registers, and memory access is only allowed through load and store instructions.
- This architecture has the advantage of having a smaller instruction word, which reduces the instruction fetch time and the memory bandwidth requirement.
- Moreover, this architecture allows more registers to be used for data processing, which increases the performance and the flexibility of the instruction set.
- However, this architecture also has some disadvantages, such as the need for more instructions and memory cycles to load and store operands from and to memory, and the increased complexity of the register file and the register addressing logic.

: https://www.geeksforgeeks.org/introduction-of-general-register-based-cpu-organization/
: https://www.geeksforgeeks.org/different-classes-of-cpu-registers/