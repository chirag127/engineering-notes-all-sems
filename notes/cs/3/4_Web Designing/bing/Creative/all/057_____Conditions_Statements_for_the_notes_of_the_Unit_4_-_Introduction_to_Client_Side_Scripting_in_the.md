# Conditional Statements

Conditional statements are used to control the flow of execution in a program based on some conditions. They allow the program to make decisions and perform different actions depending on whether the conditions are true or false.

## Types of Conditional Statements

There are two main types of conditional statements in client-side scripting:

- **if...else** statement: This statement executes a block of code if a specified condition is true, and optionally executes another block of code if the condition is false. It has the following syntax:

```javascript
if (condition) {
  // code to execute if condition is true
} else {
  // code to execute if condition is false
}
```

- **switch** statement: This statement evaluates an expression and compares it with multiple cases. It executes the code associated with the matching case, and optionally executes a default code if no case matches. It has the following syntax:

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
    // code to execute if no case matches
}
```

## Examples of Conditional Statements

Here are some examples of how to use conditional statements in client-side scripting:

- **if...else** statement: Suppose we want to display a message to the user based on their age. We can use the following code:

```javascript
var age = prompt("Enter your age"); // ask the user to enter their age
if (age >= 18) {
  alert("You are an adult"); // display this message if age is greater than or equal to 18
} else {
  alert("You are a minor"); // display this message if age is less than 18
}
```

- **switch** statement: Suppose we want to display a different greeting to the user based on the day of the week. We can use the following code:

```javascript
var day = new Date().getDay(); // get the current day of the week (0 for Sunday, 1 for Monday, etc.)
switch (day) {
  case 0:
    alert("Happy Sunday!"); // display this message if day is 0
    break;
  case 1:
    alert("Have a nice Monday!"); // display this message if day is 1
    break;
  case 2:
    alert("Enjoy your Tuesday!"); // display this message if day is 2
    break;
  case 3:
    alert("Welcome to Wednesday!"); // display this message if day is 3
    break;
  case 4:
    alert("It's Thursday already!"); // display this message if day is 4
    break;
  case 5:
    alert("Finally Friday!"); // display this message if day is 5
    break;
  case 6:
    alert("Hello Saturday!"); // display this message if day is 6
    break;
  default:
    alert("Invalid day"); // display this message if no case matches
}
```

## References

: Client-Side JavaScript Guide - Oracle. https://docs.oracle.com/cd/E19957-01/816-6409-10/stmtsov.htm
: JavaScript Conditional Statements | Client Side Scripting | Online ... https://www.onlinenotesnepal.com/java-script-conditional-statements
: Making decisions in your code — conditionals - Mozilla. https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/conditionals
: Web API Conditional Operations Sample (Client-side JavaScript). https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/samples/conditional-operations-client-side-javascript
: Dynamic client-side scripting - Learn web development | MDN - Mozilla. https://developer.mozilla.org/en-US/docs/Learn/JavaScript