### 12. Write a program to perform loop unrolling.

Loop unrolling is a technique used to optimize the performance of loops in computer programs. It involves replacing a loop with a series of statements that execute the loop body multiple times. Here are the steps to write a program to perform loop unrolling:

1. Start by defining a loop to be unrolled. For example, consider the following loop:

```c
for (int i = 0; i < N; i++) {
    // loop body
}
```

2. Determine the number of times the loop should be unrolled. This depends on factors such as the size of the loop body and the number of iterations.

3. Replace the loop with a series of statements that execute the loop body multiple times. For example, if the loop is unrolled by a factor of 4, the code would look like this:

```c
for (int i = 0; i < N; i += 4) {
    // loop body
    // loop body
    // loop body
    // loop body
}
```

4. Repeat step 3 for each iteration of the loop. For example, if the loop is unrolled by a factor of 4, the code would look like this:

```c
for (int i = 0; i < N; i += 4) {
    // loop body
    // loop body
    // loop body
    // loop body
}

for (int i = 1; i < N; i += 4) {
    // loop body
    // loop body
    // loop body
    // loop body
}

for (int i = 2; i < N; i += 4) {
    // loop body
    // loop body
    // loop body
    // loop body
}

for (int i = 3; i < N; i += 4) {
    // loop body
    // loop body
    // loop body
    // loop body
}
```

5. Compile and test the code to ensure that it works correctly and provides the desired performance improvement.

Loop unrolling is a useful technique for optimizing the performance of loops in computer programs. However, it is important to choose the appropriate unrolling factor and to test the code thoroughly to ensure that it works correctly.