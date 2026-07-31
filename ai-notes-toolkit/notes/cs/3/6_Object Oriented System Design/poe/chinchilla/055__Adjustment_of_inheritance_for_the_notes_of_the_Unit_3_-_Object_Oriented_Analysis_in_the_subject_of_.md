### Adjustment of Inheritance for the Notes of Unit 3 - Object Oriented Analysis in Object Oriented System Design

Inheritance is a fundamental concept in object-oriented programming that allows new classes to be derived from existing ones. Inheritance enables the creation of a hierarchical structure of classes, with each derived class inheriting the attributes and methods of its parent class. However, inheritance can sometimes lead to design problems, and it may be necessary to make adjustments to the inheritance hierarchy. The following are some points to consider when adjusting inheritance:

1. Avoid Deep Hierarchies: Deep inheritance hierarchies can lead to complex and hard-to-maintain code. It is important to keep the inheritance hierarchy as shallow as possible to improve code readability, maintainability, and ease of use.

2. Use Composition Instead of Inheritance: In some cases, it may be better to use composition instead of inheritance. Composition involves creating an object that is composed of other objects rather than inheriting from a parent class. This approach can help to reduce complexity and improve flexibility in the design.

3. Use Interfaces for Polymorphism: Polymorphism is a key feature of object-oriented programming, and it is often achieved through inheritance. However, it can also be achieved through the use of interfaces. An interface defines a set of methods that a class must implement, and it can be used to achieve polymorphism without the constraints of inheritance.

4. Avoid Multiple Inheritance: Multiple inheritance allows a class to inherit from multiple parent classes, but it can lead to design problems such as naming conflicts and code complexity. It is generally better to avoid multiple inheritance and use composition or interfaces instead.

5. Favor Composition Over Inheritance: Inheritance can be rigid and inflexible, making it difficult to change the behavior of a class. Composition, on the other hand, allows for more flexible and dynamic behavior. When possible, favor composition over inheritance.

6. Refactor the Inheritance Hierarchy: If the inheritance hierarchy is causing design problems, it may be necessary to refactor the hierarchy. Refactoring involves reorganizing the code to improve its structure without changing its behavior. Refactoring can help to reduce complexity and improve maintainability.

In conclusion, inheritance is a powerful tool in object-oriented programming, but it can also lead to design problems. Adjusting the inheritance hierarchy can help to improve code readability, maintainability, and flexibility. When making adjustments to the inheritance hierarchy, consider using composition, interfaces, and refactoring to achieve a better design.