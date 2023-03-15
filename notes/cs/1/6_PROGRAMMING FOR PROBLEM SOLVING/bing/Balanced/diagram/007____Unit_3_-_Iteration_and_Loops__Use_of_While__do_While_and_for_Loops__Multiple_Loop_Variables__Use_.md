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

- The initialization, condition and update parts of a for loop are optional, but the semicolons are required.
- Multiple loop variables can be used in a for loop to control the iteration. For example:

```c
for (i = 0, j = 10; i < j; i++, j--)
{
    // statements
}
```

- This loop uses two variables, i and j, to iterate from both ends of a range.
- The break statement can be used to terminate a loop prematurely. For example:

```c
for (i = 0; i < 10; i++)
{
    if (i == 5)
    {
        break; // exit the loop
    }
    // statements
}
```

- This loop will stop when i reaches 5, and the statements after the break will not be executed.
- The goto statement can be used to transfer the control of the program to a specified label. For example:

```c
for (i = 0; i < 10; i++)
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

- This loop will also stop when i reaches 5, and the statements after the goto will be skipped. The statements after the label end will be executed.
- The continue statement can be used to skip the current iteration of a loop and proceed to the next one. For example:

```c
for (i = 0; i < 10; i++)
{
    if (i % 2 == 0)
    {
        continue; // skip the even numbers
    }
    // statements
}
```

- This loop will only execute the statements for the odd numbers, and the continue statement will skip the even numbers.