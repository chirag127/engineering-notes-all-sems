### Loop optimization

- Loop optimization is a technique of code generation that aims to improve the performance of loops by reducing the number of iterations or the amount of work done in each iteration.
- Loop optimization can be applied at different levels of code representation, such as source code, intermediate code, or machine code.
- Loop optimization can be classified into two categories: loop-invariant code motion and loop transformation.

#### Loop-invariant code motion

- Loop-invariant code motion is a technique that moves code that does not depend on the loop variable or the loop iteration outside the loop body, so that it is executed only once before the loop starts.
- Loop-invariant code motion can reduce the number of instructions executed in each loop iteration, and can also enable other optimizations such as constant folding, dead code elimination, or common subexpression elimination.
- Loop-invariant code motion can be applied by identifying the loop-invariant expressions in the loop body, and hoisting them to a preheader block that precedes the loop entry block.
- Loop-invariant code motion can be illustrated by the following example:

```c
// Original code
for (i = 0; i < n; i++) {
  x = a + b; // loop-invariant expression
  y = x * i; // loop-dependent expression
  z = y + c; // loop-dependent expression
}

// Optimized code
x = a + b; // moved outside the loop
for (i = 0; i < n; i++) {
  y = x * i; // loop-dependent expression
  z = y + c; // loop-dependent expression
}
```

#### Loop transformation

- Loop transformation is a technique that changes the structure or the order of execution of loops, without changing the semantics of the program.
- Loop transformation can improve the performance of loops by exploiting parallelism, locality, or vectorization opportunities, or by reducing loop overhead or loop nesting.
- Loop transformation can be applied by applying various loop transformation operators, such as loop interchange, loop fusion, loop fission, loop unrolling, loop tiling, loop reversal, loop skewing, loop distribution, or loop peeling.
- Loop transformation can be illustrated by the following examples:

```c
// Original code
for (i = 0; i < n; i++) {
  for (j = 0; j < m; j++) {
    A[i][j] = B[i][j] + C[i][j]; // loop body
  }
}

// Optimized code by loop interchange
for (j = 0; j < m; j++) {
  for (i = 0; i < n; i++) {
    A[i][j] = B[i][j] + C[i][j]; // loop body
  }
}
```

- Loop interchange is a technique that swaps the order of nested loops, to improve the spatial locality of memory accesses, or to enable parallelization or vectorization of the inner loop.

```c
// Original code
for (i = 0; i < n; i++) {
  foo(i); // loop body 1
  for (j = 0; j < m; j++) {
    bar(i, j); // loop body 2
  }
}

// Optimized code by loop fusion
for (i = 0; i < n; i++) {
  foo(i); // loop body 1
  bar(i, 0); // loop body 2
  for (j = 1; j < m; j++) {
    bar(i, j); // loop body 2
  }
}
```

- Loop fusion is a technique that merges two adjacent loops that have the same loop bounds and loop index, to reduce the loop overhead and improve the temporal locality of memory accesses.

```c
// Original code
for (i = 0; i < n; i++) {
  foo(i); // loop body 1
}
for (i = 0; i < n; i++) {
  bar(i); // loop body 2
}

// Optimized code by loop fission
for (i = 0; i < n; i += 2) {
  foo(i); // loop body 1
  foo(i + 1); // loop body 1
}
for (i = 0; i < n; i += 2) {
  bar(i); // loop body 2
  bar(i + 1); // loop body 2
}
```

- Loop fission is a technique that splits a loop into two loops that have the same loop bounds and loop index, but execute different parts of the loop body, to enable parallelization