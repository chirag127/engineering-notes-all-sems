## Unit 3 - Iteration and Loops: Use of While, do While and for Loops, Multiple Loop Variables, Use of Break , Goto and Continue Statements.

- Iteration and loops are programming concepts that allow a block of code to be executed repeatedly based on a condition or a range of values.
- There are three types of loops in C programming: while, do while and for loops.
- A while loop executes a block of code as long as a given condition is true. The syntax of a while loop is:

```c
while (condition)
{
    // statements
}
```

- A do while loop executes a block of code at least once, and then repeats it as long as a given condition is true. The syntax of a do while loop is:

```c
do
{
    // statements
} while (condition);
```

- A for loop executes a block of code for a specified number of times, or over a range of values. The syntax of a for loop is:

```c
for (initialization; condition; update)
{
    // statements
}
```

- The initialization, condition and update parts of a for loop are optional, but the semicolons are required. The initialization part is executed only once before the loop starts, the condition part is checked before each iteration, and the update part is executed after each iteration.
- A loop can have multiple loop variables, which are variables that change their values during the loop execution. For example, the following for loop has two loop variables, i and j:

```c
for (i = 0, j = 10; i < j; i++, j--)
{
    // statements
}
```

- The loop variables can be of different types, such as int, char, float, etc.
- A loop can be terminated prematurely by using the break statement, which exits the loop immediately. For example, the following while loop breaks when the variable x becomes 5:

```c
while (1)
{
    x = rand() % 10; // generate a random number between 0 and 9
    printf("%d\n", x);
    if (x == 5)
    {
        break; // exit the loop
    }
}
```

- A loop can be skipped partially by using the continue statement, which skips the rest of the current iteration and jumps to the next one. For example, the following for loop prints only the odd numbers between 1 and 10:

```c
for (i = 1; i <= 10; i++)
{
    if (i % 2 == 0)
    {
        continue; // skip even numbers
    }
    printf("%d\n", i);
}
```

- A loop can be labeled by using a name followed by a colon before the loop. For example, the following loop is labeled as outer:

```c
outer: for (i = 0; i < 5; i++)
{
    // statements
}
```

- A labeled loop can be exited or skipped by using the goto statement, which transfers the control to the label specified. For example, the following nested loops break out of the outer loop when the variable x becomes 5:

```c
outer: for (i = 0; i < 5; i++)
{
    for (j = 0; j < 5; j++)
    {
        x = rand() % 10; // generate a random number between 0 and 9
        printf("%d\n", x);
        if (x == 5)
        {
            goto outer; // exit the outer loop
        }
    }
}
```

- The use of goto statement is generally discouraged, as it can make the code difficult to read and maintain. It is better to use break or continue statements instead, or refactor the code to avoid the need for goto.