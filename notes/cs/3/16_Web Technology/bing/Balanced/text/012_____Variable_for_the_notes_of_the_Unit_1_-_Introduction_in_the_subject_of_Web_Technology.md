### Variable

- A variable is a named storage location that can hold different values of the same data type.
- A variable has a name (also called an identifier) and a value that can be changed during the program execution.
- A variable can be declared by specifying its data type and name, optionally followed by an assignment operator and an initial value.
- For example, in JavaScript, a variable can be declared as follows:

```javascript
var x; // declare a variable named x
var y = 10; // declare a variable named y and assign it the value 10
```

- A variable can be used in expressions, statements, and other parts of the program where a value is needed.
- A variable can be assigned a new value at any time using the assignment operator (=).

```javascript
x = 5; // assign the value 5 to x
y = x + 2; // assign the value of x + 2 to y
```

- A variable can have different scopes depending on where it is declared and how it is accessed.
- A variable can be global, local, or block-scoped.
- A global variable is declared outside any function or block and can be accessed from anywhere in the program.
- A local variable is declared inside a function or block and can be accessed only within that function or block.
- A block-scoped variable is declared with the keywords let or const inside a block (such as a loop or a conditional statement) and can be accessed only within that block.
- For example, in JavaScript, a variable can have different scopes as follows:

```javascript
var a = 1; // global variable
function foo() {
  var b = 2; // local variable
  if (true) {
    let c = 3; // block-scoped variable
    console.log(a); // prints 1
    console.log(b); // prints 2
    console.log(c); // prints 3
  }
  console.log(a); // prints 1
  console.log(b); // prints 2
  console.log(c); // error: c is not defined
}
foo();
console.log(a); // prints 1
console.log(b); // error: b is not defined
console.log(c); // error: c is not defined
```

- A variable can have different data types depending on the value it holds and the programming language used.
- A data type defines the range of values, the size of memory, and the operations that can be performed on a variable.
- Some common data types are: number, string, boolean, array, object, function, etc.
- For example, in JavaScript, a variable can have different data types as follows:

```javascript
var x = 10; // number
var y = "Hello"; // string
var z = true; // boolean
var w = [1, 2, 3]; // array
var v = {name: "Alice", age: 25}; // object
var u = function() {return "Hi"}; // function
```