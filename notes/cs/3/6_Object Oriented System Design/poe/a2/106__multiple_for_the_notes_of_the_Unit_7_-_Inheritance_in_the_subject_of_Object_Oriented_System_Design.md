 Here are the notes for Unit 7 - Inheritance in Object Oriented System Design:

### Inheritance

- Inheritance is the process by which one class acquires the properties and behaviors of another class. The acquiring class is known as the subclass (or child class), and the class being acquired is known as the superclass (or parent class).
- Through inheritance, the subclass can reuse the code from the superclass, and the superclass can define common characteristics for its subclasses. This results in a hierarchy of relationships between classes.
- The key benefits of inheritance are:
- Code reuse: Subclass can reuse the methods and properties defined in the superclass. This avoids redundant code and makes the code more maintainable.
- Polymorphism: The subclass can override methods defined in the superclass, giving them specific implementation. This allows us to invoke methods on a superclass type and have the "most-derived" implementation execute at runtime.
- Extensibility: We can extend an existing class to add more features to it. The original class can remain unchanged while new classes can be created from it.

### Types of Inheritance

- Single inheritance: A class can inherit from only one superclass. This is the most common type.
- Multiple inheritance: A class can inherit from multiple superclasses. This can lead to ambiguity and is not supported in many programming languages.
- Multilevel inheritance: A subclass can inherit from another subclass, extending the hierarchy to multiple levels.
- Hierarchical inheritance: A superclass can have multiple subclasses that inherit from it.
- Hybrid inheritance: A combination of multiple types of inheritance.