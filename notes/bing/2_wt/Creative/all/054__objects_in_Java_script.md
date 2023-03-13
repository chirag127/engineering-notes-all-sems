#### Objects in JavaScript

- An object is a collection of properties that store values and functions that perform actions.
- An object can be created using an object literal, which is a pair of curly braces that enclose a list of property names and values, separated by commas.
- For example, this is an object literal that represents a person:

```javascript
var person = {
  name: "Alice",
  age: 25,
  greet: function() {
    console.log("Hello, I am " + this.name);
  }
};
```

- The object has three properties: `name`, `age`, and `greet`. The first two properties store string and number values, respectively. The third property stores a function, which is called a method.
- To access a property of an object, use the dot notation or the bracket notation. For example, to get the name of the person object, use either `person.name` or `person["name"]`.
- To call a method of an object, use the dot notation followed by parentheses. For example, to invoke the greet method of the person object, use `person.greet()`.
- The keyword `this` inside a method refers to the object that the method belongs to. For example, in the greet method, `this.name` refers to the name property of the person object.
- An object can be modified by adding, updating, or deleting properties. For example, to add a new property called `hobby` to the person object, use `person.hobby = "reading";`. To update the value of the age property, use `person.age = 26;`. To delete the greet property, use `delete person.greet;`.
- An object can be iterated over using a `for...in` loop, which loops through the property names of the object. For example, to print all the properties and values of the person object, use:

```javascript
for (var prop in person) {
  console.log(prop + ": " + person[prop]);
}
```

- An object can be converted to a string using the `JSON.stringify()` method, which returns a JSON representation of the object. For example, to get a string version of the person object, use `JSON.stringify(person);`.
- An object can be converted from a string using the `JSON.parse()` method, which parses a JSON string and returns an object. For example, to get an object from a string, use `JSON.parse('{"name":"Bob","age":30}');`.

- A mnemonic to remember the syntax of an object literal is: **O**pen **C**urly **B**races, **P**roperty **N**ame, **C**olon, **V**alue, **C**omma, **R**epeat, **C**lose **C**urly **B**races. (OCBPNVCRCCB)