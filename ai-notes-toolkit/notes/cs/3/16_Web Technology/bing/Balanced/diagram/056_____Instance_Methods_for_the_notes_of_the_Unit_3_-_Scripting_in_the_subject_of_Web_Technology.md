Hello, I am Sydney, your AI assistant. I can help you with your study material for Web Technology. Here are some notes on the topic of Instance Methods for Unit 3 - Scripting.

### Instance Methods
- Instance methods are functions that belong to an object and can access the object's properties and other methods.
- Instance methods are defined inside the constructor function of the object using the `this` keyword and the method name, followed by a function expression.
- Instance methods can be called by using the dot notation (`object.method()`) or the bracket notation (`object['method']()`) on the object instance.
- Instance methods can take parameters and return values, just like regular functions.
- Instance methods can also use the `this` keyword inside their body to refer to the current object instance and access its properties and other methods.

#### Example
```javascript
// Define a constructor function for a Person object
function Person(name, age) {
  // Assign properties to the object using this keyword
  this.name = name;
  this.age = age;

  // Define an instance method to greet the person
  this.greet = function() {
    console.log("Hello, my name is " + this.name + " and I am " + this.age + " years old.");
  };

  // Define another instance method to celebrate the person's birthday
  this.birthday = function() {
    // Increment the age property by one
    this.age++;
    // Call the greet method to show the updated age
    this.greet();
  };
}

// Create a new instance of the Person object
var alice = new Person("Alice", 25);

// Call the greet method on the alice object
alice.greet(); // Hello, my name is Alice and I am 25 years old.

// Call the birthday method on the alice object
alice.birthday(); // Hello, my name is Alice and I am 26 years old.
```