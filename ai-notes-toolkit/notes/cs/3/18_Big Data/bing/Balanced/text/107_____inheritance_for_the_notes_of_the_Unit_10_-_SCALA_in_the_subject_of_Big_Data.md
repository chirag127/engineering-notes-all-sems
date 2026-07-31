### Inheritance

Inheritance is an object-oriented concept that allows a class to reuse the features (fields and methods) of another class. The class that inherits the features is called a subclass (or a derived class or a child class). The class that provides the features is called a superclass (or a base class or a parent class).

Scala supports various types of inheritance, such as:

- Single inheritance: A subclass inherits from only one superclass.
- Multilevel inheritance: A subclass inherits from a superclass, which in turn inherits from another superclass, and so on.
- Hierarchical inheritance: A superclass has more than one subclass.
- Multiple inheritance: A subclass inherits from more than one superclass. This is not possible with classes, but can be achieved by using traits.
- Hybrid inheritance: A combination of multiple and hierarchical inheritance. This can also be achieved by using traits.

Some key points to remember about inheritance in Scala are:

- You can use the `extends` keyword to indicate that a class inherits from another class or trait.
- You can use the `override` keyword to modify or replace a member of a superclass in a subclass.
- You can use the `super` keyword to access a member of a superclass from a subclass.
- You can use the `final` keyword to prevent a class from being inherited or a member from being overridden.
- You can use the `sealed` keyword to restrict the subclasses of a class to the same source file.
- You can use the `abstract` keyword to declare a class that cannot be instantiated, but can be inherited by other classes. An abstract class can have abstract members, which are declared without a definition and must be implemented by a subclass.
- You can use the `with` keyword to mix in one or more traits to a class, which allows you to combine the features of multiple superclasses. This is also known as mixin class composition.