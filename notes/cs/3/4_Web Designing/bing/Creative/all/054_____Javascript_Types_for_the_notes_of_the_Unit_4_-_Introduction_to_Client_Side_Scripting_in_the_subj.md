# JavaScript Types

JavaScript is a dynamic, multi-paradigm, single-threaded programming language that supports object-oriented, imperative, and declarative styles. JavaScript has 8 basic data types :

- **undefined**: The type undefined has one value, undefined, which indicates that a variable has not been assigned a value.
- **null**: The type null has one value, null, which represents the intentional absence of any object value.
- **boolean**: The type boolean has two values, true and false, which are used for logical operations.
- **number**: The type number represents both integer and floating-point numbers. There are many operations for numbers, e.g. multiplication *, division /, addition +, subtraction -, and so on.
- **bigint**: The type bigint represents integer numbers of arbitrary length. It can store numbers that are too large for the number type.
- **string**: The type string represents a sequence of characters. A string may have zero or more characters, there’s no separate single-character type. Strings are enclosed in quotes, either single or double.
- **symbol**: The type symbol represents a unique identifier that can be used as a property key in objects. Symbols are created by calling the Symbol() function.
- **object**: The type object represents a collection of data and/or functionality. Objects can contain other objects, arrays, functions, dates, etc. Objects are created by using curly braces {} or the new keyword .

Here is an example of declaring variables of different types in JavaScript:

```javascript
// undefined
let x;

// null
let y = null;

// boolean
let z = true;

// number
let a = 42;

// bigint
let b = 1234567890123456789012345678901234567890n;

// string
let c = "Hello, world!";

// symbol
let d = Symbol("id");

// object
let e = {
  name: "Alice",
  age: 25,
  greet: function() {
    console.log("Hi, I'm " + this.name);
  }
};
```