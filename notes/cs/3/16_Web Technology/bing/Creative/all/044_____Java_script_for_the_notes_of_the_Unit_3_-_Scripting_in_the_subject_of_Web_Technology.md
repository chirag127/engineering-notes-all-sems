# JavaScript for the notes of the Unit 3 - Scripting in the subject of Web Technology

## Introduction

JavaScript is a scripting language that can be used to create dynamic and interactive web pages. It can run on both the client-side and the server-side, depending on the environment. JavaScript is based on the ECMAScript standard, which defines the core features and syntax of the language. JavaScript also supports object-oriented, imperative, and declarative programming paradigms.

## Basics

Some of the basic concepts and features of JavaScript are:

- **Variables**: Variables are containers that store values of different data types, such as strings, numbers, booleans, arrays, objects, etc. Variables can be declared using the keywords `var`, `let`, or `const`, depending on the scope and mutability of the variable. For example:

```javascript
var name = "John"; // A global variable that can be changed
let age = 25; // A block-scoped variable that can be changed
const pi = 3.14; // A block-scoped variable that cannot be changed
```

- **Operators**: Operators are symbols that perform operations on one or more values (or operands) and produce a result. JavaScript supports various types of operators, such as arithmetic, assignment, comparison, logical, bitwise, string, ternary, etc. For example:

```javascript
var x = 10; // Assignment operator
var y = x + 5; // Arithmetic operator
var z = x == y; // Comparison operator
var w = x && y; // Logical operator
var v = x << 1; // Bitwise operator
var u = x > 10 ? "Yes" : "No"; // Ternary operator
var s = "Hello" + "World"; // String operator
```

- **Conditionals**: Conditionals are statements that execute different blocks of code based on certain conditions. JavaScript supports the `if...else` statement, the `switch` statement, and the `try...catch` statement for error handling. For example:

```javascript
var score = 80;
if (score >= 90) {
  console.log("A grade");
} else if (score >= 80) {
  console.log("B grade");
} else if (score >= 70) {
  console.log("C grade");
} else {
  console.log("Fail");
}

var day = "Monday";
switch (day) {
  case "Monday":
    console.log("First day of the week");
    break;
  case "Tuesday":
    console.log("Second day of the week");
    break;
  // Other cases
  default:
    console.log("Invalid day");
}

var num = 0;
try {
  var result = 10 / num;
  console.log(result);
} catch (error) {
  console.log("Division by zero error");
}
```

- **Loops**: Loops are statements that repeat a block of code until a certain condition is met. JavaScript supports the `for` loop, the `while` loop, the `do...while` loop, and the `for...in` loop for iterating over objects. For example:

```javascript
for (var i = 0; i < 10; i++) {
  console.log(i);
}

var j = 0;
while (j < 10) {
  console.log(j);
  j++;
}

var k = 0;
do {
  console.log(k);
  k++;
} while (k < 10);

var obj = {name: "Alice", age: 20, city: "New York"};
for (var key in obj) {
  console.log(key + ": " + obj[key]);
}
```

- **Functions**: Functions are blocks of code that can be defined and invoked to perform a specific task. Functions can have parameters and return values. Functions can be declared using the `function` keyword, or as expressions or arrow functions. For example:

```javascript
// Function declaration
function add(a, b) {
  return a + b;
}

// Function expression
var subtract = function(a, b) {
  return a - b;
}

// Arrow function
var multiply = (a, b) => {
  return a * b;
}

// Function invocation
var x = add(2, 3); // x = 5
var y = subtract(5, 2); // y = 3
var z = multiply(2, 3); // z = 6
```

- **Arrays**: Arrays are objects that store