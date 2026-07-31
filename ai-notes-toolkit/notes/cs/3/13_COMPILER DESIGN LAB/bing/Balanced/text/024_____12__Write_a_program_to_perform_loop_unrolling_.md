### 12. Write a program to perform loop unrolling.

- Loop unrolling is a technique that reduces the overhead of loop control instructions by replicating the loop body multiple times and adjusting the loop bounds accordingly.
- Loop unrolling can improve the performance of a program by increasing the instruction-level parallelism, reducing the branch misprediction penalty, and exploiting the cache locality of data.
- Loop unrolling can also have some drawbacks, such as increasing the code size, causing register pressure, and wasting computation if the loop iterations are not divisible by the unrolling factor.
- To perform loop unrolling, we need to identify the loop that can benefit from this technique, determine the unrolling factor, and modify the loop body and the loop condition accordingly.
- Here is an example of a C program that performs loop unrolling on a simple loop that adds two arrays:

```c
// Original loop
for (i = 0; i < n; i++) {
  c[i] = a[i] + b[i];
}

// Unrolled loop with unrolling factor of 4
for (i = 0; i < n; i += 4) {
  c[i] = a[i] + b[i];
  c[i+1] = a[i+1] + b[i+1];
  c[i+2] = a[i+2] + b[i+2];
  c[i+3] = a[i+3] + b[i+3];
}

// Handle the remaining iterations if n is not divisible by 4
for (; i < n; i++) {
  c[i] = a[i] + b[i];
}
```