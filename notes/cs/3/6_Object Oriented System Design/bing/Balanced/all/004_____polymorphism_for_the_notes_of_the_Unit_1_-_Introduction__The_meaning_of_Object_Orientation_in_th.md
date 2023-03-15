# Polymorphism

- Polymorphism is one of the core concepts of object-oriented programming (OOP) and describes situations in which something occurs in several different forms.
- In computer science, it describes the concept that you can access objects of different types through the same interface.
- Polymorphism is often referred to as the third pillar of object-oriented programming, after encapsulation and inheritance.
- Polymorphism is a Greek word that means "many-shaped" and it has two distinct aspects:
  - **Static polymorphism**: This is also known as compile-time polymorphism or method overloading. It occurs when you have multiple methods with the same name but different parameters or signatures in the same class or its subclasses.
  - **Dynamic polymorphism**: This is also known as run-time polymorphism or method overriding. It occurs when you have a method in a base class that is redefined by a subclass. The method that is executed depends on the type of the object at run-time.
- You can use polymorphism to solve problems in object-oriented system design in two basic steps:
  - Create a class hierarchy in which each specific class derives from a common base class.
  - Use a virtual method to invoke the appropriate method on any derived class through a single call to the base class method.
- The benefits of polymorphism in object-oriented system design are:
  - It enforces simplicity, making codes more readable and maintainable.
  - It makes codes more extendable and reusable, allowing you to add new classes or modify existing ones without changing the interface.
  - It reduces coupling and increases cohesion, enhancing the modularity and flexibility of the system.