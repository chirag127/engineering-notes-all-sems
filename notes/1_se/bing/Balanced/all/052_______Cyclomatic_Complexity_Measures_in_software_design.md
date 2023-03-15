##### Cyclomatic Complexity Measures in software design

- Cyclomatic complexity is a software metric used to measure the complexity of a program .
- It is a count of the number of decisions in the source code. The higher the count, the more complex the code.
- It is calculated by using the control flow graph of the program, which is a graphical representation of the paths that can be traversed through the program during its execution .
- The formula for cyclomatic complexity is:

    `V(G) = E - N + 2P`

    where V(G) is the cyclomatic complexity, E is the number of edges, N is the number of nodes, and P is the number of connected components in the graph .

- Cyclomatic complexity can be used to:

    - Determine the number of independent paths through the program, which can help in designing test cases .
    - Assess the maintainability and readability of the code, as more complex code is harder to understand and modify.
    - Identify the potential defects and errors in the code, as more complex code is more prone to bugs.

- Some advantages of cyclomatic complexity are:

    - It is easy to compute and apply.
    - It is independent of the programming language and style.
    - It can help in improving the quality and reliability of the software.

- Some disadvantages of cyclomatic complexity are:

    - It does not consider the data flow or the logical complexity of the code.
    - It can be influenced by the coding conventions and the use of loops and conditional statements.
    - It does not account for the user requirements or the functionality of the software.

- An example of cyclomatic complexity calculation is shown below:

    ```c
    // A simple C program to calculate the area of a circle
    #include <stdio.h>
    #define PI 3.14

    int main()
    {
        float radius, area;
        printf("Enter the radius of the circle: ");
        scanf("%f", &radius);
        if (radius > 0)
        {
            area = PI * radius * radius;
            printf("The area of the circle is: %f\n", area);
        }
        else
        {
            printf("Invalid input\n");
        }
        return 0;
    }
    ```

    The control flow graph for this program is:

    ```
    +-----+     +-----+     +-----+     +-----+
    |  1  |---->|  2  |---->|  3  |---->|  4  |
    +-----+     +-----+     +-----+     +-----+
                      |           |
                      |           |
                      v           v
                    +-----+     +-----+
                    |  5  |     |  6  |
                    +-----+     +-----+
                      |           |
                      |           |
                      +----+ +----+
                           | |
                           v v
                         +-----+
                         |  7  |
                         +-----+
    ```

    The cyclomatic complexity is:

    `V(G) = E - N + 2P`

    `V(G) = 9 - 7 + 2*1`

    `V(G) = 4`

    This means that there are four independent paths through the program, which are:

    - 1-2-3-4-7
    - 1-2-5-7
    - 1-2-3-6-7
    - 1-2-5-6-7

- A possible mnemonic to remember the formula for cyclomatic complexity is:

    `V(G) = E - N + 2P`

    **V**ery **G**ood **E**xams **N**eed **2P**reparation