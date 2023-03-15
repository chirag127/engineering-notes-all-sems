### 12. Write a program to perform loop unrolling

Loop unrolling is a technique used to optimize the execution time of a program by reducing the number of iterations of a loop. This is achieved by replicating the body of the loop multiple times and adjusting the loop control variable accordingly.

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

In this example, the loop is unrolled by a factor of 5. This means that the body of the loop is replicated 5 times and the loop control variable is incremented by 5 in each iteration. This reduces the number of iterations of the loop from 100 to 20, resulting in faster execution of the program.

- Loop unrolling can improve the performance of a program by reducing the overhead associated with loop control instructions.
- However, it can also increase the size of the code, which may have a negative impact on performance if the code size exceeds the size of the instruction cache.
- Loop unrolling is most effective when the number of iterations of the loop is known at compile time and is a multiple of the unrolling factor.
- It is important to carefully choose the unrolling factor to balance the trade-off between code size and performance.