### Code optimization for the notes of the Unit 5 - Code Generation in the subject of Compiler Design

- Code optimization is the process of improving the quality and efficiency of the generated code by applying various techniques at different stages of the compiler.
- Code optimization can be classified into two categories: machine-independent and machine-dependent.
- Machine-independent optimization is applied to the intermediate code and does not depend on the target architecture or instruction set.
- Machine-dependent optimization is applied to the object code and exploits the features and constraints of the target machine.
- Some of the common machine-independent optimization techniques are :
  - Compile time evaluation: evaluating constant expressions and folding them into a single value at compile time.
  - Constant propagation: replacing the use of a variable with its constant value if it is known at compile time.
  - Common subexpression elimination: eliminating redundant computations of the same subexpression and reusing the previously computed value.
  - Code movement: moving invariant code out of loops or conditional blocks to reduce the execution time.
  - Dead code elimination: removing code that does not affect the output or the program behavior, such as unreachable statements or unused variables.
  - Strength reduction: replacing expensive operations with cheaper ones, such as multiplication with addition or division with shift.
- Some of the common machine-dependent optimization techniques are:
  - Instruction selection: choosing the best instruction or sequence of instructions to implement an operation or a statement.
  - Instruction scheduling: reordering the instructions to avoid stalls and improve the utilization of the functional units.
  - Register allocation: assigning the variables and temporary values to the available registers to minimize the memory accesses.
  - Peephole optimization: applying local transformations to a small window of instructions to eliminate or simplify them.
- Code optimization can also be guided by the profile of the program execution, which provides information about the frequency and cost of different parts of the code.
- Profile-guided optimization (PGO) is a technique that uses the profile data to perform more accurate and effective optimizations, such as inlining, loop unrolling, branch prediction, etc.