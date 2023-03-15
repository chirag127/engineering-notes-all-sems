Hello, I am Sydney, your AI assistant. I can help you with your notes on the topic of objects for the Unit 3 - Scripting in the subject of Web Technology. Here is the content in markdown format:

### Objects

- An object is a collection of properties and methods that define its behavior and characteristics.
- A property is a variable that belongs to an object and stores some value, such as `name`, `color`, `age`, etc.
- A method is a function that belongs to an object and performs some action, such as `sayHello()`, `move()`, `calculate()`, etc.
- Objects can be created using different ways, such as:
  - Object literals: using curly braces `{}` and key-value pairs, such as `var person = {name: "Alice", age: 25, sayHello: function() {console.log("Hello, I am " + this.name);}};`
  - Object constructors: using a function that defines the properties and methods of an object, such as `function Person(name, age) {this.name = name; this.age = age; this.sayHello = function() {console.log("Hello, I am " + this.name);}}; var person = new Person("Alice", 25);`
  - Object.create(): using an existing object as a prototype for a new object, such as `var person = {name: "Alice", age: 25, sayHello: function() {console.log("Hello, I am " + this.name);}}; var student = Object.create(person); student.grade = 10;`
- Objects can be accessed and modified using dot notation or bracket notation, such as `person.name` or `person["name"]`.
- Objects can be nested inside other objects, creating complex data structures, such as `var school = {name: "ABC", students: [{name: "Alice", grade: 10}, {name: "Bob", grade: 9}], teachers: [{name: "Mr. X", subject: "Math"}, {name: "Ms. Y", subject: "English"}]};`
- Objects can be used to model real-world entities and concepts, such as `var car = {make: "Toyota", model: "Corolla", color: "red", start: function() {console.log("The car is starting");}, stop: function() {console.log("The car is stopping");}};`