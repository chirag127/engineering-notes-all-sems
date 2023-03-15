#### Inheritance in Core Java
Inheritance is one of the fundamental concepts of Object-Oriented Programming (OOP) in Java. It allows the creation of hierarchical classifications and enables code reusability. Here are some key points to remember about inheritance in Core Java:

1. Inheritance allows a new class to be created based on an existing class. The new class is called a subclass or derived class, and the existing class is called the superclass or base class.
2. The subclass inherits all the non-private members (fields, methods, and nested classes) from its superclass. This means that the subclass can use the methods and fields defined in the superclass as if they were its own.
3. Inheritance is implemented in Java using the `extends` keyword. The syntax for creating a subclass is `class Subclass extends Superclass { ... }`.
4. A subclass can add new fields and methods to those inherited from the superclass. It can also override the methods of the superclass to provide its own implementation.
5. In Java, all classes inherit from the `Object` class, either directly or indirectly. The `Object` class is the root of the class hierarchy and provides some common methods that all objects can use.
6. Java supports single inheritance, which means that a class can have only one direct superclass. However, a class can implement multiple interfaces, which allows for a form of multiple inheritance.
7. The `super` keyword can be used to access members of the superclass that have been hidden or overridden in the subclass.
8. Constructors are not inherited by subclasses, but a subclass constructor can call a constructor of the superclass using the `super` keyword.

Inheritance is a powerful feature that allows for code reuse and the creation of complex class hierarchies. It is important to use inheritance judiciously and design classes with a clear and logical hierarchy.