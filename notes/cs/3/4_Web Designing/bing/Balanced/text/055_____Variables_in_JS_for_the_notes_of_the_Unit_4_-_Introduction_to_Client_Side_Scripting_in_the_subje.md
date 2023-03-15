### Variables in JS

- A variable is a named container that can store a value of a certain type, such as a number, a string, a boolean, an array, an object, or a function.
- Variables are declared using the keywords `var`, `let`, or `const`, followed by the variable name and an optional assignment operator and initial value.
- Example: `var x = 10;` declares a variable named `x` and assigns it the value `10`.
- The keyword `var` creates a function-scoped or globally-scoped variable, depending on where it is declared. It can be redeclared and reassigned within the same scope.
- The keyword `let` creates a block-scoped variable, which means it is only accessible within the nearest enclosing curly braces. It can be reassigned but not redeclared within the same scope.
- The keyword `const` creates a block-scoped variable that cannot be reassigned or redeclared. It must be initialized with a value when it is declared.
- Example: 

```js
function foo() {
  var a = 1; // function-scoped variable
  let b = 2; // block-scoped variable
  const c = 3; // block-scoped constant
  if (true) {
    var a = 4; // redeclares and reassigns a
    let b = 5; // reassigns b
    const c = 6; // creates a new block-scoped constant
    console.log(a, b, c); // 4, 5, 6
  }
  console.log(a, b, c); // 4, 2, 3
}
foo();
```
- Variables can be accessed by using their names, as long as they are in scope. If a variable is not in scope, or has not been declared, an error will be thrown.
- Variables can be manipulated by using operators, such as arithmetic, assignment, comparison, logical, or bitwise operators. Operators can change the value or type of a variable, or perform some operation on it and return a new value.
- Example: `x += 5;` adds `5` to the value of `x` and assigns the result back to `x`.
- Variables can also be passed as arguments to functions, or returned as values from functions. Functions can create local variables that are only accessible within the function body, or use global variables that are accessible from anywhere in the code.
- Example: 

```js
var x = 10; // global variable
function add(y) { // y is a local variable and a parameter
  var z = x + y; // z is a local variable
  return z; // returns the value of z
}
console.log(add(5)); // 15
console.log(z); // error: z is not defined
```