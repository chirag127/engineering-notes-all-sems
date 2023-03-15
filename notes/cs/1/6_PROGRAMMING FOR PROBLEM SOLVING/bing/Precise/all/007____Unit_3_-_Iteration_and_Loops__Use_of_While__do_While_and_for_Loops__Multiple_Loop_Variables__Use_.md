# Unit 3 - Iteration and Loops

## While Loop
- The `while` loop is used to repeatedly execute a block of code as long as a certain condition is true.
- The syntax for a `while` loop is:
```
while (condition) {
    // code block to be executed
}
```
- The condition is evaluated before each iteration. If the condition is true, the code block is executed. If the condition is false, the loop is exited.

## Do While Loop
- The `do while` loop is similar to the `while` loop, but the condition is evaluated after each iteration.
- The syntax for a `do while` loop is:
```
do {
    // code block to be executed
} while (condition);
```
- The code block is executed at least once, even if the condition is false.

## For Loop
- The `for` loop is used to repeatedly execute a block of code a specific number of times.
- The syntax for a `for` loop is:
```
for (initialization; condition; increment) {
    // code block to be executed
}
```
- The initialization is executed once before the loop starts. The condition is evaluated before each iteration. If the condition is true, the code block is executed. If the condition is false, the loop is exited. The increment is executed after each iteration.

## Multiple Loop Variables
- It is possible to use multiple loop variables in a `for` loop.
- The syntax for using multiple loop variables is:
```
for (initialization1, initialization2; condition; increment1, increment2) {
    // code block to be executed
}
```
- The initializations, conditions, and increments for each loop variable are separated by commas.

## Break Statement
- The `break` statement is used to exit a loop early.
- The `break` statement is placed inside the loop and is usually used with an `if` statement to exit the loop when a certain condition is met.

## Goto Statement
- The `goto` statement is used to transfer control to a specific location in the code.
- The syntax for a `goto` statement is:
```
goto label;
...
label: // code block to be executed
```
- The `goto` statement transfers control to the location specified by the label.

## Continue Statement
- The `continue` statement is used to skip the rest of the current iteration of a loop and start the next iteration.
- The `continue` statement is placed inside the loop and is usually used with an `if` statement to skip the rest of the current iteration when a certain condition is met.