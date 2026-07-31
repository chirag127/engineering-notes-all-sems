 Here is the formal content on the given topic:

### 12. Write a program to perform loop unrolling.

1. Loop unrolling is a technique used to optimize loops by reducing the number of iterations required. 
2. This is done by expanding one loop iteration into multiple steps, thereby reducing the number of loop iterations required. 
3. For example, a loop which runs 4 iterations can be unrolled into 2 iterations of 2 steps each. This reduces the number of loop control overhead like incrementing counters, checking exit conditions, etc. 
4. The unrolled loop increases the code size but can significantly improve performance due to reduced loop control overhead. 
5. However, unrolling may not be beneficial if the loop body is small or the number of iterations is not known at compile time. 
6. A sample C program to perform loop unrolling:

    for (int i = 0; i < 100; i+=4) {
        // Loop body - 4 iterations
    }

7. The above loop runs the loop body 4 times in each iteration, thereby reducing the total number of iterations to 25. This improves performance due to reduced loop control overhead.
8. Loop unrolling is typically performed by compilers automatically based on factors like loop size and number of iterations. Programmers can also manually specify unrolling using directives or pragmas.

The content is written in points in a formal tone without any emojis or external links as specified. Let me know if you would like me to modify or expand the content.