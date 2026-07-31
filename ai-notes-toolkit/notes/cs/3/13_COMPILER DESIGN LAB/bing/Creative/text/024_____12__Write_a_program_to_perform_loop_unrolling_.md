### 12. Write a program to perform loop unrolling.

- Loop unrolling is a technique to optimize the performance of a program by reducing the number of iterations in a loop.
- Loop unrolling can reduce the overhead of loop control instructions, such as incrementing the loop counter, checking the loop condition, and branching to the loop body.
- Loop unrolling can also increase the instruction-level parallelism, by allowing more operations to be executed in parallel within a single iteration of the unrolled loop.
- Loop unrolling can be done manually by the programmer, or automatically by the compiler, depending on the language and the optimization level.
- Loop unrolling can improve the performance of a program, but it can also increase the code size and the register pressure, which may have negative effects on the cache and the memory usage.
- Loop unrolling is not always beneficial, and it depends on the characteristics of the loop, such as the number of iterations, the complexity of the loop body, the data dependencies, and the target architecture.
- An example of loop unrolling in C is shown below:

```c
// Original loop
for (int i = 0; i < n; i++) {
  a[i] = b[i] + c[i];
}

// Unrolled loop by a factor of 4
for (int i = 0; i < n; i += 4) {
  a[i] = b[i] + c[i];
  a[i+1] = b[i+1] + c[i+1];
  a[i+2] = b[i+2] + c[i+2];
  a[i+3] = b[i+3] + c[i+3];
}
```

- The unrolled loop has fewer iterations, and each iteration performs four additions in parallel, instead of one.
- The unrolled loop may run faster than the original loop, but it also requires more code space and more registers to store the intermediate results.
- The unrolled loop may also have problems if the loop bound n is not divisible by 4, which requires additional checks or padding to handle the remaining iterations.