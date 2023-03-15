#### Inheritance in Scala

- Inheritance is an important pillar of OOP (Object Oriented Programming).
- It is the mechanism in Scala by which one class is allowed to inherit the features (fields and methods) of another class .
- The class whose features are inherited is known as superclass (or a base class or a parent class).
- The class that inherits the features of the superclass is known as subclass (or a derived class or a child class).
- The subclass can access all the non-private members of the superclass.
- The subclass can also override the methods of the superclass by using the `override` keyword.
- Scala supports various types of inheritance, including single, multilevel, multiple, and hybrid .
- Single inheritance is the most simple form of inheritance, where one subclass inherits from one superclass.
- Multilevel inheritance is the form of inheritance where one subclass inherits from another subclass, which in turn inherits from another superclass, and so on.
- Multiple inheritance is the form of inheritance where one subclass inherits from more than one superclass. This can only be achieved by using traits, which are abstract types that can contain fields and methods.
- Hybrid inheritance is the form of inheritance that combines multiple and multilevel inheritance. This can also only be achieved by using traits.
- Scala also supports abstract classes, which are classes that cannot be instantiated and can contain abstract methods that have no implementation.
- Abstract classes can be inherited by subclasses that provide the implementation for the abstract methods.
- Scala also supports final classes, which are classes that cannot be inherited by any other class. Final classes can be declared by using the `final` keyword.
- Scala also supports sealed classes, which are classes that can only be inherited by classes in the same file. Sealed classes can be declared by using the `sealed` keyword.