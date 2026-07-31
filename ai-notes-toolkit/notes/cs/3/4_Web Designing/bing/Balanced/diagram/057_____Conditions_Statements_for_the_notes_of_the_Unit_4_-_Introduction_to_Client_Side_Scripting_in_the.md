### Conditional Statements

Conditional statements are used to perform different actions based on different conditions. They allow the client-side script to make decisions and execute different blocks of code depending on the result of a logical expression.

There are two main types of conditional statements in client-side scripting:

- **if...else** statement: This statement executes one block of code if the condition is true, and another block of code if the condition is false. It can also have multiple else if clauses to check for more than two conditions.

- **switch** statement: This statement executes one of many blocks of code based on the value of an expression. It can also have a default clause to execute if none of the cases match the expression.

#### Syntax and Examples

The syntax of the if...else statement is:

```javascript
if (condition) {
  // code to execute if condition is true
} else {
  // code to execute if condition is false
}
```

The condition can be any expression that evaluates to a boolean value (true or false). The else clause is optional and can be omitted if there is no code to execute if the condition is false.

For example:

```javascript
var age = 18;
if (age >= 18) {
  console.log("You are an adult.");
} else {
  console.log("You are a minor.");
}
```

The output of this code will be "You are an adult." if the value of age is 18 or more, and "You are a minor." if the value of age is less than 18.

The syntax of the switch statement is:

```javascript
switch (expression) {
  case value1:
    // code to execute if expression matches value1
    break;
  case value2:
    // code to execute if expression matches value2
    break;
  ...
  default:
    // code to execute if expression does not match any case
    break;
}
```

The expression can be any value or variable. The case clauses compare the expression with different values using strict equality (===). The break statement is used to exit the switch statement after executing the code for the matching case. The default clause is optional and can be omitted if there is no code to execute if the expression does not match any case.

For example:

```javascript
var color = "red";
switch (color) {
  case "red":
    console.log("The color is red.");
    break;
  case "blue":
    console.log("The color is blue.");
    break;
  case "green":
    console.log("The color is green.");
    break;
  default:
    console.log("The color is unknown.");
    break;
}
```

The output of this code will be "The color is red." if the value of color is "red", "The color is blue." if the value of color is "blue", "The color is green." if the value of color is "green", and "The color is unknown." if the value of color is anything else.