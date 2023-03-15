### JS Functions

- A function is a block of code that performs a specific task and can be reused in a program.
- A function can have parameters, which are variables that hold the values passed to the function when it is called.
- A function can also have a return value, which is the result of the function's execution that can be used by the caller.
- To define a function, use the `function` keyword followed by the function name and a list of parameters in parentheses. Then write the function body in curly braces.
- To call a function, use the function name followed by a list of arguments in parentheses. The arguments are the values that are passed to the function's parameters.
- Example:

```js
// Define a function that calculates the area of a circle
function areaOfCircle(radius) {
  // Use the Math.PI constant and the power operator (**)
  return Math.PI * radius ** 2;
}

// Call the function with different arguments
console.log(areaOfCircle(5)); // 78.53981633974483
console.log(areaOfCircle(10)); // 314.1592653589793
```

- A function can also be defined as an expression, which is a value that can be assigned to a variable or passed as an argument to another function.
- To define a function expression, use the `function` keyword followed by an optional function name and a list of parameters in parentheses. Then write the function body in curly braces.
- To call a function expression, use the variable name that holds the function value followed by a list of arguments in parentheses.
- Example:

```js
// Define a function expression that calculates the square of a number
var square = function (num) {
  return num ** 2;
};

// Call the function expression with different arguments
console.log(square(3)); // 9
console.log(square(4)); // 16
```

- A function can also be defined as an arrow function, which is a shorter and more concise way of writing function expressions.
- To define an arrow function, use a list of parameters in parentheses, followed by an arrow (`=>`) and the function body. If the function body is a single expression, the curly braces and the `return` keyword can be omitted.
- To call an arrow function, use the variable name that holds the function value followed by a list of arguments in parentheses.
- Example:

```js
// Define an arrow function that calculates the cube of a number
var cube = (num) => num ** 3;

// Call the arrow function with different arguments
console.log(cube(2)); // 8
console.log(cube(3)); // 27
```