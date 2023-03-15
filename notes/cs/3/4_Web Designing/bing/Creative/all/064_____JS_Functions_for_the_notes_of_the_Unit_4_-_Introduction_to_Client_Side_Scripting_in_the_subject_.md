# JS Functions

- A function is a block of code that performs a specific task and can be reused multiple times.
- A function can have parameters, which are variables that receive values from the function caller.
- A function can also return a value to the function caller, using the return statement.
- To define a function, use the function keyword, followed by the function name, parentheses, and curly braces.
- To call a function, use the function name, followed by parentheses, and optionally pass arguments that match the parameters.
- Example:

```javascript
// Define a function that calculates the area of a circle
function areaOfCircle(radius) {
  // Use the Math.PI constant and the power operator
  return Math.PI * radius ** 2;
}

// Call the function and store the result in a variable
let area = areaOfCircle(5);

// Print the result
console.log(area); // 78.53981633974483
```

- A function can also be assigned to a variable, which is called a function expression.
- A function expression can be anonymous, meaning it does not have a name, or named, meaning it has a name.
- A function expression can also be an arrow function, which uses the arrow syntax (=>) instead of the function keyword.
- Example:

```javascript
// Assign an anonymous function expression to a variable
let square = function (num) {
  return num * num;
};

// Assign a named function expression to a variable
let cube = function cubed(num) {
  return num * num * num;
};

// Assign an arrow function expression to a variable
let double = (num) => {
  return num * 2;
};

// Call the function expressions and print the results
console.log(square(4)); // 16
console.log(cube(3)); // 27
console.log(double(5)); // 10
```

- A function can also be defined as a method of an object, which is called a method.
- A method can access the properties and other methods of the object using the this keyword.
- To define a method, use the object name, followed by a dot, the method name, parentheses, and curly braces.
- To call a method, use the object name, followed by a dot, the method name, and parentheses.
- Example:

```javascript
// Define an object with properties and methods
let person = {
  name: "Alice",
  age: 25,
  greet: function () {
    // Use the this keyword to access the name property
    console.log("Hello, my name is " + this.name);
  },
  birthday: function () {
    // Use the this keyword to access and modify the age property
    this.age++;
    console.log("I am now " + this.age + " years old");
  },
};

// Call the methods of the object
person.greet(); // Hello, my name is Alice
person.birthday(); // I am now 26 years old
```