## Unit 3 - Iteration and Loops: Use of While, do While and for Loops, Multiple Loop Variables, Use of Break , Goto and Continue Statements

In this unit, we will learn about iteration and loops. Iteration is the process of repeating a task until a certain condition is met. Loops are used to perform iteration in programming. There are three types of loops: while loops, do while loops, and for loops.

### While Loops

A while loop is used to repeat a block of code while a certain condition is true. The syntax of a while loop is as follows:

```
while (condition) {
    // code block to be executed
}
```

The code block will be executed repeatedly as long as the condition is true.

### Do While Loops

A do while loop is similar to a while loop, except that the code block is executed at least once, even if the condition is false. The syntax of a do while loop is as follows:

```
do {
    // code block to be executed
} while (condition);
```

### For Loops

A for loop is used to repeat a block of code a specific number of times. The syntax of a for loop is as follows:

```
for (initialization; condition; increment) {
    // code block to be executed
}
```

The initialization is performed once at the beginning of the loop, the condition is checked before each iteration, and the increment is performed after each iteration.

### Multiple Loop Variables

In a for loop, it is possible to use multiple loop variables. The syntax of a for loop with multiple variables is as follows:

```
for (int i = 0, j = 10; i < j; i++, j--) {
    // code block to be executed
}
```

### Use of Break Statements

The break statement is used to exit a loop. When a break statement is encountered, the loop is immediately exited, and the program continues with the next statement. The syntax of a break statement is as follows:

```
while (condition) {
    if (someCondition) {
        break;
    }
}
```

### Use of Goto Statements

The goto statement is used to transfer control to a different part of the program. The syntax of a goto statement is as follows:

```
goto label;
```

The label must be defined somewhere in the program.

### Use of Continue Statements

The continue statement is used to skip the current iteration of a loop and continue with the next iteration. The syntax of a continue statement is as follows:

```
while (condition) {
    if (someCondition) {
        continue;
    }
    // code block to be executed
}
```

In conclusion, iteration and loops are important concepts in programming, and understanding how to use while loops, do while loops, and for loops, as well as multiple loop variables, break statements, goto statements, and continue statements, is essential for writing efficient and effective code.