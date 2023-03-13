#### Objects in JavaScript

- Objects are variables that contain multiple data values, in the form of key-value pairs. The keys can be variables or functions, and are called properties or methods, respectively.
- Objects can be created using the `Object()` constructor or the object literal syntax, which uses curly braces `{}` to enclose the key-value pairs.
- For example, the following code creates an object named `person` with three properties: `name`, `age`, and `greet`.

```javascript
// Using the Object() constructor
var person = new Object();
person.name = "Alice";
person.age = 25;
person.greet = function() {
  console.log("Hello, I am " + this.name);
};

// Using the object literal syntax
var person = {
  name: "Alice",
  age: 25,
  greet: function() {
    console.log("Hello, I am " + this.name);
  }
};
```

- To access or modify the properties or methods of an object, we can use the dot notation `.` or the bracket notation `[]`.
- For example, the following code prints the name and age of the `person` object, and invokes the `greet` method.

```javascript
// Using the dot notation
console.log(person.name); // Alice
console.log(person.age); // 25
person.greet(); // Hello, I am Alice

// Using the bracket notation
console.log(person["name"]); // Alice
console.log(person["age"]); // 25
person["greet"](); // Hello, I am Alice
```

- Objects in JavaScript are dynamic, meaning that we can add, delete, or change their properties or methods at any time.
- For example, the following code adds a new property `gender` and deletes the `age` property from the `person` object.

```javascript
// Adding a new property
person.gender = "female";
console.log(person.gender); // female

// Deleting a property
delete person.age;
console.log(person.age); // undefined
```

- Objects in JavaScript are also mutable, meaning that they can be modified by reference. This means that if we assign an object to another variable, both variables will point to the same object in memory, and any changes made to one will affect the other.
- For example, the following code assigns the `person` object to a new variable `anotherPerson`, and changes the `name` property of `anotherPerson`. This also changes the `name` property of `person`.

```javascript
// Assigning an object to another variable
var anotherPerson = person;
console.log(anotherPerson.name); // Alice

// Changing the name property of anotherPerson
anotherPerson.name = "Bob";
console.log(anotherPerson.name); // Bob
console.log(person.name); // Bob
```

- Objects in JavaScript are instances of the `Object` type, which is the root of the prototype chain. This means that all objects inherit some properties and methods from the `Object.prototype` object, such as `toString()`, `hasOwnProperty()`, and `valueOf()`.
- We can also create our own custom objects by using constructor functions or classes, which allow us to define the properties and methods of the objects, and set their prototype to a specific object. This way, we can implement inheritance and polymorphism in JavaScript.