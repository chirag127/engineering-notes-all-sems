### Types of Inheritance

Inheritance is one of the fundamental concepts of object-oriented programming. It allows a class to inherit the properties and methods of another class, thus reusing and extending the existing code. Inheritance also enables polymorphism, which is the ability of different objects to respond in different ways to the same message.

There are five types of inheritance commonly used in object-oriented programming:

- **Single inheritance**: A derived class inherits from only one base class. For example, a `Dog` class can inherit from an `Animal` class.
- **Multilevel inheritance**: A derived class inherits from another derived class, which in turn inherits from a base class. For example, a `Poodle` class can inherit from a `Dog` class, which inherits from an `Animal` class.
- **Multiple inheritance**: A derived class inherits from more than one base class. For example, a `FlyingCar` class can inherit from both a `Car` class and a `Plane` class.
- **Hierarchical inheritance**: More than one derived class inherits from the same base class. For example, a `Cat` class and a `Dog` class can both inherit from an `Animal` class.
- **Hybrid inheritance**: A combination of two or more types of inheritance. For example, a `FlyingCar` class can inherit from a `Vehicle` class (single inheritance), and also implement an `IFlyable` interface and an `IDrivable` interface (multiple inheritance).

The following diagram illustrates the different types of inheritance:

![inheritance types](https://jharaphula.com/wp-content/uploads/2016/05/Types-of-Inheritance-in-OOPs.png)