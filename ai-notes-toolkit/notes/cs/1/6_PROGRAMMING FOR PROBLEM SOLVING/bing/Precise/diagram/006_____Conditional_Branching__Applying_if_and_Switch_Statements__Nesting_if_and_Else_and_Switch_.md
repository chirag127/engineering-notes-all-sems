### Conditional Branching: Applying if and Switch Statements, Nesting if and Else and Switch

Conditional branching is a fundamental concept in programming that allows the program to execute different code blocks depending on whether a condition is true or false. The two main conditional statements in many programming languages are the `if` statement and the `switch` statement.

1. **The `if` statement**: The `if` statement is used to execute a block of code if a specified condition is true. If the condition is false, the code block is skipped. The basic syntax of an `if` statement is as follows:
```
if (condition) {
    // code to be executed if condition is true
}
```
2. **The `else` statement**: The `else` statement is used in conjunction with the `if` statement to execute a block of code if the condition in the `if` statement is false. The basic syntax of an `else` statement is as follows:
```
if (condition) {
    // code to be executed if condition is true
} else {
    // code to be executed if condition is false
}
```
3. **Nesting `if` and `else` statements**: `if` and `else` statements can be nested inside one another to test for multiple conditions. The basic syntax of nested `if` and `else` statements is as follows:
```
if (condition1) {
    // code to be executed if condition1 is true
} else if (condition2) {
    // code to be executed if condition1 is false and condition2 is true
} else {
    // code to be executed if both condition1 and condition2 are false
}
```
4. **The `switch` statement**: The `switch` statement is used to execute different code blocks based on the value of a variable or expression. The basic syntax of a `switch` statement is as follows:
```
switch (expression) {
    case value1:
        // code to be executed if expression == value1
        break;
    case value2:
        // code to be executed if expression == value2
        break;
    ...
    default:
        // code to be executed if expression does not match any case
}
```
The `break` statement is used to exit the `switch` statement and prevent the execution of the following cases. If the `break` statement is omitted, the program will continue to execute the following cases until a `break` statement is encountered or the end of the `switch` statement is reached.