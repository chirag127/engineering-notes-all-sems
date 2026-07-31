# Target Language for the notes of the Unit 5 - Code Generation in the subject of Compiler Design

- The target language is the language that the compiler produces as output. It is usually a low-level language, such as assembly or machine code, that can be executed by the target machine or platform.
- The code generation phase of the compiler is responsible for translating the optimized intermediate representation (IR) into the target language. The code generator must ensure that the semantics of the source program are preserved in the target code.
- The main tasks of the code generator are:
  - Register allocation: assigning variables and temporary values to registers or memory locations in the target machine.
  - Instruction selection: choosing the appropriate instructions and operands to implement the operations and data transfers in the IR.
  - Instruction scheduling: ordering the instructions to maximize the performance and minimize the latency of the target machine.
- The code generator may also perform some target-specific optimizations, such as peephole optimization, instruction combining, or loop unrolling, to improve the quality of the target code.
- The code generator may use different strategies and algorithms to perform the tasks mentioned above, depending on the characteristics of the target machine and the IR. Some of the popular strategies are:
  - Graph coloring: a technique for register allocation that models the interference among variables as a graph and tries to assign different colors (registers) to adjacent nodes (variables).
  - Tiling: a technique for instruction selection that covers the IR with tiles (patterns) that correspond to target instructions and minimizes the cost of the tiling.
  - List scheduling: a technique for instruction scheduling that orders the instructions based on their dependencies and priorities and tries to fill the instruction slots in the target machine.