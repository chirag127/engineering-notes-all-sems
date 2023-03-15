Hello, I am Sydney, your AI assistant. I can help you with your study material for Web Technology. Here are some notes on the topic of Instance Methods for Unit 3 - Scripting.

### Instance Methods

- Instance methods are functions that are defined inside a class and can be called on an object of that class.
- Instance methods have access to the object's attributes and can modify them using the `this` keyword.
- Instance methods can also call other instance methods of the same class using the `this` keyword.
- Instance methods can be inherited by subclasses and can be overridden by redefining them in the subclass.
- Instance methods can be invoked using the dot notation (`object.method()`) or the bracket notation (`object['method']()`).

#### Example

```javascript
// Define a class called Person
class Person {
  // Define a constructor that takes a name and an age as parameters
  constructor(name, age) {
    // Assign the parameters to the object's attributes
    this.name = name;
    this.age = age;
  }

  // Define an instance method called greet that returns a greeting message
  greet() {
    return `Hello, my name is ${this.name} and I am ${this.age} years old.`;
  }

  // Define an instance method called celebrate that increments the object's age by one and prints a message
  celebrate() {
    this.age++;
    console.log(`Happy birthday, ${this.name}! You are now ${this.age} years old.`);
  }
}

// Create an object of the Person class
let alice = new Person('Alice', 25);

// Invoke the greet method on the object
console.log(alice.greet()); // Hello, my name is Alice and I am 25 years old.

// Invoke the celebrate method on the object
alice.celebrate(); // Happy birthday, Alice! You are now 26 years old.
```