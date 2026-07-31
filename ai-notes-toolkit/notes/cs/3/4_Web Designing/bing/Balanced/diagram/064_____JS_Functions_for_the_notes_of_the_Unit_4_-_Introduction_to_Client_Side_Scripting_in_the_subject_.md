Hello, I am Sydney, your AI assistant. I can help you with your study material for Web Designing. Here are some notes on JS Functions for Unit 4 - Introduction to Client Side Scripting.

### JS Functions

- A function is a block of code that performs a specific task and can be reused in a program.
- A function can have parameters, which are variables that receive values from the function caller.
- A function can also return a value to the function caller, using the return statement.
- To define a function, use the function keyword, followed by the function name, parentheses, and the function body enclosed in curly braces.

```js
// Example of a function definition
function add(x, y) {
  // x and y are parameters
  var sum = x + y; // sum is a local variable
  return sum; // return the value of sum
}
```

- To call a function, use the function name, followed by parentheses, and optionally, arguments that match the parameters.

```js
// Example of a function call
var result = add(3, 5); // result is a global variable
console.log(result); // prints 8
```

- A function can be declared anywhere in the code, but it is recommended to declare it before using it.
- A function can also be assigned to a variable or passed as an argument to another function. This is called a function expression.

```js
// Example of a function expression
var multiply = function(x, y) {
  // multiply is a variable that holds a function
  return x * y;
};

var product = multiply(4, 6); // product is a global variable
console.log(product); // prints 24
```

- A function can also be defined using an arrow syntax, which is a shorter way of writing a function expression. This is called an arrow function.

```js
// Example of an arrow function
var divide = (x, y) => {
  // divide is a variable that holds a function
  return x / y;
};

var quotient = divide(12, 4); // quotient is a global variable
console.log(quotient); // prints 3
```

- A function can have default values for its parameters, which are used when the function is called without arguments or with undefined arguments.

```js
// Example of a function with default parameters
function greet(name = "Anonymous", message = "Hello") {
  // name and message are parameters with default values
  console.log(message + ", " + name + "!");
}

greet(); // prints Hello, Anonymous!
greet("Sydney"); // prints Hello, Sydney!
greet("Sydney", "Welcome"); // prints Welcome, Sydney!
greet(undefined, "Goodbye"); // prints Goodbye, Anonymous!
```

- A function can have a rest parameter, which is a special parameter that can hold any number of arguments as an array. The rest parameter must be the last parameter in the function definition.

```js
// Example of a function with a rest parameter
function sum(...numbers) {
  // numbers is a rest parameter that holds an array of arguments
  var total = 0;
  for (var num of numbers) {
    // loop through the array of arguments
    total += num; // add each argument to the total
  }
  return total; // return the total
}

console.log(sum(1, 2, 3)); // prints 6
console.log(sum(4, 5, 6, 7)); // prints 22
console.log(sum()); // prints 0
```