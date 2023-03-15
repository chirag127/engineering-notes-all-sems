### Types of Inheritance for the Notes of the Unit 7 - Inheritance in the Subject of Object Oriented System Design

Inheritance is one of the fundamental concepts of object-oriented programming. It allows a class to inherit the properties and methods of another class, thus avoiding code duplication and enhancing reusability. Inheritance also enables polymorphism, which is the ability of an object to behave differently depending on its type.

There are different types of inheritance in object-oriented programming, depending on the number and relationship of the classes involved. Here are some common types of inheritance:

- **Single inheritance**: A class inherits from only one base class. This is the simplest form of inheritance. For example, a `Dog` class can inherit from an `Animal` class.
- **Multilevel inheritance**: A class inherits from another class, which in turn inherits from another class. This creates a chain of inheritance. For example, a `Poodle` class can inherit from a `Dog` class, which inherits from an `Animal` class.
- **Multiple inheritance**: A class inherits from more than one base class. This allows a class to combine the features of different classes. For example, a `FlyingCar` class can inherit from both a `Car` class and a `Plane` class.
- **Hierarchical inheritance**: More than one class inherits from the same base class. This creates a tree-like structure of inheritance. For example, a `Cat` class and a `Dog` class can both inherit from an `Animal` class.
- **Hybrid inheritance**: A combination of two or more types of inheritance. This creates a complex network of inheritance. For example, a `Bat` class can inherit from both an `Animal` class and a `Flying` interface, which is a form of multiple inheritance, while a `VampireBat` class can inherit from a `Bat` class, which is a form of multilevel inheritance.

Different programming languages support different types of inheritance. For example, C++ supports multiple inheritance, while Java does not. However, Java supports multiple inheritance of interfaces, which are abstract classes that only declare methods without providing any implementation. Interfaces can be used to achieve polymorphism and code reuse without the complexity of multiple inheritance.