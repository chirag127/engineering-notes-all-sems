#### Statements in JavaScript

- A statement is a piece of code that performs some action or produces some value.
- Statements can be simple or complex, depending on the number of sub-statements they contain.
- Statements are executed in order, from top to bottom, unless there is a control flow statement that changes the order of execution.
- Statements are usually terminated by a semicolon (;), but it is optional in most cases.
- Some examples of statements are:

```javascript
// A simple statement that assigns a value to a variable
var x = 10;

// A complex statement that contains a conditional expression and a block of statements
if (x > 0) {
  console.log("x is positive");
  x--;
}

// A statement that defines a function
function add(a, b) {
  return a + b;
}

// A statement that calls a function
var sum = add(3, 4);

// A statement that creates an object
var person = {
  name: "Alice",
  age: 25
};

// A statement that accesses a property of an object
var name = person.name;

// A statement that loops through an array
for (var i = 0; i < array.length; i++) {
  console.log(array[i]);
}
```