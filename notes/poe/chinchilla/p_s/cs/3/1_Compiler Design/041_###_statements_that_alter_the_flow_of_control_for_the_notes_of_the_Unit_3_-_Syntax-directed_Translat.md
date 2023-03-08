### Statements that Alter the Flow of Control

Statements that alter the flow of control are an essential part of syntax-directed translation. They are responsible for determining the execution order of statements in a program. These statements are used to implement control structures such as loops, conditionals, and function calls. In this unit, we will discuss the following statements:

1. Conditional statements
2. Loop statements
3. Jump statements

#### Conditional Statements

Conditional statements are used to execute code based on a specific condition. The most common type of conditional statement is the if-else statement. The if statement executes a block of code if a condition is true. If the condition is false, the code inside the if statement is skipped, and the code inside the else statement (if present) is executed.

```
if (condition) {
    // code to execute if condition is true
} else {
    // code to execute if condition is false
}
```

#### Loop Statements

Loop statements are used to execute a block of code repeatedly until a condition is met. There are three types of loop statements: for, while, and do-while.

The for loop executes a block of code a specific number of times. It has three parts: initialization, condition, and increment/decrement.

```
for (initialization; condition; increment/decrement) {
    // code to execute
}
```

The while loop executes a block of code repeatedly as long as a condition is true.

```
while (condition) {
    // code to execute
}
```

The do-while loop is similar to the while loop, except that it guarantees that the code inside the loop is executed at least once.

```
do {
    // code to execute
} while (condition);
```

#### Jump Statements

Jump statements are used to transfer control to a different part of the program. There are three types of jump statements: break, continue, and goto.

The break statement is used to exit a loop prematurely.

```
while (condition) {
    if (break_condition) {
        break;
    }
    // code to execute
}
```

The continue statement is used to skip the rest of the current iteration of a loop and move on to the next iteration.

```
while (condition) {
    if (continue_condition) {
        continue;
    }
    // code to execute
}
```

The goto statement is used to transfer control to a different part of the program. It is considered harmful and should be avoided.

```
goto label;
// code to execute
label:
// code to execute
```

#### Conclusion

Statements that alter the flow of control are an essential part of syntax-directed translation. They are used to implement control structures such as loops, conditionals, and function calls. Understanding these statements is crucial for writing efficient and correct compilers.