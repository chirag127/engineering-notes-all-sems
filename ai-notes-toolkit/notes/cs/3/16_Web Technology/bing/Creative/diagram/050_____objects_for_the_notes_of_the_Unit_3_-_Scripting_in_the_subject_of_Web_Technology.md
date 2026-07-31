Hello, I am Sydney, your AI assistant. I can help you with your notes on web technology. Here is some content on the topic of objects for the unit 3 - scripting.

### Objects

- An object is a collection of properties and methods that define its behavior and characteristics.
- A property is a variable that belongs to an object and stores some value, such as a name, a color, a number, etc.
- A method is a function that belongs to an object and performs some action, such as changing a property, displaying a message, calculating a result, etc.
- Objects can be created using different ways, such as object literals, constructors, or object-oriented classes.
- Object literals are a simple and concise way to create objects using curly braces and key-value pairs, such as `var person = {name: "Alice", age: 25, greet: function() {alert("Hello, " + this.name);}};`
- Constructors are functions that are used to create objects of the same type, using the `new` keyword and the `this` keyword to refer to the current object, such as `function Person(name, age) {this.name = name; this.age = age; this.greet = function() {alert("Hello, " + this.name);}}; var person1 = new Person("Alice", 25); var person2 = new Person("Bob", 30);`
- Object-oriented classes are a modern and elegant way to create objects using the `class` keyword and the `constructor` method, as well as other methods and properties, such as `class Person {constructor(name, age) {this.name = name; this.age = age;} greet() {alert("Hello, " + this.name);}}; var person1 = new Person("Alice", 25); var person2 = new Person("Bob", 30);`
- Objects can be accessed and modified using the dot notation or the bracket notation, such as `person1.name = "Alice Smith"; person2["age"] = 31;`
- Objects can be nested inside other objects, creating complex data structures, such as `var family = {parents: {father: {name: "John", age: 50}, mother: {name: "Mary", age: 48}}, children: [{name: "Alice", age: 25}, {name: "Bob", age: 30}]};`
- Objects can be inherited from other objects, creating a hierarchy of classes and subclasses, using the `extends` keyword and the `super` keyword, such as `class Student extends Person {constructor(name, age, grade) {super(name, age); this.grade = grade;} study() {alert(this.name + " is studying for grade " + this.grade);}}; var student1 = new Student("Alice", 25, "A"); var student2 = new Student("Bob", 30, "B");`
- Objects can be used to create dynamic and interactive web pages, using scripting languages such as JavaScript, which can manipulate the Document Object Model (DOM) and the Browser Object Model (BOM) of the web browser.