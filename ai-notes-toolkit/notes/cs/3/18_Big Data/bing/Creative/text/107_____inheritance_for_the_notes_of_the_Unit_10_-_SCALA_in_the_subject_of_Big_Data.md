### Inheritance

Inheritance is an object-oriented concept that allows a class to reuse the features (fields and methods) of another class. The class that inherits the features is called the subclass (or derived class or child class), and the class that provides the features is called the superclass (or base class or parent class).

Scala supports various types of inheritance, such as:

- Single inheritance: A subclass inherits from only one superclass.
- Multilevel inheritance: A subclass inherits from a superclass, which in turn inherits from another superclass, and so on.
- Hierarchical inheritance: A superclass has more than one subclass that inherit from it.
- Multiple inheritance: A subclass inherits from more than one superclass. This is not directly supported by Scala classes, but can be achieved by using traits, which are abstract types that can contain fields and methods.
- Hybrid inheritance: A combination of multiple and hierarchical inheritance. This can also be achieved by using traits.

Some of the benefits of inheritance are:

- Code reusability: A subclass can reuse the existing code of the superclass, without having to write it again.
- Code extensibility: A subclass can add new features or override existing ones of the superclass, without modifying the original code.
- Polymorphism: A subclass can be treated as an instance of the superclass, and can have different behaviors depending on the actual type.

Some of the syntax and rules of inheritance in Scala are:

- To inherit from a superclass, a subclass uses the `extends` keyword, followed by the name of the superclass.
- A subclass can access the public and protected members of the superclass, but not the private ones.
- A subclass can override the methods of the superclass by using the `override` keyword, and can also invoke the superclass methods by using the `super` keyword.
- A subclass can also inherit from a trait by using the `with` keyword, and can inherit from multiple traits by using multiple `with` keywords.
- A subclass can also define its own primary constructor and auxiliary constructors, but they must call the superclass constructor as the first statement.