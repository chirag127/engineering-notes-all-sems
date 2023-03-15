Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of JS Objects for the Unit 4 - Introduction to Client Side Scripting in the subject of Web Designing.

### JS Objects

- An object is a collection of properties that store values and functions that perform actions.
- An object can be created using the object literal syntax, which consists of a pair of curly braces `{}` and a comma-separated list of property names and values.
- Example: `var person = {name: "Alice", age: 25, greet: function() {console.log("Hello, I am " + this.name);}};`
- An object can also be created using the `new` keyword and a constructor function, which is a special function that defines the properties and methods of the object.
- Example: `function Person(name, age) {this.name = name; this.age = age; this.greet = function() {console.log("Hello, I am " + this.name);};} var person = new Person("Alice", 25);`
- An object can be accessed and modified using the dot notation or the bracket notation.
- Example: `person.name = "Bob"; person["age"] = 26;`
- An object can be iterated over using a `for...in` loop, which loops through the property names of the object.
- Example: `for (var prop in person) {console.log(prop + ": " + person[prop]);}`
- An object can be converted to a string using the `JSON.stringify()` method, which returns a JSON representation of the object.
- Example: `var personString = JSON.stringify(person); console.log(personString); // {"name":"Bob","age":26,"greet":function() {console.log("Hello, I am " + this.name);}}`
- An object can be converted from a string using the `JSON.parse()` method, which returns an object parsed from the JSON string.
- Example: `var personObject = JSON.parse(personString); console.log(personObject); // {name: "Bob", age: 26, greet: ƒ}`