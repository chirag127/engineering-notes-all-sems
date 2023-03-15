### JS Functions

- A function is a block of code that performs a specific task and can be reused in a program.
- A function can have parameters, which are variables that receive values from the function caller.
- A function can also return a value to the function caller, using the `return` statement.
- To define a function, use the `function` keyword, followed by the function name, parentheses, and curly braces.
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

// Print the result
console.log(area); // 78.53981633974483
```

- A function can also be defined as an expression, by assigning an anonymous function (a function without a name) to a variable or a constant.
- A function expression can be useful when passing a function as an argument to another function, or when using a function as a property of an object.
- Example:

```javascript
// Define a function expression that calculates the square of a number
const square = function (num) {
  return num * num;
};

// Call the function expression and print the result
console.log(square(4)); // 16

// Define an object with a function expression as a property
let calculator = {
  add: function (a, b) {
    return a + b;
  },
  subtract: function (a, b) {
    return a - b;
  },
};

// Call the function expression as a property of the object
console.log(calculator.add(3, 2)); // 5
console.log(calculator.subtract(3, 2)); // 1
```

- A function can also be defined using an arrow notation, which is a shorter and more concise way of writing a function expression.
- An arrow function has the following syntax: `(parameters) => { body }`
- If the function has only one parameter, the parentheses can be omitted.
- If the function has only one statement in the body, the curly braces and the `return` keyword can be omitted.
- Example:

```javascript
// Define an arrow function that doubles a number
let double = (num) => {
  return num * 2;
};

// Call the arrow function and print the result
console.log(double(6)); // 12

// Define an arrow function that triples a number, without parentheses
let triple = num => {
  return num * 3;
};

// Call the arrow function and print the result
console.log(triple(6)); // 18

// Define an arrow function that adds two numbers, without curly braces and return
let add = (a, b) => a + b;

// Call the arrow function and print the result
console.log(add(6, 4)); // 10
```

- A function can have default values for its parameters, which are used when the function is called without passing arguments for those parameters.
- To specify a default value for a parameter, use the assignment operator (`=`) after the parameter name, followed by the default value.
- Example:

```javascript
// Define a function that greets a person, with a default value for the name parameter
function greet(name = "stranger") {
  // Use a template literal to interpolate the name
  console.log(`Hello, ${name}!`);
}

// Call the function without passing an argument
greet(); // Hello, stranger!

// Call the function with passing an argument
greet("Sydney"); // Hello, Sydney!
```

- A function can have a rest parameter, which is a special parameter that can accept any number of arguments as an array.
- To specify a rest parameter, use the spread operator (`...`) before the parameter name.
- A rest parameter must be the last parameter in the function definition.
- Example:

```javascript
// Define a function that calculates the sum of any number of numbers
function sum(...nums) {
  // Use the reduce method to iterate over the array and add the numbers
  return nums.reduce((total, num) => total + num, 0);
}

// Call the function with different number of arguments
console.log(sum(1, 2, 3)); // 6
console.log(sum(4, 5)); // 9
console.log(sum(6)); // 6
console.log(sum()); // 0
```