#### Objects in JavaScript

- An object is a collection of properties that store values and functions that perform actions.
- An object can be created using an object literal, which is a pair of curly braces that enclose a list of property names and values, separated by commas.
- For example, the following code creates an object named person with three properties: name, age, and greet.

```javascript
var person = {
  name: "Alice",
  age: 25,
  greet: function() {
    console.log("Hello, I am " + this.name);
  }
};
```

- The properties of an object can be accessed using the dot notation or the bracket notation.
- For example, the following code prints the name and age of the person object.

```javascript
console.log(person.name); // Alice
console.log(person["age"]); // 25
```

- The this keyword refers to the current object in a function that is defined as a property of that object.
- For example, the following code calls the greet function of the person object, which prints "Hello, I am Alice".

```javascript
person.greet(); // Hello, I am Alice
```

- An object can be modified by adding, updating, or deleting properties.
- For example, the following code adds a new property called hobby to the person object, updates the age property to 26, and deletes the greet property.

```javascript
person.hobby = "reading";
person.age = 26;
delete person.greet;
```

- An object can be iterated over using a for...in loop, which loops through the property names of the object.
- For example, the following code prints all the properties and values of the person object.

```javascript
for (var prop in person) {
  console.log(prop + ": " + person[prop]);
}
```

- An object can be copied by using the Object.assign method, which takes a target object and one or more source objects as arguments, and copies the properties from the source objects to the target object.
- For example, the following code creates a new object named person2 that is a copy of person.

```javascript
var person2 = Object.assign({}, person);
```

- An object can be compared by using the === operator, which checks if two objects refer to the same memory location, not if they have the same properties and values.
- For example, the following code compares person and person2, and prints false, because they are two different objects.

```javascript
console.log(person === person2); // false
```

- An object can be converted to a string by using the JSON.stringify method, which returns a JSON representation of the object.
- For example, the following code converts person to a string and prints it.

```javascript
var personString = JSON.stringify(person);
console.log(personString); // {"name":"Alice","age":26,"hobby":"reading"}
```

- An object can be converted from a string by using the JSON.parse method, which takes a JSON string and returns an object.
- For example, the following code converts personString to an object and assigns it to person3.

```javascript
var person3 = JSON.parse(personString);
```

- A mnemonic to remember the syntax of an object literal is: **CURLY**.
  - **C** for curly braces that enclose the object.
  - **U** for unquoted property names, unless they contain special characters or keywords.
  - **R** for colon that separates the property name and value.
  - **L** for comma that separates the properties.
  - **Y** for value that can be any data type, including another object or a function.