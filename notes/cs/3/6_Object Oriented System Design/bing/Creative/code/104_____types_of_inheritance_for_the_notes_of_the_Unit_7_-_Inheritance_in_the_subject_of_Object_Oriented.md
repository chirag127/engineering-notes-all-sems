# Types of Inheritance for the Notes of the Unit 7 - Inheritance in the Subject of Object Oriented System Design

Inheritance is one of the fundamental concepts of object-oriented programming. It allows a class to inherit the properties and methods of another class, thus reusing and extending the existing code. Inheritance also enables polymorphism, which is the ability of an object to behave differently depending on its type.

There are different types of inheritance in object-oriented programming, depending on the number and relationship of the classes involved. Here are some common types of inheritance:

- **Single inheritance**: A class inherits from only one base class. This is the simplest form of inheritance. For example, a `Dog` class can inherit from an `Animal` class, and a `Poodle` class can inherit from a `Dog` class.
- **Multilevel inheritance**: A class inherits from another class that also inherits from a base class. This creates a hierarchy of classes. For example, a `Poodle` class can inherit from a `Dog` class, which inherits from an `Animal` class.
- **Multiple inheritance**: A class inherits from more than one base class. This allows a class to combine the features of different classes. For example, a `FlyingCar` class can inherit from both a `Car` class and a `Plane` class.
- **Hierarchical inheritance**: More than one class inherits from a single base class. This creates a tree-like structure of classes. For example, a `Dog` class, a `Cat` class, and a `Bird` class can all inherit from an `Animal` class.
- **Hybrid inheritance**: A combination of two or more types of inheritance. This creates a complex network of classes. For example, a `FlyingCar` class can inherit from both a `Car` class and a `Plane` class, and a `Car` class can inherit from a `Vehicle` class. This is an example of multiple and single inheritance.

Each type of inheritance has its own advantages and disadvantages, and the choice of inheritance depends on the design and requirements of the system. Inheritance can help to achieve code reuse, modularity, and polymorphism, but it can also introduce complexity, ambiguity, and coupling. Therefore, inheritance should be used with care and understanding.