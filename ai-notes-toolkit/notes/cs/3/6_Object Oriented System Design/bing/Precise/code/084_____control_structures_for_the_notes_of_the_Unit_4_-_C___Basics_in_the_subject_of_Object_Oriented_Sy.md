### Control Structures

Control structures are used to control the flow of execution of a program. They allow the program to make decisions and repeat actions. In C++, there are three types of control structures: sequence, selection, and iteration.

1. **Sequence**: This is the default control structure, where statements are executed in the order in which they appear in the program.

2. **Selection**: This control structure allows the program to make decisions based on certain conditions. The two main selection statements in C++ are `if` and `switch`.

    - `if` statement: This statement allows the program to execute a block of code only if a certain condition is true. The syntax for the `if` statement is as follows:
    ```
    if (condition)
    {
        // statements to be executed if condition is true
    }
    ```
    - `switch` statement: This statement allows the program to execute one of several blocks of code, depending on the value of a certain expression. The syntax for the `switch` statement is as follows:
    ```
    switch (expression)
    {
        case constant1:
            // statements to be executed if expression == constant1
            break;
        case constant2:
            // statements to be executed if expression == constant2
            break;
        ...
        default:
            // statements to be executed if expression does not match any constant
    }
    ```

3. **Iteration**: This control structure allows the program to repeat a block of code a certain number of times, or until a certain condition is met. The three main iteration statements in C++ are `while`, `do-while`, and `for`.

    - `while` loop: This loop executes a block of code repeatedly as long as a certain condition is true. The syntax for the `while` loop is as follows:
    ```
    while (condition)
    {
        // statements to be executed while condition is true
    }
    ```
    - `do-while` loop: This loop is similar to the `while` loop, but the block of code is executed at least once, even if the condition is false. The syntax for the `do-while` loop is as follows:
    ```
    do
    {
        // statements to be executed
    } while (condition);
    ```
    - `for` loop: This loop is used to repeat a block of code a fixed number of times. The syntax for the `for` loop is as follows:
    ```
    for (initialization; condition; increment)
    {
        // statements to be executed
    }
    ```

These are the main control structures in C++. They allow the program to make decisions and repeat actions, making it more flexible and powerful. It is important to use the appropriate control structure for the task at hand, in order to write clear and efficient code.