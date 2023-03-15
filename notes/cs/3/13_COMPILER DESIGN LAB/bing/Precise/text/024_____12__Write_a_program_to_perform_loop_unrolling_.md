### 12. Write a program to perform loop unrolling

Loop unrolling is a technique used to optimize the execution time of a program by reducing the number of iterations of a loop. This is done by replicating the body of the loop multiple times and adjusting the loop control variable accordingly.

Here is an example of loop unrolling in C:

```c
#include <stdio.h>

int main() {
    int i;
    for (i = 0; i < 100; i += 5) {
        printf("%d\n", i);
        printf("%d\n", i + 1);
        printf("%d\n", i + 2);
        printf("%d\n", i + 3);
        printf("%d\n", i + 4);
    }
    return 0;
}
```

In this example, the loop iterates 20 times instead of 100 times, and the body of the loop is executed 5 times in each iteration. This can result in faster execution time, especially if the loop body contains computationally expensive operations.

However, loop unrolling can also increase the size of the code and make it less readable. It is important to carefully consider the trade-offs before using this technique.

- Loop unrolling can reduce the number of iterations of a loop.
- This is done by replicating the body of the loop multiple times.
- Loop unrolling can result in faster execution time.
- However, it can also increase the size of the code and make it less readable.
- It is important to carefully consider the trade-offs before using this technique.