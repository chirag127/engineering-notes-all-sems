# Unit 4 - Introduction to Client Side Scripting: JS Functions

Functions are one of the fundamental building blocks in JavaScript. A function is a set of statements that performs a specific task and can be reused throughout the code.

- **Defining a function**: A function is defined using the `function` keyword, followed by the function name, a list of parameters enclosed in parentheses, and the function body enclosed in curly braces.

```javascript
function functionName(parameter1, parameter2) {
    // function body
}
```

- **Calling a function**: A function is called by using its name followed by the arguments enclosed in parentheses.

```javascript
functionName(argument1, argument2);
```

- **Function parameters**: Function parameters are the names listed in the function definition. They act as placeholders for the values that will be passed to the function when it is called.

- **Function arguments**: Function arguments are the values passed to the function when it is called. The number of arguments passed to the function must match the number of parameters defined in the function.

- **Return value**: A function can return a value using the `return` statement. The value returned by the function can be used in the calling code.

```javascript
function add(a, b) {
    return a + b;
}

let sum = add(1, 2); // sum is 3
```

- **Function scope**: Variables defined inside a function are local to the function and cannot be accessed outside the function. Variables defined outside the function are global and can be accessed by any code in the program.

- **Anonymous functions**: An anonymous function is a function without a name. Anonymous functions are often used as arguments to other functions or as the value of a variable.

```javascript
let myFunction = function() {
    // function body
}
```

- **Arrow functions**: Arrow functions are a shorthand way of writing functions using the `=>` syntax. They are particularly useful for writing short, single-expression functions.

```javascript
let myFunction = (a, b) => a + b;
```

These are some of the key concepts related to JavaScript functions. Understanding these concepts is essential for working with client-side scripting in web designing.