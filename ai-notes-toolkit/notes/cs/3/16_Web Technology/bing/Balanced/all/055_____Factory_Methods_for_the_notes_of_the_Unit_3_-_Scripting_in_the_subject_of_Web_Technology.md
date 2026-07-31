# Factory Methods

- Factory methods are a type of design pattern that allows creating objects without specifying their concrete classes.
- Factory methods define a method, which should be used for creating objects instead of using a direct constructor call (new operator).
- Factory methods are useful when a class cannot anticipate the type of objects it needs to create beforehand, or when a class requires its subclasses to specify the objects it creates.
- Factory methods can also provide a level of abstraction and encapsulation for the object creation process, hiding the implementation details from the client code.
- Factory methods can be implemented in different ways, such as using a static method, a parameterized method, or an abstract method.
- Factory methods can have advantages such as:
  - Reducing coupling between classes by avoiding hard-coded dependencies.
  - Improving code readability and maintainability by using descriptive names for the factory methods.
  - Supporting the open/closed principle by allowing adding new classes without modifying the existing code.
  - Enhancing testability by allowing mocking or stubbing the factory methods.
- Factory methods can have disadvantages such as:
  - Increasing the complexity of the code by introducing additional classes and interfaces.
  - Violating the single responsibility principle by mixing the creation and usage logic in the same class.
  - Creating unnecessary overhead by creating objects that are not needed or used.

- An example of factory methods in web scripting is the factory functions in JavaScript, which are similar to constructor functions, but they do not require the use of the `this` keyword for inner values or the `new` keyword when instantiating new objects .
- Factory functions in JavaScript can contain inner values, methods, etc. just like normal regular functions .
- Factory functions in JavaScript can be used to create objects with different properties and behaviors based on the parameters passed to the function .
- Factory functions in JavaScript can also leverage closures to create private variables and methods that are not accessible from the outside .
- An example of a factory function in JavaScript is:

```javascript
// A factory function that creates a person object
function createPerson(name, age, occupation) {
  // A private variable that stores the person's salary
  let salary = 0;

  // A private method that calculates the person's salary based on their occupation
  function calculateSalary() {
    switch (occupation) {
      case "teacher":
        salary = 30000;
        break;
      case "engineer":
        salary = 50000;
        break;
      case "doctor":
        salary = 80000;
        break;
      default:
        salary = 0;
    }
  }

  // A public method that returns the person's name
  function getName() {
    return name;
  }

  // A public method that returns the person's age
  function getAge() {
    return age;
  }

  // A public method that returns the person's occupation
  function getOccupation() {
    return occupation;
  }

  // A public method that returns the person's salary
  function getSalary() {
    // Call the private method to calculate the salary
    calculateSalary();
    return salary;
  }

  // Return an object that exposes the public methods
  return {
    getName,
    getAge,
    getOccupation,
    getSalary,
  };
}

// Create a person object using the factory function
let person1 = createPerson("Alice", 25, "teacher");

// Access the person's properties and methods
console.log(person1.getName()); // Alice
console.log(person1.getAge()); // 25
console.log(person1.getOccupation()); // teacher
console.log(person1.getSalary()); // 30000

// Create another person object using the factory function
let person2 = createPerson("Bob", 30, "engineer");

// Access the person's properties and methods
console.log(person2.getName()); // Bob
console.log(person2.getAge()); // 30
console.log(person2.getOccupation()); // engineer
console.log(person2.getSalary()); // 50000
```