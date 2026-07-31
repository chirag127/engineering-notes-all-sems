# Code Generator for the notes of the Unit 5 - Code Generation in the subject of Compiler Design

- Code generation is the final phase of compilation that converts the intermediate representation of source code into a form that can be readily executed by the target system .
- The code generator is responsible for mapping the intermediate code to the target code, which may be machine code or assembly code.
- The code generator generally performs three tasks:
  - Instruction selection: choosing the appropriate instructions from the target instruction set to implement the intermediate code operations.
  - Register allocation: assigning the intermediate code operands to the available registers of the target machine.
  - Instruction scheduling: ordering the instructions to improve the performance and utilization of the target machine resources.
- The code generator may also perform some optimizations on the target code, such as peephole optimization, instruction combining, and loop unrolling .
- The code generator may use different strategies for register allocation and optimization, such as:
  - Local register allocation: allocating registers within a basic block, which is a sequence of instructions with no branches or labels.
  - Global register allocation: allocating registers across basic blocks, which may require graph coloring or linear scan algorithms.
  - Register optimization: reducing the number of register spills and reloads, which are memory accesses to store or load registers.