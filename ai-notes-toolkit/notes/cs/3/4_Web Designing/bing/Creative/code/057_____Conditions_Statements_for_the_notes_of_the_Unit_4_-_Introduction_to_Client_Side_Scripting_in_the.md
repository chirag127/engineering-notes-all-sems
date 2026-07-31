Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of conditional statements for the notes of the unit 4 - Introduction to Client Side Scripting in the subject of Web Designing.

### Conditional Statements

- Conditional statements are used to control the flow of execution of a program based on some conditions.
- The most common conditional statements are `if`, `if-else`, and `switch` statements.
- The `if` statement evaluates a condition and executes a block of code if the condition is true. For example:

```javascript
if (x > 10) {
  console.log("x is greater than 10");
}
```

- The `if-else` statement evaluates a condition and executes one block of code if the condition is true, and another block of code if the condition is false. For example:

```javascript
if (x > 10) {
  console.log("x is greater than 10");
} else {
  console.log("x is less than or equal to 10");
}
```

- The `switch` statement evaluates an expression and executes a block of code that matches the value of the expression. It can have multiple cases and a default case. For example:

```javascript
switch (x) {
  case 1:
    console.log("x is 1");
    break;
  case 2:
    console.log("x is 2");
    break;
  default:
    console.log("x is neither 1 nor 2");
    break;
}
```

- Conditional statements can be nested, meaning that one conditional statement can be inside another conditional statement. For example:

```javascript
if (x > 10) {
  if (x % 2 == 0) {
    console.log("x is an even number greater than 10");
  } else {
    console.log("x is an odd number greater than 10");
  }
} else {
  console.log("x is less than or equal to 10");
}
```

- Conditional statements can also be combined with logical operators, such as `&&` (and), `||` (or), and `!` (not), to form complex conditions. For example:

```javascript
if (x > 10 && x < 20) {
  console.log("x is between 10 and 20");
}

if (x == 1 || x == 2) {
  console.log("x is either 1 or 2");
}

if (!(x > 10)) {
  console.log("x is not greater than 10");
}
```