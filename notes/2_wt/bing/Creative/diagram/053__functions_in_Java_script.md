A function in JavaScript is a block of code that performs a specific task or calculates a value. It can take some input as parameters and return an output. A function can be defined with the function keyword, followed by a name, followed by parentheses that contain the parameters, followed by a block of code that defines the function body. For example:

function add (a, b) {
  return a + b;
}

This function takes two parameters, a and b, and returns their sum. To invoke or call a function, you use the function name followed by parentheses that contain the arguments, which are the values you pass to the function. For example:

let result = add (3, 5); // result is 8

You can also define a function as an expression, which means assigning it to a variable or a constant. For example:

const multiply = function (a, b) {
  return a * b;
};

This function is anonymous, meaning it has no name. You can invoke it by using the variable name followed by the arguments. For example:

let result = multiply (3, 5); // result is 15

Functions can also be nested, meaning that a function can contain another function inside it. For example:

function outer (x) {
  function inner (y) {
    return y + 1;
  }
  return inner (x) * 2;
}

This function has an inner function that takes a parameter y and returns y + 1. The outer function takes a parameter x and returns the result of calling the inner function with x, multiplied by 2. For example:

let result = outer (3); // result is 8

#### Functions in JavaScript

The following diagram illustrates the basic structure of a function in JavaScript:

```
+-----------------+
| function name   |
| (parameters)    |
+-----------------+
|                 |
| function body   |
|                 |
| return value    |
|                 |
+-----------------+
```

The function name is optional, depending on whether the function is a declaration or an expression. The parameters are the names of the variables that the function expects as input. The function body is the block of code that defines what the function does. The return value is the output of the function, which can be any data type. The return statement is used to specify the return value, and it also ends the execution of the function. If there is no return statement, the function returns undefined by default.