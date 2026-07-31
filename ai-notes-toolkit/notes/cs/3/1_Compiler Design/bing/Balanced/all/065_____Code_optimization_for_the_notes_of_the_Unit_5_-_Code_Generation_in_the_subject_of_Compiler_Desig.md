# Code optimization for the notes of the Unit 5 - Code Generation in the subject of Compiler Design

Code optimization is the process of improving the quality and efficiency of the generated code by applying various techniques and transformations. Code optimization can be performed at different levels of the compiler, such as source code, intermediate code, or object code. Code optimization can be classified into two major categories: machine-independent and machine-dependent.

Machine-independent optimization is applied to the intermediate code and does not depend on the target architecture or instruction set. Some examples of machine-independent optimization techniques are:

- Compile time evaluation: This technique evaluates constant expressions and arithmetic operations at compile time and replaces them with their results. For example, `2 * (22.0 / 7.0) * r` can be evaluated as `44.0 / 7.0 * r` at compile time.
- Constant propagation: This technique replaces the occurrences of a variable with its constant value if it is known. For example, if `x = 12.4`, then `x / 2.3` can be replaced with `12.4 / 2.3`.
- Constant folding: This technique simplifies constant expressions by applying arithmetic rules and identities. For example, `2 + 3 * 4` can be folded as `14`.
- Common subexpression elimination: This technique eliminates redundant computations of the same subexpression by reusing the previously computed value. For example, if `a = b + c` and `d = b + c`, then the second expression can be eliminated and replaced with `d = a`.
- Dead code elimination: This technique removes unreachable or unnecessary code that does not affect the output or the program behavior. For example, if `x = 10` and `if (x > 20) then y = 5` then the conditional statement can be eliminated as it is always false.
- Code movement: This technique moves code from one place to another to reduce the frequency of execution or to avoid repeated execution. For example, loop invariant code can be moved outside the loop to execute only once.

Machine-dependent optimization is applied to the object code and depends on the target architecture or instruction set. Some examples of machine-dependent optimization techniques are:

- Instruction selection: This technique chooses the best instruction or sequence of instructions to implement a given operation or expression. For example, some architectures may have special instructions for multiplication or division that are faster than the general ones.
- Instruction scheduling: This technique orders the instructions to maximize the parallelism and minimize the stalls or delays caused by dependencies or resource conflicts. For example, some instructions may have latency or delay before producing the result, so other independent instructions can be executed in the meantime.
- Register allocation: This technique assigns the variables or values to the registers to reduce the memory accesses and improve the performance. For example, some variables may be frequently used or live for a long time, so they can be allocated to the registers instead of the memory.
- Peephole optimization: This technique applies local transformations to a small window of instructions to improve the code quality. For example, some transformations are: eliminating redundant instructions, replacing expensive instructions with cheaper ones, combining adjacent instructions, or reordering instructions.