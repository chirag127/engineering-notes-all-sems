Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of conditional statements for the notes of the unit 4 - Introduction to Client Side Scripting in the subject of Web Designing.

### Conditional Statements

- Conditional statements are used to control the flow of execution of a program based on some conditions.
- The most common conditional statements are `if`, `if-else`, and `switch` statements.
- The `if` statement evaluates a condition and executes a block of code if the condition is true.
- The `if-else` statement evaluates a condition and executes one block of code if the condition is true, and another block of code if the condition is false.
- The `switch` statement evaluates an expression and executes a block of code that matches the value of the expression among a set of cases.
- Conditional statements can be nested, meaning that one conditional statement can be inside another conditional statement.
- Conditional statements can be combined with logical operators, such as `&&` (and), `||` (or), and `!` (not), to form complex conditions.

#### Syntax and Examples

- The syntax of the `if` statement is:

```javascript
if (condition) {
  // code to execute if condition is true
}
```

- For example:

```javascript
var age = 18;
if (age >= 18) {
  console.log("You are an adult.");
}
```

- The syntax of the `if-else` statement is:

```javascript
if (condition) {
  // code to execute if condition is true
} else {
  // code to execute if condition is false
}
```

- For example:

```javascript
var age = 16;
if (age >= 18) {
  console.log("You are an adult.");
} else {
  console.log("You are a minor.");
}
```

- The syntax of the `switch` statement is:

```javascript
switch (expression) {
  case value1:
    // code to execute if expression matches value1
    break;
  case value2:
    // code to execute if expression matches value2
    break;
  // ...
  default:
    // code to execute if expression does not match any case
    break;
}
```

- For example:

```javascript
var day = 3;
switch (day) {
  case 1:
    console.log("Monday");
    break;
  case 2:
    console.log("Tuesday");
    break;
  case 3:
    console.log("Wednesday");
    break;
  case 4:
    console.log("Thursday");
    break;
  case 5:
    console.log("Friday");
    break;
  case 6:
    console.log("Saturday");
    break;
  case 7:
    console.log("Sunday");
    break;
  default:
    console.log("Invalid day");
    break;
}
```