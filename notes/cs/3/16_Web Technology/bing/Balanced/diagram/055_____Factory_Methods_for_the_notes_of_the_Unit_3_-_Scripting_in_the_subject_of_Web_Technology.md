Hello, I am Sydney, your AI assistant. I can help you with your study material for Web Technology. Here are some notes on the topic of Factory Methods for the Unit 3 - Scripting.

### Factory Methods

- Factory methods are a design pattern that allows creating objects without specifying the exact class or constructor function that will be used.
- Factory methods are useful when the type of object to be created depends on some conditions or parameters, such as user input, configuration settings, or environment variables.
- Factory methods can also provide a level of abstraction and encapsulation, hiding the details of object creation and allowing for easy modification or extension of the code.
- Factory methods can be implemented in different ways, such as using a simple function, a static method, or a separate factory class or object.
- Factory methods can return different types of objects that share a common interface or superclass, allowing for polymorphism and dynamic binding.
- Factory methods can also be used to implement the singleton pattern, which ensures that only one instance of a class or object exists in the application.

#### Example of a factory method in JavaScript

```javascript
// A simple factory function that returns a different type of animal object based on the parameter
function createAnimal(type) {
  if (type === "cat") {
    return {
      name: "Fluffy",
      sound: "Meow",
      makeSound: function() {
        console.log(this.sound);
      }
    };
  } else if (type === "dog") {
    return {
      name: "Spot",
      sound: "Woof",
      makeSound: function() {
        console.log(this.sound);
      }
    };
  } else {
    return {
      name: "Unknown",
      sound: "???",
      makeSound: function() {
        console.log(this.sound);
      }
    };
  }
}

// Using the factory function to create different animal objects
var cat = createAnimal("cat");
var dog = createAnimal("dog");
var alien = createAnimal("alien");

// Calling the makeSound method on each object
cat.makeSound(); // Meow
dog.makeSound(); // Woof
alien.makeSound(); // ???
```