### JavaScript for the notes of the Unit 3 - Scripting in the subject of Web Technology

- JavaScript is a **scripting language** that can be used to create dynamic and interactive web pages. It can run on both the **client-side** and the **server-side** of a web application .
- JavaScript is a **multi-paradigm** language, meaning it supports different programming styles, such as **object-oriented**, **imperative**, and **declarative** (e.g. functional programming) .
- JavaScript has a **standard library** of built-in objects, such as **Array**, **Date**, and **Math**, and a **core set** of language elements, such as **operators**, **control structures**, and **statements** .
- JavaScript can interact with the **browser** and its **Document Object Model (DOM)**, which is a representation of the web page content and structure. JavaScript can manipulate the DOM to change the web page dynamically  .
- JavaScript follows the **ECMAScript** standard, which defines the syntax and features of the language. The latest version of ECMAScript is **ES2020** .

Some of the basic concepts of JavaScript are:

- **Variables**: Variables are containers that store values. They can be declared with the keywords **var**, **let**, or **const**, depending on the scope and mutability of the variable. For example:

```javascript
var name = "John"; // a global variable that can be changed
let age = 25; // a block-scoped variable that can be changed
const pi = 3.14; // a block-scoped variable that cannot be changed
```

- **Operators**: Operators are symbols that perform operations on values or variables. They can be classified into different types, such as **arithmetic**, **assignment**, **comparison**, **logical**, **bitwise**, **string**, and **ternary** operators. For example:

```javascript
x + y // addition
x - y // subtraction
x * y // multiplication
x / y // division
x % y // modulus (remainder)
x ** y // exponentiation
x = y // assignment
x == y // equality
x != y // inequality
x === y // strict equality
x !== y // strict inequality
x < y // less than
x > y // greater than
x <= y // less than or equal to
x >= y // greater than or equal to
x && y // logical and
x || y // logical or
!x // logical not
x & y // bitwise and
x | y // bitwise or
x ^ y // bitwise xor
~x // bitwise not
x << y // bitwise left shift
x >> y // bitwise right shift
x >>> y // bitwise unsigned right shift
x + "y" // string concatenation
x ? y : z // ternary operator (if x then y else z)
```

- **Conditionals**: Conditionals are statements that execute different blocks of code depending on a condition. The most common conditional statements are **if-else** and **switch-case**. For example:

```javascript
if (x > 10) {
  console.log("x is greater than 10");
} else if (x < 10) {
  console.log("x is less than 10");
} else {
  console.log("x is equal to 10");
}

switch (x) {
  case 1:
    console.log("x is 1");
    break;
  case 2:
    console.log("x is 2");
    break;
  default:
    console.log("x is neither 1 nor 2");
}
```

- **Loops**: Loops are statements that repeat a block of code until a condition is met. The most common loop statements are **for**, **while**, and **do-while**. For example:

```javascript
for (let i = 0; i < 10; i++) {
  console.log(i);
}

let i = 0;
while (i < 10) {
  console.log(i);
  i++;
}

let i = 0;
do {
  console.log(i);
  i++;
} while (i < 10);
```

- **Functions**: Functions are blocks of code that can be defined and called to perform a specific task. They can have parameters and return values. They can also be assigned to variables or passed as arguments to other