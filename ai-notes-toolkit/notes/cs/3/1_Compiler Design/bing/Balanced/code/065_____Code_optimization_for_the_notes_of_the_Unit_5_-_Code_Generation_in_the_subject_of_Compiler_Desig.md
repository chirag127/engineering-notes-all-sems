### Code optimization for the notes of the Unit 5 - Code Generation in the subject of Compiler Design

Code optimization is the process of improving the quality and efficiency of the generated code by applying various techniques and transformations. Code optimization can be done at different levels of the compiler, such as source code, intermediate code, or object code. Code optimization can be machine-independent or machine-dependent, depending on whether the techniques are applicable to any target machine or specific to a particular architecture.

Some of the common goals of code optimization are:

- Reducing the execution time of the code
- Reducing the memory usage of the code
- Reducing the power consumption of the code
- Improving the readability and maintainability of the code
- Enhancing the portability and compatibility of the code

Some of the common techniques of code optimization are:

- Compile-time evaluation: This technique evaluates constant expressions and variables at compile time and replaces them with their values, thus saving run-time computation. For example, `2 * (22.0/7.0) * r` can be evaluated as `44.0 * r` at compile time.
- Constant propagation: This technique propagates the values of constant variables to their uses and replaces them with their values, thus eliminating unnecessary assignments and references. For example, `x = 12.4; y = x / 2.3;` can be replaced by `y = 12.4 / 2.3;`.
- Constant folding: This technique evaluates constant expressions and replaces them with their values, thus reducing the number of operations. For example, `x = 2 + 3 * 4;` can be replaced by `x = 14;`.
- Common subexpression elimination: This technique identifies and eliminates redundant computations of the same subexpression, thus saving run-time computation. For example, `x = a + b + c; y = a + b + c + d;` can be replaced by `x = a + b + c; y = x + d;`.
- Dead code elimination: This technique removes unreachable or unnecessary code that does not affect the output of the program, thus saving memory and execution time. For example, `if (false) { x = 10; }` can be removed as the statement is never executed.
- Code movement: This technique moves invariant code out of loops or conditional statements, thus reducing the number of executions. For example, `for (i = 0; i < n; i++) { x = a + b; y = x * i; }` can be replaced by `x = a + b; for (i = 0; i < n; i++) { y = x * i; }`.
- Strength reduction: This technique replaces expensive operations with cheaper ones, such as multiplication with addition, division with shift, etc. For example, `x = y * 8;` can be replaced by `x = y << 3;`.
- Loop optimization: This technique applies various transformations to loops, such as loop unrolling, loop fusion, loop inversion, loop invariant code motion, loop induction variable elimination, etc. to improve the performance of loops.
- Function inlining: This technique replaces a function call with the body of the function, thus eliminating the overhead of function call and return. For example, `int square(int x) { return x * x; } y = square(z);` can be replaced by `y = z * z;`.
- Machine-dependent optimization: This technique exploits the features and characteristics of the target machine, such as instruction set, registers, pipelines, caches, etc. to generate optimal code. For example, using a faster calling convention, using compiler-intrinsic functions, using profile-guided optimization, etc .