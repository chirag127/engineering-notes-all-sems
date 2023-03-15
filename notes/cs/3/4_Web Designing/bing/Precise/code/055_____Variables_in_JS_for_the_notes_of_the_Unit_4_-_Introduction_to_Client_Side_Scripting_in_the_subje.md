### Variables in JS

Variables are used to store data values in JavaScript. They are declared using the `var`, `let`, or `const` keyword, followed by the variable name.

- `var`: used to declare a variable with a function scope or global scope.
- `let`: used to declare a variable with a block scope.
- `const`: used to declare a constant variable with a block scope.

Example:
```javascript
var x = 10; // function or global scope
let y = 20; // block scope
const z = 30; // block scope, constant value
```

Variables can store different data types, such as numbers, strings, and objects. The value of a variable can be changed, except for `const` variables, which cannot be reassigned.

Example:
```javascript
var a = 5; // number
var b = "Hello"; // string
var c = {name: "John", age: 25}; // object

a = 10; // changing the value of a
b = "World"; // changing the value of b
// c = {name: "Jane", age: 30}; // error, cannot reassign a const variable
```

It is important to choose meaningful and descriptive variable names to make the code easier to read and understand.