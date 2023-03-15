### Code optimization for the notes of the Unit 5 - Code Generation in the subject of Compiler Design

Code optimization is the process of improving the quality and efficiency of the generated code by applying various techniques and transformations. Code optimization can be performed at different levels of the compiler, such as source code, intermediate code, or object code. Code optimization can be machine-independent or machine-dependent, depending on whether the techniques are applicable to any target machine or specific to a particular architecture.

Some of the common goals of code optimization are:

- Reducing the execution time of the program
- Reducing the memory usage of the program
- Reducing the power consumption of the program
- Improving the readability and maintainability of the code
- Enhancing the portability and compatibility of the code

Some of the common techniques of code optimization are:

- Compile-time evaluation: This technique involves evaluating constant expressions and variables at compile time, rather than at run time, to avoid unnecessary computations. For example, `2 * (22.0 / 7.0) * r` can be evaluated as `44.0 * r` at compile time.
- Constant propagation: This technique involves replacing the occurrences of a variable with its constant value, if the variable is assigned a constant value. For example, `x = 12.4; y = x / 2.3;` can be replaced by `y = 12.4 / 2.3;`.
- Constant folding: This technique involves simplifying constant expressions by applying arithmetic or logical operations. For example, `x = 2 + 3 * 4;` can be simplified as `x = 14;`.
- Common subexpression elimination: This technique involves identifying and eliminating redundant computations of the same subexpression. For example, `a = b + c; d = b + c;` can be replaced by `a = b + c; d = a;`.
- Code movement: This technique involves moving code statements or expressions out of loops or branches, if they do not depend on the loop or branch condition. This can reduce the number of executions of the code and improve the performance. For example, `for (i = 0; i < n; i++) { x = y + z; a[i] = x * i; }` can be replaced by `x = y + z; for (i = 0; i < n; i++) { a[i] = x * i; }`.
- Dead code elimination: This technique involves removing code statements or expressions that have no effect on the output of the program. For example, `x = 10; x = 20; y = x + 5;` can be replaced by `y = 25;`.
- Strength reduction: This technique involves replacing expensive operations with cheaper ones, such as using shifts instead of multiplications or divisions, or using additions instead of multiplications. For example, `x = y * 8;` can be replaced by `x = y << 3;`.
- Loop optimization: This technique involves applying various transformations to loops, such as loop unrolling, loop fusion, loop inversion, loop invariant code motion, loop induction variable elimination, loop interchange, loop distribution, loop peeling, loop tiling, etc. These transformations can improve the performance, parallelism, and locality of loops.
- Function inlining: This technique involves replacing a function call with the body of the function, to avoid the overhead of function call and return. This can improve the performance and code size, but may also increase the code size if the function is large or called many times.
- Tail recursion elimination: This technique involves converting a tail recursive function into a loop, to avoid the overhead of recursive calls and stack frames. A tail recursive function is one that has a recursive call as the last statement in the function body.
- Machine-dependent optimization: This technique involves applying optimizations that are specific to the target machine architecture, such as instruction selection, instruction scheduling, register allocation, instruction encoding, etc. These optimizations can exploit the features and constraints of the target machine, such as instruction set, pipeline, cache, registers, etc.
- Profile-guided optimization: This technique involves collecting and using the runtime information of the program, such as execution frequency, branch prediction, cache behavior, etc., to guide the optimization decisions. This can improve the performance and accuracy of the optimizations, but may also increase the