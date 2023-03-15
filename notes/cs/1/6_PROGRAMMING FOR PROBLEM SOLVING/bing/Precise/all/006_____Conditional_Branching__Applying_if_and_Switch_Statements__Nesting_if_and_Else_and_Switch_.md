### Conditional Branching: Applying if and Switch Statements, Nesting if and Else and Switch

Conditional branching is a fundamental concept in programming that allows the program to execute different code blocks based on certain conditions. The two most common conditional branching statements are `if` and `switch`.

- `if` statement: The `if` statement is used to execute a block of code if a specified condition is true. If the condition is false, the code block is skipped. The basic syntax of an `if` statement is as follows:
```
if (condition) {
  // code to be executed if condition is true
}
```
- `else` statement: The `else` statement is used in conjunction with an `if` statement to specify a block of code to be executed if the condition in the `if` statement is false. The basic syntax of an `else` statement is as follows:
```
if (condition) {
  // code to be executed if condition is true
} else {
  // code to be executed if condition is false
}
```
- `else if` statement: The `else if` statement is used to specify multiple conditions in an `if` statement. If the first condition is false, the program checks the next `else if` condition, and so on. The basic syntax of an `else if` statement is as follows:
```
if (condition1) {
  // code to be executed if condition1 is true
} else if (condition2) {
  // code to be executed if condition2 is true
} else {
  // code to be executed if all conditions are false
}
```
- `switch` statement: The `switch` statement is used to execute different code blocks based on the value of a variable or expression. The basic syntax of a `switch` statement is as follows:
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
- Nesting: It is possible to nest `if` and `else` statements, as well as `switch` statements, within each other to create more complex conditional branching structures.

These conditional branching statements allow for greater flexibility and control in the flow of a program, allowing it to make decisions and execute different code blocks based on certain conditions. It is important to use these statements correctly and efficiently to create well-structured and readable code.