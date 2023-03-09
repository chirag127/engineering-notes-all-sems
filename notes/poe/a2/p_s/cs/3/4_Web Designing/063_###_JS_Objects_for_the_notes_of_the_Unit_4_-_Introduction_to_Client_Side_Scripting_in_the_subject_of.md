 Here is the content written in markdown format for the topic ### JS Objects for the notes of the Unit 4 - Introduction to Client Side Scripting in the subject of Web Designing:

### JS Objects

- Objects in JavaScript are a collection of properties that hold data and methods that perform actions.
- Objects are represented by curly braces {} with properties and methods inside.
- For example: {name: "John", age: 30, car: "BMW"}
- Properties are denoted by name: value pairs and methods are functions.
- Some important built-in objects in JS are:

1. String - for string manipulation
2. Number - for numeric operations
3. Boolean - for boolean logic
4. Date - for date and time functions
5. Array - for arrays of data
6. Math - for mathematical operations

- Object properties can be accessed using dot notation (object.property) or bracket notation (object["property"]).
- Objects can be created using object literals or constructor functions.
- For example:

Object literal:
const person = {
  name: "John",
  age: 30
};

Constructor function:
function Person(name, age) {
  this.name = name;
  this.age = age;
}

const person1 = new Person("John", 30);

- Advantages of objects:
- Code reusability - objects can be reused
- Organized structure - keeps related data and functions together
- Easy to understand - resembles real world objects

- Disadvantages:
- Can be complex to handle as more properties and methods are added
- Scope - objects can pollute the global scope if not properly contained

- Various applications of objects:
- Creating models of real world things
- Storing and manipulating data
- Creating reusable code modules
- And much more! Objects are a fundamental part of JavaScript.