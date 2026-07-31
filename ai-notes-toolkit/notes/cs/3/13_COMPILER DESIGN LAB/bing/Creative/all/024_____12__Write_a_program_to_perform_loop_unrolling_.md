# Loop unrolling

- Loop unrolling is a technique to optimize the performance of a program by reducing the number of iterations of a loop.
- Loop unrolling can reduce the overhead of loop control instructions, such as branch, compare, and increment, and increase the instruction-level parallelism of the code.
- Loop unrolling can also improve the cache locality of the data accessed by the loop, and reduce the number of pipeline stalls or cache misses.
- Loop unrolling can be done manually by the programmer, or automatically by the compiler or the processor.
- Loop unrolling can be applied to any loop that has a fixed or predictable number of iterations, and does not contain any break, continue, or return statements inside the loop body.
- Loop unrolling can be done by replicating the loop body multiple times, and adjusting the loop counter and the loop bounds accordingly.
- For example, consider the following loop that adds two arrays of size N:

```c
for (int i = 0; i < N; i++) {
  c[i] = a[i] + b[i];
}
```

- This loop can be unrolled by a factor of 4, meaning that the loop body is replicated 4 times, and the loop counter is incremented by 4 in each iteration:

```c
for (int i = 0; i < N; i += 4) {
  c[i] = a[i] + b[i];
  c[i+1] = a[i+1] + b[i+1];
  c[i+2] = a[i+2] + b[i+2];
  c[i+3] = a[i+3] + b[i+3];
}
```

- This loop unrolling reduces the number of iterations of the loop from N to N/4, and the number of loop control instructions from N to N/4.
- This loop unrolling also increases the instruction-level parallelism, as the four additions can be executed in parallel by the processor, if it has enough functional units and registers.
- This loop unrolling also improves the cache locality, as the four elements of each array are accessed consecutively, and are likely to be in the same cache line.
- However, loop unrolling also has some drawbacks, such as:
  - Increasing the code size and the instruction cache pressure, which may lead to more cache misses or branch mispredictions.
  - Introducing alignment or padding issues, which may cause performance degradation or memory waste.
  - Requiring extra handling for the case when the loop bound is not divisible by the unrolling factor, which may introduce more branch instructions or conditional statements.
  - Making the code less readable and maintainable, especially if the loop body is complex or contains function calls or nested loops.