 Here is the content in markdown format for the topic -

### 12. Write a program to perform loop unrolling.

Loop unrolling is a technique used to optimize loops by reducing the overhead of looping constructs. It involves expanding or 'unrolling' a loop's body multiple times, thus reducing the number of iterations required.

For example, consider a loop which executes 4 iterations:

for (i = 0; i < 4; i++) {
    // code block to be executed
}

This can be unrolled as:

// code block to be executed
// code block to be executed
// code block to be executed
// code block to be executed

The advantages of loop unrolling are:

- Reduces the number of comparisons and branch instructions, thus improving processor efficiency.
- The loop exit test is evaluated fewer times.
- More instruction-level parallelism can be exploited as more instructions are available at a time for execution.

The disadvantages are:

- The code size increases as the loop body is expanded multiple times. This can be significant for loops with large number of iterations.
- Extra registers may be required to hold the unrolled loop variables.
- Unrolling may not be effective if the loop body is short or the processor has an efficient looping mechanism.

A sample C program to perform loop unrolling is shown below:

void unroll_loop(int n) {
    int i = 0;
    //Unroll the loop 4 times
    //This is equivalent to executing the loop body for i=0 to 3
    //code block to be executed
    //code block to be executed
    //code block to be executed
    //code block to be executed
    //Remaining iterations
    for (; i < n - 4; i++) {
        //code block to be executed
    }
}

The level of unrolling (4 in this case) is a trade-off between the code size increase and performance gain and is dependent on the processor architecture and loop body. Loop unrolling is commonly performed by compilers using an optimization technique called loop unswitching.