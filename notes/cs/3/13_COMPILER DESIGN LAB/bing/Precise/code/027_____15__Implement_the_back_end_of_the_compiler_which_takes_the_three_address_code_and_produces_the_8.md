### 15. Implement the back end of the compiler which takes the three address code and produces the 8086 assembly language

The back end of a compiler is responsible for generating the target code from the intermediate representation, in this case, the three address code. The target code for this specific implementation is the 8086 assembly language.

Here are the steps to implement the back end of the compiler:

1. **Instruction selection**: Map the three address code instructions to the corresponding 8086 assembly language instructions. This can be done using a table-driven approach or a tree-rewriting approach.

2. **Register allocation**: Assign registers to the variables used in the three address code. This can be done using graph coloring or linear scan algorithms.

3. **Code generation**: Generate the final 8086 assembly language code by replacing the variables in the instructions with the assigned registers.

It is important to note that the 8086 assembly language has its own set of instructions and addressing modes, which must be taken into account when implementing the back end of the compiler. Additionally, optimization techniques can be applied to improve the efficiency of the generated code.