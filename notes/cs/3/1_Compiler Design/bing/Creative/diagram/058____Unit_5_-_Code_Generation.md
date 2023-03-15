## Unit 5 - Code Generation

- Code generation is the process of translating an intermediate representation of a source program into a target program that can be executed by a machine.
- Code generation can be divided into two phases: instruction selection and instruction scheduling.
- Instruction selection is the process of choosing the appropriate instructions from the target instruction set to implement the operations in the intermediate representation.
- Instruction scheduling is the process of ordering the instructions to optimize the performance of the target program, taking into account the dependencies, latencies, and resource constraints of the target machine.
- Code generation can be performed using different techniques, such as template-based, peephole, and graph-based methods.
- Template-based code generation uses predefined patterns or templates to match the intermediate representation with the target instructions.
- Peephole code generation applies local optimizations to a stream of target instructions by examining a small window or peephole of instructions at a time.
- Graph-based code generation uses data structures such as trees or graphs to represent the intermediate representation and the target instructions, and applies graph transformations or pattern matching to generate the target code.