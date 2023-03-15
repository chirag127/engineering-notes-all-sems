#### Objects in JavaScript

- An object is a collection of properties that store values and functions that perform actions.
- An object can be created using an object literal, which is a pair of curly braces that enclose a list of property names and values, separated by commas.
- For example, `var person = {name: "Alice", age: 25, greet: function() {console.log("Hello, " + this.name);}};` creates an object named `person` with three properties: `name`, `age`, and `greet`.
- An object can also be created using an object constructor, which is a function that defines the properties and methods of the object.
- For example, `function Person(name, age) {this.name = name; this.age = age; this.greet = function() {console.log("Hello, " + this.name);};}` defines a constructor function named `Person` that takes two parameters: `name` and `age`.
- To create an object using a constructor, the `new` keyword is used, followed by the name of the constructor and the arguments.
- For example, `var person = new Person("Alice", 25);` creates an object named `person` using the `Person` constructor with the arguments `"Alice"` and `25`.
- An object can be accessed and modified using dot notation or bracket notation.
- Dot notation uses a dot (`.`) followed by the property name to access or assign a value to a property.
- For example, `person.name` returns `"Alice"` and `person.name = "Bob"` changes the value of the `name` property to `"Bob"`.
- Bracket notation uses square brackets (`[]`) with the property name as a string to access or assign a value to a property.
- For example, `person["name"]` returns `"Alice"` and `person["name"] = "Bob"` changes the value of the `name` property to `"Bob"`.
- Bracket notation is useful when the property name is stored in a variable or contains special characters that are not allowed in dot notation.
- For example, `var prop = "name"; person[prop]` returns `"Alice"` and `person["first name"] = "Alice"` assigns a value to a property named `"first name"`.
- An object can have methods, which are functions that are stored as properties of the object and can access and manipulate the object's data using the `this` keyword.
- For example, `person.greet()` calls the `greet` method of the `person` object, which logs `"Hello, Alice"` to the console.
- The `this` keyword refers to the current object that the method belongs to, and can be used to access and modify the object's properties.
- For example, `this.name` inside the `greet` method refers to the `name` property of the `person` object.