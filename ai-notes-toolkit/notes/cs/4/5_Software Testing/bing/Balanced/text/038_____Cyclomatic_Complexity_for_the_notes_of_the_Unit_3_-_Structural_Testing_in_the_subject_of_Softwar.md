### Cyclomatic Complexity

- Cyclomatic complexity is a software metric used to indicate the complexity of a program.
- It is a quantitative measure of the number of linearly independent paths through a program's source code.
- It was developed by Thomas J. McCabe, Sr. in 1976.
- Cyclomatic complexity can be calculated using the following formula:

    `C = E - N + 2P`

    where C is the cyclomatic complexity, E is the number of edges in the control flow graph, N is the number of nodes in the control flow graph, and P is the number of connected components.

- Cyclomatic complexity can also be calculated using the following formula:

    `C = D + 1`

    where C is the cyclomatic complexity and D is the number of decision structures in the code, such as if, while, for, switch, etc.

- Cyclomatic complexity can predict how hard it is to test a given piece of code.
- Cyclomatic complexity is the minimum number of test cases needed to achieve full branch coverage.
- Cyclomatic complexity can help identify code that is prone to errors, bugs, or maintenance issues.
- Cyclomatic complexity can be reduced by refactoring the code, such as extracting methods, simplifying conditions, using polymorphism, etc.

- Example: Consider the following code snippet:

    ```csharp
    public void DoSomething(int x, int y)
    {
        if (x > 0)
        {
            Console.WriteLine("x is positive");
        }
        else
        {
            Console.WriteLine("x is negative or zero");
        }

        switch (y)
        {
            case 1:
                Console.WriteLine("y is one");
                break;
            case 2:
                Console.WriteLine("y is two");
                break;
            default:
                Console.WriteLine("y is something else");
                break;
        }
    }
    ```

    - The cyclomatic complexity of this code can be calculated using the first formula as follows:

        `C = E - N + 2P`

        where E is the number of edges in the control flow graph, N is the number of nodes in the control flow graph, and P is the number of connected components.

        - The control flow graph of this code is shown below:

            ![control flow graph](https://docs.microsoft.com/en-us/visualstudio/code-quality/media/code-metrics-cyclomatic-complexity/cyclomatic-complexity.png?view=vs-2022)

        - The number of edges in the control flow graph is 10.
        - The number of nodes in the control flow graph is 9.
        - The number of connected components is 1.
        - Therefore, the cyclomatic complexity is:

            `C = 10 - 9 + 2 * 1`

            `C = 3`

    - The cyclomatic complexity of this code can also be calculated using the second formula as follows:

        `C = D + 1`

        where D is the number of decision structures in the code, such as if, while, for, switch, etc.

        - The number of decision structures in the code is 2: the if statement and the switch statement.
        - Therefore, the cyclomatic complexity is:

            `C = 2 + 1`

            `C = 3`

    - The cyclomatic complexity of this code is 3, which means that at least 3 test cases are needed to achieve full branch coverage.
    - The cyclomatic complexity of this code is relatively low, which means that the code is not very complex and easy to test.