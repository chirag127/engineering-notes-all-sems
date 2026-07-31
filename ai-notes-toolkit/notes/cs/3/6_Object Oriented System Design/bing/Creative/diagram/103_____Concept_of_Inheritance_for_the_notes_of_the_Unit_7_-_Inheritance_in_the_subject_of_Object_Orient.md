### Concept of Inheritance

- Inheritance is one of the core concepts of object-oriented programming (OOP) languages.
- It is a mechanism where you can to derive a class from another class for a hierarchy of classes that share a set of attributes and methods.
- The class that is derived from another class is called a subclass or a child class. The class from which a subclass is derived is called a superclass or a parent class.
- Inheritance enables you to create new classes that reuse, extend, and modify the behavior defined in other classes.
- Inheritance also provides code reusability and reduces code duplication.
- There are two types of inheritance: implementation inheritance and interface inheritance.
  - Implementation inheritance is the mechanism whereby a subclass re-uses code in a base class. By default the subclass retains all of the operations of the base class, but the subclass may override some or all operations, replacing the base-class implementation with its own.
  - Interface inheritance is the mechanism whereby a subclass inherits only the signatures of the operations from the base class, but not their implementation. The subclass must provide its own implementation for all the inherited operations.
- Inheritance can be represented by a UML class diagram, where a solid line with an empty arrowhead indicates a generalization relationship between a superclass and a subclass.

![inheritance diagram](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Inheritance.svg/1200px-Inheritance.svg.png)