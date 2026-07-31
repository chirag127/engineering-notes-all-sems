Hello, I am Sydney, your AI assistant. I can help you with your notes on web designing. Here is the content for the topic of variables in JS for the unit 4 - Introduction to Client Side Scripting.

### Variables in JS

- A variable is a named container that can store a value of a certain type, such as a number, a string, a boolean, an array, an object, or a function.
- Variables are declared using the keywords `var`, `let`, or `const`, followed by the variable name and an optional assignment operator and initial value.
- Example: `var x = 10;` declares a variable named `x` and assigns it the value `10`.
- The scope of a variable determines where it can be accessed and modified in the code. Variables declared with `var` have either global scope or function scope, meaning they can be accessed anywhere in the global context or within the function where they are declared. Variables declared with `let` or `const` have block scope, meaning they can only be accessed within the block (a set of curly braces) where they are declared.
- Example: 

```js
var a = 1; // global scope
function foo() {
  var b = 2; // function scope
  if (true) {
    let c = 3; // block scope
    const d = 4; // block scope
    console.log(a, b, c, d); // 1, 2, 3, 4
  }
  console.log(a, b, c, d); // 1, 2, ReferenceError: c is not defined, ReferenceError: d is not defined
}
console.log(a, b, c, d); // 1, ReferenceError: b is not defined, ReferenceError: c is not defined, ReferenceError: d is not defined
```

- The value of a variable can be changed by assigning a new value to it, unless it is declared with `const`, which means it cannot be reassigned.
- Example: `x = 20;` changes the value of `x` from `10` to `20`, but `const y = 30; y = 40;` throws a TypeError: Assignment to constant variable.
- Variables can be used in expressions, statements, and functions to perform calculations, store data, and control the flow of the program.