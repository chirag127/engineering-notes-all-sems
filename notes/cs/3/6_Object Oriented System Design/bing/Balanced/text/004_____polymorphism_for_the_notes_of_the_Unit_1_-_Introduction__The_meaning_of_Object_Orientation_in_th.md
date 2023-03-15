### Polymorphism for the notes of the Unit 1 - Introduction: The meaning of Object Orientation in the subject of Object Oriented System Design

- Polymorphism is one of the core concepts of object-oriented programming (OOP) and describes situations in which something occurs in several different forms .
- In computer science, it describes the concept that you can access objects of different types through the same interface .
- For example, you can have a base class called Shape that defines a common interface for drawing different shapes, such as Circle, Square, Triangle, etc. Each derived class can implement its own draw method, but they can all be accessed through the same interface of the base class.
- Polymorphism allows you to write generic and reusable code that can work with different types of objects without knowing their exact details at compile time .
- Polymorphism also helps to enforce simplicity, making codes more extendable and easily maintaining applications.
- There are two main types of polymorphism in OOP: static (or compile-time) and dynamic (or run-time).
  - Static polymorphism is achieved by using method overloading, which means defining multiple methods with the same name but different parameters in the same class or its subclasses.
  - Dynamic polymorphism is achieved by using method overriding, which means redefining a method of the base class in a derived class to provide a different implementation. This requires the use of virtual methods, which are methods that can be overridden by subclasses.
- Polymorphism is one of the principles of OOP, along with abstraction, encapsulation, and inheritance. These principles help to design and develop software systems that are modular, reusable, maintainable, and extensible.