Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of JS Objects for the Unit 4 - Introduction to Client Side Scripting in the subject of Web Designing.

# JS Objects

- An object is a collection of properties and methods that define its behavior and characteristics.
- A property is a key-value pair that associates a name with a value. A value can be a primitive data type (such as a number, string, boolean, null, or undefined) or another object or function.
- A method is a property that has a function as its value. A method can perform some actions on the object or its properties, and optionally return a value.
- An object can be created using an object literal, which is a comma-separated list of properties and methods enclosed in curly braces. For example:

```js
var person = {
  name: "Alice",
  age: 25,
  greet: function() {
    console.log("Hello, I am " + this.name);
  }
};
```

- An object can also be created using a constructor function, which is a special function that defines the properties and methods of the object. A constructor function is invoked with the new keyword, which creates a new instance of the object. For example:

```js
function Person(name, age) {
  this.name = name;
  this.age = age;
  this.greet = function() {
    console.log("Hello, I am " + this.name);
  };
}

var person = new Person("Alice", 25);
```

- An object can also be created using the Object.create() method, which takes an existing object as a prototype and returns a new object that inherits its properties and methods. For example:

```js
var person = {
  name: "Alice",
  age: 25,
  greet: function() {
    console.log("Hello, I am " + this.name);
  }
};

var student = Object.create(person);
student.school = "ABC University";
student.study = function() {
  console.log("I am studying at " + this.school);
};
```

- To access or modify the properties or methods of an object, the dot notation or the bracket notation can be used. For example:

```js
// dot notation
console.log(person.name); // Alice
person.age = 26;
person.greet(); // Hello, I am Alice

// bracket notation
console.log(person["name"]); // Alice
person["age"] = 26;
person["greet"](); // Hello, I am Alice
```

- The this keyword refers to the current object that is executing the code. It can be used to access or modify the properties or methods of the object. For example:

```js
var person = {
  name: "Alice",
  age: 25,
  greet: function() {
    console.log("Hello, I am " + this.name);
    this.age++;
    console.log("I am " + this.age + " years old");
  }
};

person.greet();
// Hello, I am Alice
// I am 26 years old
```

- An object can have other objects or functions as its properties or methods. This allows for creating complex and hierarchical data structures. For example:

```js
var person = {
  name: "Alice",
  age: 25,
  address: {
    street: "123 Main Street",
    city: "New York",
    zip: "10001"
  },
  hobbies: ["reading", "writing", "coding"],
  greet: function() {
    console.log("Hello, I am " + this.name);
  },
  showAddress: function() {
    console.log("I live at " + this.address.street + ", " + this.address.city + ", " + this.address.zip);
  },
  showHobbies: function() {
    console.log("I like " + this.hobbies.join(", "));
  }
};

person.greet(); // Hello, I am Alice
person.showAddress(); // I live at 123 Main Street, New York, 10001
person.showHobbies(); // I like reading, writing, coding
```