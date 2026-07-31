# JS Functions

- A function is a block of code that performs a specific task and can be reused in a program.
- A function can have zero or more parameters that receive values from the function caller.
- A function can return a value to the function caller using the `return` statement.
- A function can be defined using a function declaration, a function expression, or an arrow function.

## Function Declaration

- A function declaration is a statement that defines a function using the `function` keyword, followed by the function name, a list of parameters in parentheses, and a block of code in curly braces.
- A function declaration can be placed anywhere in the code and can be called before or after it is defined.
- Example:

```js
// Function declaration
function add(a, b) {
  return a + b;
}

// Function call
let sum = add(3, 5); // sum is 8
```

## Function Expression

- A function expression is an expression that defines a function using the `function` keyword, optionally followed by a function name, a list of parameters in parentheses, and a block of code in curly braces.
- A function expression can be assigned to a variable, passed as an argument to another function, or returned from another function.
- A function expression can only be called after it is defined.
- Example:

```js
// Function expression
let multiply = function (a, b) {
  return a * b;
};

// Function call
let product = multiply(3, 5); // product is 15
```

## Arrow Function

- An arrow function is a concise way of defining a function using the `=>` operator, followed by a list of parameters in parentheses, and a block of code or an expression in curly braces or parentheses.
- An arrow function does not have its own `this`, `arguments`, `super`, or `new.target` values and inherits them from the enclosing scope.
- An arrow function cannot be used as a constructor or a generator function.
- Example:

```js
// Arrow function
let subtract = (a, b) => {
  return a - b;
};

// Function call
let difference = subtract(3, 5); // difference is -2
```