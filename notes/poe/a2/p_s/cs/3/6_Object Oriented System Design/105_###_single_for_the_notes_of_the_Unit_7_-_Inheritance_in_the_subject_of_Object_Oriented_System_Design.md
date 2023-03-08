 Here are the notes for Unit 7 - Inheritance in Object Oriented System Design:

### Inheritance

Inheritance is one of the fundamental concepts of Object Oriented Programming (OOP). It allows us to define a class that inherits all the methods and properties from another class.

Parent class: The class being inherited from is called parent class or base class.
Child class: The class that inherits from another class is called child class or derived class.

Advantages:

- Code reusability: Inheritance allows us to reuse the code from the parent class, thus promoting code reusability.
- Extensibility: We can extend the functionality of a parent class by defining a child class that inherits from it. The child class can have additional properties and methods as needed.
- Readability: The inheritance hierarchy makes the structure of a program more readable and easier to understand.

Types:

- Single inheritance: When a child class inherits from only one parent class, it is called single inheritance.
- Multiple inheritance: When a child class inherits from multiple parent classes, it is called multiple inheritance. (Note: Multiple inheritance is not supported in Java)
- Multilevel inheritance: When we have a child and grandchild relationship between multiple classes, it is called multilevel inheritance. The grandchild class inherits from the child class which in turn inherits from the parent class.
- Hierarchical inheritance: When multiple child classes inherit from a single parent class, it is called hierarchical inheritance.

Examples:

Vehicle (parent class)
- wheels: 4
- seats: 5

Car (child class)
- doors: 4

Motorcycle (child class)
- wheels: 2

Applications: Inheritance is used extensively in Java and other OOP languages to model real-world relationships between entities. For example, an inheritance hierarchy of classes Vehicle, Car, Motorcycle models the "is a" relationship. A Car "is a" Vehicle, and a Motorcycle "is a" Vehicle as well.