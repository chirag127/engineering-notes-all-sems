# Loop unrolling

- Loop unrolling is a technique to optimize the performance of a program by reducing the number of iterations of a loop.
- Loop unrolling can reduce the overhead of loop control instructions, such as checking the loop condition, incrementing the loop counter, and branching to the loop body.
- Loop unrolling can also increase the instruction-level parallelism, by allowing more operations to be executed in each iteration of the unrolled loop.
- Loop unrolling can be done manually by the programmer, or automatically by the compiler or the processor.
- Loop unrolling can improve the performance of a program, but it can also increase the code size and the register pressure, which may have negative effects on the cache and the memory usage.
- Loop unrolling is usually applied to loops that have a small and fixed number of iterations, and that do not contain complex or variable control flow.

## Example of loop unrolling

- Consider the following C code that computes the sum of the elements of an array:

```c
int sum = 0;
for (int i = 0; i < 100; i++) {
  sum += array[i];
}
```

- The loop can be unrolled by a factor of 4, which means that 4 iterations of the original loop are replaced by one iteration of the unrolled loop:

```c
int sum = 0;
for (int i = 0; i < 100; i += 4) {
  sum += array[i];
  sum += array[i + 1];
  sum += array[i + 2];
  sum += array[i + 3];
}
```

- The unrolled loop has fewer loop control instructions, and can execute 4 additions in parallel in each iteration. However, it also has more code and requires more registers to store the intermediate results.