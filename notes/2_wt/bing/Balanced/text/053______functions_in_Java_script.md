#### Functions in JavaScript

- A function is a block of code that performs a specific task and can be reused in different parts of a program.
- A function can have parameters, which are variables that receive values from the function caller.
- A function can also have a return value, which is the result of the function execution that can be used by the caller.
- To define a function, use the `function` keyword followed by the function name and a list of parameters in parentheses. The function body is enclosed in curly braces and contains the statements that implement the function logic.
- To call a function, use the function name followed by a list of arguments in parentheses. The arguments are the values that are passed to the function parameters.
- Example:

```javascript
// Define a function that calculates the area of a circle
function areaOfCircle(radius) {
  // Use the Math.PI constant and the power operator
  return Math.PI * radius ** 2;
}

// Call the function with different arguments
console.log(areaOfCircle(5)); // 78.53981633974483
console.log(areaOfCircle(10)); // 314.1592653589793
```

- A function can also be defined as an expression, which is a value that can be assigned to a variable or passed as an argument to another function. To define a function expression, use the `function` keyword without a function name and assign it to a variable. The function can then be called by using the variable name.
- Example:

```javascript
// Define a function expression that calculates the square of a number
var square = function(number) {
  return number * number;
};

// Call the function by using the variable name
console.log(square(3)); // 9
console.log(square(4)); // 16
```

- A function can also be defined as an arrow function, which is a shorter and more concise way of writing function expressions. To define an arrow function, use the `=>` operator after the list of parameters and before the function body. The function body can be a single expression or a block of statements. If the function body is a single expression, the `return` keyword is not needed and the result of the expression is returned automatically. If the function body is a block of statements, the `return` keyword is needed to return a value. If the function has only one parameter, the parentheses around the parameter can be omitted.
- Example:

```javascript
// Define an arrow function that calculates the cube of a number
var cube = number => number ** 3;

// Call the function by using the variable name
console.log(cube(2)); // 8
console.log(cube(3)); // 27
```