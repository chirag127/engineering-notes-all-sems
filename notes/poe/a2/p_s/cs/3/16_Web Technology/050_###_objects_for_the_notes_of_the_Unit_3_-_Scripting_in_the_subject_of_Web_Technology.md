 Here is the content written in markdown format for the topic ### objects for the notes of the Unit 3 - Scripting in the subject of Web Technology:

### Objects

- Objects in JavaScript are entities that hold data and behavior together. They model real-world things, encapsulating properties and methods.
- Properties are variables that hold data about the object. Methods are functions that act on the object.
- Object properties can be accessed using dot notation or bracket notation. Dot notation uses a period (.) to access properties, e.g. myObject.property. Bracket notation uses brackets ([]) and a string to access properties, e.g. myObject["property"].
- Objects can be created using object literals - this is an easy way to define objects. For example:

```
let myObject = {
  property1: "value1",
  property2: "value2",
  method1: function() {
    // method body
  }
};
```

- You can also use the new keyword to create an object from a constructor function. For example:

```
function myObject() {
  this.property1 = "value1";
  this.method1 = function() {
    // method body
  };
}
let myInstance = new myObject();
```

- JavaScript has some built-in objects like String, Date, Math and Array. These objects have methods and properties pre-defined which you can use in your programs. For example:

```
let myString = new String("Hello");
myString.toUpperCase(); // Returns "HELLO"
```

- Object-oriented programming in JavaScript can be achieved by defining classes that serve as blueprints for objects and creating prototype-based inheritance relationships between classes.
- Advantages of using objects:
    - Code reuse - objects allow you to reuse methods/properties in different places
    - Data protection - objects can keep data and methods private/hidden from the outside world
    - Organized structure - objects allow you to structure code into logical entities