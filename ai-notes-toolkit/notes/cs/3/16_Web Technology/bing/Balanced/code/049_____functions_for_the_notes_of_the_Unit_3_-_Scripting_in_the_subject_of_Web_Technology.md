### Functions

- A function is a block of code that performs a specific task and can be reused in a program.
- A function can have zero or more parameters that are passed as input values and can return zero or more values as output.
- A function can be defined using the `function` keyword followed by the function name and a list of parameters in parentheses.
- A function can be called by using the function name followed by a list of arguments in parentheses that match the parameters of the function.
- A function can be declared before or after the code that calls it, as long as the function name is in scope.
- A function can be assigned to a variable or passed as an argument to another function.
- A function can be nested inside another function and have access to the variables and parameters of the outer function.
- A function can be anonymous, meaning it does not have a name and is usually used as a callback or a closure.

Example of a function definition and a function call in JavaScript:

```javascript
// Define a function that calculates the area of a rectangle
function area(length, width) {
  return length * width;
}

// Call the function with two arguments and store the result in a variable
var result = area(10, 5);

// Print the result to the console
console.log(result); // 50
```