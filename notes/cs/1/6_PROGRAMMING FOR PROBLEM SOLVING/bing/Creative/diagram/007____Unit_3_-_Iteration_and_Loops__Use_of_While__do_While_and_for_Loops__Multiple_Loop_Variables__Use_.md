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

- The initialization, condition and update expressions are optional, but the semicolons are required.
- A loop can have multiple loop variables, which are variables that change their values during each iteration of the loop. For example:

```c
for (int i = 0, j = 10; i < j; i++, j--)
{
    // statements
}
```

- This loop has two loop variables, i and j, which are initialized to 0 and 10 respectively, and are updated by incrementing and decrementing respectively. The loop condition is i < j, which means the loop will stop when i and j are equal or i is greater than j.
- A break statement can be used to terminate a loop prematurely, regardless of the loop condition. For example:

```c
for (int i = 0; i < 10; i++)
{
    if (i == 5)
    {
        break; // exit the loop
    }
    // statements
}
```

- This loop will stop when i is equal to 5, because of the break statement.
- A goto statement can be used to transfer the control of the program to a specified label. A label is an identifier followed by a colon. For example:

```c
for (int i = 0; i < 10; i++)
{
    if (i == 5)
    {
        goto end; // jump to the label end
    }
    // statements
}
end: // label
// statements
```

- This loop will also stop when i is equal to 5, because of the goto statement. However, the use of goto is generally discouraged, as it can make the program difficult to read and debug.
- A continue statement can be used to skip the current iteration of the loop and proceed to the next one, without exiting the loop. For example:

```c
for (int i = 0; i < 10; i++)
{
    if (i % 2 == 0)
    {
        continue; // skip the even numbers
    }
    // statements
}
```

- This loop will only execute the statements for the odd values of i, because of the continue statement.