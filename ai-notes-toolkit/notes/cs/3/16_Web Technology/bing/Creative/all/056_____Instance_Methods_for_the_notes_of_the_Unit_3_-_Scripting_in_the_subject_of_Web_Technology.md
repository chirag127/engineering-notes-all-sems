Hello, I am Sydney, your AI assistant. I can help you with your study material for Web Technology. Here are some notes on the topic of Instance Methods for Unit 3 - Scripting.

# Instance Methods

- Instance methods are functions that are defined inside a class and can be called on an object of that class.
- Instance methods have access to the object's attributes and can modify them using the `this` keyword.
- Instance methods can also use other instance methods of the same class or superclass using the `this` keyword.
- Instance methods can be overridden by subclasses to provide different behavior for the same method name.
- Instance methods can be inherited by subclasses from superclasses, unless they are marked as `private` or `final`.
- Instance methods can be overloaded by defining multiple methods with the same name but different parameters in the same class.

## Example of Instance Methods

```javascript
// Define a class called Person
class Person {
  // Define a constructor that takes a name and an age as parameters
  constructor(name, age) {
    // Assign the parameters to the object's attributes
    this.name = name;
    this.age = age;
  }

  // Define an instance method called greet that prints a greeting message
  greet() {
    console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`);
  }

  // Define an instance method called celebrate that increments the age by one and prints a message
  celebrate() {
    this.age++;
    console.log(`Happy birthday, ${this.name}! You are now ${this.age} years old.`);
  }
}

// Create an object of the Person class
let alice = new Person("Alice", 25);

// Call the greet method on the object
alice.greet(); // Hello, my name is Alice and I am 25 years old.

// Call the celebrate method on the object
alice.celebrate(); // Happy birthday, Alice! You are now 26 years old.
```