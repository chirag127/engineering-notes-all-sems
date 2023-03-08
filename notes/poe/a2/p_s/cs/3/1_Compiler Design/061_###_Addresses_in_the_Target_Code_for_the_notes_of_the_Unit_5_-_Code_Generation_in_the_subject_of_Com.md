 Here is the content in markdown format for the topic ### Addresses in the Target Code for the notes of the Unit 5 - Code Generation in the subject of Compiler Design:

### Addresses in the Target Code

- Addresses play an important role in the target code generation process. The compiler needs to assign appropriate addresses to the variables, arrays, functions, etc. in the target code.
- There are mainly two types of addressing techniques used:

1. Absolute Addressing: In absolute addressing, the actual/absolute address of the memory location is specified to access the variable/array element. For example, LOAD R1, 1000 (loads the content at address 1000 into register R1). The advantage is that it is simple and fast. The disadvantage is that the program is non-relocatable (if loaded at a different base address, it will not work).

2. Relative Addressing: In relative addressing, the address is specified relative to some base address. For example, LOAD R1, 20(R6) (loads the content at address (base address in R6 + 20) into register R1). The advantage is that the program is relocatable (can be loaded at any base address). The disadvantage is that the addressing is slightly complex.

- Most compilers use relative addressing and determine the base address while loading the target code in memory. This provides flexibility and portability.
- Examples of calculating relative addresses, advantages and disadvantages, applications, etc. can also be included here with diagrams and codes for better understanding.