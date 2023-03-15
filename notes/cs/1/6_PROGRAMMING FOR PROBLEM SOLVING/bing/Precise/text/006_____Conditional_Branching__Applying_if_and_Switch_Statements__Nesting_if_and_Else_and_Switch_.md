### Conditional Branching: Applying if and Switch Statements, Nesting if and Else and Switch

Conditional branching is a fundamental concept in programming that allows the program to execute different code blocks based on certain conditions. The two most common conditional branching statements are `if` and `switch`.

1. **if statement**: The `if` statement is used to execute a block of code if a specified condition is `true`. If the condition is `false`, the code block is skipped. The basic syntax of an `if` statement is as follows:
```
if (condition) {
    // code to be executed if condition is true
}
```
2. **else statement**: The `else` statement is used in conjunction with an `if` statement to execute a block of code if the condition in the `if` statement is `false`. The basic syntax of an `else` statement is as follows:
```
if (condition) {
    // code to be executed if condition is true
} else {
    // code to be executed if condition is false
}
```
3. **else if statement**: The `else if` statement is used to specify multiple conditions in an `if` statement. The basic syntax of an `else if` statement is as follows:
```
if (condition1) {
    // code to be executed if condition1 is true
} else if (condition2) {
    // code to be executed if condition2 is true
} else {
    // code to be executed if neither condition1 nor condition2 is true
}
```
4. **switch statement**: The `switch` statement is used to execute different code blocks based on the value of a variable or expression. The basic syntax of a `switch` statement is as follows:
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
5. **Nesting**: `if` and `else` statements, as well as `switch` statements, can be nested within one another to create more complex branching logic. For example:
```
if (condition1) {
    if (condition2) {
        // code to be executed if condition1 and condition2 are both true
    } else {
        // code to be executed if condition1 is true and condition2 is false
    }
} else {
    // code to be executed if condition1 is false
}
```

These are the basics of conditional branching using `if` and `switch` statements, as well as nesting `if` and `else` and `switch` statements. These statements allow for more complex and dynamic program behavior based on certain conditions. It is important to understand and apply these concepts when writing programs.