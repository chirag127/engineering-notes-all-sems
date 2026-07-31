# The Target Language for the notes of the Unit 5 - Code Generation in the subject of Compiler Design

- Code generation is the process of converting the intermediate representation of the source code into a form that can be executed by the target system.
- The target language is the lower-level programming language that the compiler produces as the output, such as assembly language or machine code.
- The target language should be compatible with the target system's architecture, instruction set, memory model, and calling conventions.
- The target language should also be efficient and optimized to reduce the execution time and space of the compiled program.
- The code generator is the component of the compiler that performs the code generation task. It typically performs three subtasks:
  - Instruction selection: choosing the appropriate instructions from the target language to implement the operations in the intermediate code.
  - Register allocation: assigning the variables and temporary values to the available registers in the target system.
  - Instruction scheduling: ordering the instructions to exploit the parallelism and pipelining features of the target system.
- The code generator may also perform some peephole optimizations, such as eliminating redundant instructions, replacing expensive instructions with cheaper ones, and rearranging instructions to avoid stalls.
- The code generator may use different techniques and data structures to perform the code generation task, such as templates, patterns, graphs, trees, and DAGs .
- The code generator may also interact with the symbol table and the intermediate code generator to resolve the names and types of the variables and functions in the source code.