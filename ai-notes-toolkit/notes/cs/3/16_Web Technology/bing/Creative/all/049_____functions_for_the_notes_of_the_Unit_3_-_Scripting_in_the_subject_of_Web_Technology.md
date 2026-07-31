# Functions

Functions are reusable blocks of code that perform a specific task or calculate a value. Functions can take some input and return an output where there is some obvious relationship between the input and the output. Functions can also be called by other code to execute their task.

Some of the main concepts related to functions in web scripting are:

- **Function declaration**: A function declaration is a statement that defines a function with a name, a list of parameters, and a body. For example:

```javascript
function add(a, b) {
  return a + b;
}
```

- **Function expression**: A function expression is an expression that defines a function without a name, and assigns it to a variable or a property. For example:

```javascript
let add = function(a, b) {
  return a + b;
};
```

- **Function call**: A function call is an expression that invokes a function with a given set of arguments. For example:

```javascript
let sum = add(2, 3); // sum is 5
```

- **Function scope**: Function scope is the area of the code where a variable defined inside a function can be accessed. Variables defined inside a function cannot be accessed from anywhere outside the function, because the variable is only in the function's scope. For example:

```javascript
function add(a, b) {
  let result = a + b; // result is only in the function's scope
  return result;
}

console.log(result); // ReferenceError: result is not defined
```

- **Closures**: Closures are functions that can access variables from the outer scope, even after the outer function has returned. Closures are useful for creating private variables and maintaining state. For example:

```javascript
function makeCounter() {
  let count = 0; // count is a private variable
  return function() {
    count++; // count can be accessed by the inner function
    return count;
  };
}

let counter = makeCounter(); // counter is a closure
console.log(counter()); // 1
console.log(counter()); // 2
```

- **Function types**: JavaScript has four kinds of functions:

  - **Regular function**: can return anything; always runs to completion after invocation
  - **Generator function**: returns a Generator object; can be paused and resumed with the yield operator
  - **Async function**: returns a Promise; can be paused and resumed with the await operator
  - **Async generator function**: returns an AsyncGenerator object; both the await and yield operators can be used