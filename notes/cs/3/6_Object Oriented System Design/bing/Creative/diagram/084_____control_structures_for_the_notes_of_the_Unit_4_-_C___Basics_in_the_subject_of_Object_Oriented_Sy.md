Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of control structures for the notes of the Unit 4 - C++ Basics in the subject of Object Oriented System Design.

### Control Structures
- Control structures are statements that determine the flow of execution of a program.
- Control structures can be classified into three types: sequential, selection and iteration.
- Sequential control structures are the default ones that execute statements one after another in the order they are written.
- Selection control structures allow the program to choose between two or more alternative paths based on some condition.
- Iteration control structures allow the program to repeat a block of statements until some condition is met.
- C++ provides various control structures for selection and iteration, such as if, if-else, switch, for, while, do-while, break, continue, and goto.

#### If Statement
- The if statement is a selection control structure that executes a block of statements if a condition is true, and skips it otherwise.
- The syntax of the if statement is:

```cpp
if (condition)
{
    // statements to execute if condition is true
}
```

- The condition can be any expression that evaluates to a bool value (true or false).
- The block of statements can be a single statement or multiple statements enclosed in curly braces.
- The block of statements is optional, but it is recommended to always use curly braces for clarity and consistency.
- Example:

```cpp
int x = 10;
if (x > 0)
{
    cout << "x is positive" << endl;
}
```

#### If-Else Statement
- The if-else statement is an extension of the if statement that executes one block of statements if a condition is true, and another block of statements if the condition is false.
- The syntax of the if-else statement is:

```cpp
if (condition)
{
    // statements to execute if condition is true
}
else
{
    // statements to execute if condition is false
}
```

- The else part is optional, but it is recommended to always use it for completeness and readability.
- Example:

```cpp
int x = -10;
if (x > 0)
{
    cout << "x is positive" << endl;
}
else
{
    cout << "x is negative" << endl;
}
```

#### Nested If-Else Statement
- The nested if-else statement is a combination of multiple if-else statements inside each other.
- The nested if-else statement allows the program to test more than one condition and choose among multiple alternative paths.
- The syntax of the nested if-else statement is:

```cpp
if (condition1)
{
    // statements to execute if condition1 is true
    if (condition2)
    {
        // statements to execute if condition2 is true
    }
    else
    {
        // statements to execute if condition2 is false
    }
}
else
{
    // statements to execute if condition1 is false
    if (condition3)
    {
        // statements to execute if condition3 is true
    }
    else
    {
        // statements to execute if condition3 is false
    }
}
```

- The nested if-else statement can have any number of levels of nesting, but it is advisable to avoid too much nesting as it can make the code complex and difficult to read and debug.
- Example:

```cpp
int x = 10, y = 20, z = 30;
if (x > y)
{
    if (x > z)
    {
        cout << "x is the largest" << endl;
    }
    else
    {
        cout << "z is the largest" << endl;
    }
}
else
{
    if (y > z)
    {
        cout << "y is the largest" << endl;
    }
    else
    {
        cout << "z is the largest" << endl;
    }
}
```

#### Switch Statement
- The switch statement is a selection control structure that allows the program to choose among multiple cases based on the value of an expression.
- The switch statement is useful when the program needs to perform different actions for different values of the same variable or expression.
- The syntax of the switch statement is:

```cpp
switch (expression)
{
    case value1:
        // statements to execute if expression matches value1
        break;
    case value2:
        // statements to execute if expression matches value2
        break;
    ...
    default:
        // statements to execute if expression does not match any case value
        break;
}
```

- The expression can be any expression that evaluates to an int,