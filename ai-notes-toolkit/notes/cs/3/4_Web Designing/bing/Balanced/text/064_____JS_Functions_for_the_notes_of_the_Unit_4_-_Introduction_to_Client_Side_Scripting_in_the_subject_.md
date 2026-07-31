### JS Functions

- A function is a block of code that performs a specific task and can be reused in a program.
- A function can have parameters, which are variables that receive values from the function caller.
- A function can also return a value to the function caller, using the return statement.
- To define a function, use the function keyword, followed by the function name, parentheses, and curly braces.
- To call a function, use the function name, followed by parentheses, and optionally pass arguments that match the parameters.
- Example:

```javascript
// Define a function that calculates the area of a circle
function areaOfCircle(radius) {
  // Use the Math.PI constant and the power operator
  return Math.PI * radius ** 2;
}

// Call the function and store the result in a variable
let area = areaOfCircle(5);

// Display the result
console.log("The area of the circle is " + area);
```

- A function can be declared before or after it is called, because JavaScript hoists function declarations to the top of the scope.
- A function can also be defined as an expression, by assigning an anonymous function to a variable or a constant.
- A function expression is not hoisted, so it must be defined before it is called.
- Example:

```javascript
// Define a function expression that calculates the perimeter of a rectangle
const perimeterOfRectangle = function (length, width) {
  // Use the addition and multiplication operators
  return 2 * (length + width);
};

// Call the function expression and store the result in a variable
let perimeter = perimeterOfRectangle(10, 5);

// Display the result
console.log("The perimeter of the rectangle is " + perimeter);
```

- A function can also be defined using an arrow syntax, which is a shorter and more concise way of writing function expressions.
- An arrow function does not have its own this value, so it is useful for writing callbacks and event handlers.
- Example:

```javascript
// Define an arrow function that calculates the volume of a cube
const volumeOfCube = (side) => {
  // Use the power and multiplication operators
  return side ** 3;
};

// Call the arrow function and store the result in a variable
let volume = volumeOfCube(3);

// Display the result
console.log("The volume of the cube is " + volume);
```