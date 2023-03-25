### Variables in JS

JavaScript is a dynamic programming language that allows developers to define and manipulate variables. Variables are used to store values, such as numbers or strings, that can be used later in the program. In this section, we will learn about variables in JavaScript.

#### Declaring Variables

In JavaScript, variables are declared using the `var` keyword. For example, to declare a variable called `myVariable`, we could write:

```js
var myVariable;
```

#### Initializing Variables

Variables can also be initialized with a value at the time of declaration. For example:

```js
var myVariable = 10;
```

In this case, `myVariable` is initialized with the value `10`.

#### Data Types

JavaScript supports several data types, including:

- Numbers: e.g. `10`, `3.14`
- Strings: e.g. `"Hello, world!"`, `'JavaScript'`
- Booleans: `true`, `false`
- Null: `null`
- Undefined: `undefined`
- Objects: `{key: value}`
- Arrays: `['apple', 'banana', 'orange']`

Variables can hold any of these data types.

#### Naming Conventions

When naming variables in JavaScript, there are a few rules to follow:

- Variable names must begin with a letter, underscore (`_`), or dollar sign (`$`).
- Variable names can contain letters, numbers, underscores, and dollar signs.
- Variable names are case sensitive.
- Variable names should be descriptive and meaningful.

#### Scope

In JavaScript, variables have either global or local scope. Global variables are declared outside of any function, while local variables are declared inside a function.

#### Example

```js
var x = 10; // global variable

function myFunction() {
  var y = 20; // local variable
  console.log(x + y); // output: 30
}

myFunction();
console.log(x + y); // ReferenceError: y is not defined
```

In this example, `x` is a global variable and is accessible inside and outside of the function. `y` is a local variable and is only accessible inside the function.

#### Conclusion

Variables are an important concept in JavaScript and are essential for writing dynamic programs. By understanding how to declare, initialize, and use variables, you will be able to create complex programs that can respond to user input and manipulate data on the fly.