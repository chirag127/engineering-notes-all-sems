## Unit 5 - Code Generation

- Code generation is the process of translating an intermediate representation of a source program into a target program that can be executed by a machine.
- Code generation can be divided into two phases: instruction selection and instruction scheduling.
- Instruction selection is the task of choosing the appropriate instructions from the target instruction set to implement the operations in the intermediate representation.
- Instruction scheduling is the task of ordering the instructions to optimize the performance of the target program, taking into account the dependencies, latencies, and resource constraints of the target machine.
- Code generation can be performed by different methods, such as template-based, peephole, and graph-based methods.
- Template-based methods use predefined patterns of instructions to match the operations in the intermediate representation and generate the corresponding target code.
- Peephole methods apply local optimizations to the generated code by examining a small window of instructions and replacing them with more efficient ones.
- Graph-based methods use data structures such as trees or graphs to represent the intermediate representation and the target instruction set, and apply algorithms such as pattern matching, tree covering, or graph coloring to generate the optimal code.