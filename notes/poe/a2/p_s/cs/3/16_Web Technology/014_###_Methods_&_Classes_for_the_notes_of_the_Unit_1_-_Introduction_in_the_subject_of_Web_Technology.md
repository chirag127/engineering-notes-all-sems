 Here are the notes in markdown format for the topic ### Methods & Classes for the Unit 1 - Introduction in Web Technology:

## Methods

- Methods are functions that are associated with a class.
- They are declared inside a class and can only be called on instances of that class.
- Methods allow you to reuse code and make your code more organized.
- The syntax for declaring a method is:

```
class MyClass {
  methodName() {
    // method body
  }
}
```

- Methods can take parameters (inputs) and return a value. For example:

```
class MyClass {
  addNumbers(x, y) {
    return x + y;
  }
}
```

## Classes

- Classes are blueprints for objects. They define properties and methods for the objects.
- The syntax for declaring a class is:

```
class MyClass {
  // class body
}
```

- Classes should be named using PascalCase.
- You can create multiple objects from a class - each object is an instance of the class. For example:

```
let object1 = new MyClass();
let object2 = new MyClass();
```

- Classes can have constructors - special methods that are called when an object is instantiated. They are used to initialize the state of the object. For example:

```
class MyClass {
  constructor() {
    // constructor logic
  }
}
```

- Inheritance allows classes to inherit properties and methods from another class. This promotes code reuse and promotes the DRY (Don't Repeat Yourself) principle. The syntax is:

```
class ChildClass extends ParentClass {
  // class body
}
```