# Inheritance

Inheritance is an object-oriented concept that allows a class to reuse the features (fields and methods) of another class. The class that inherits the features is called a subclass (or a derived class or a child class). The class that provides the features is called a superclass (or a base class or a parent class).

Scala supports various types of inheritance, such as:

- Single inheritance: A subclass inherits from only one superclass.
- Multilevel inheritance: A subclass inherits from a superclass, which in turn inherits from another superclass, and so on.
- Hierarchical inheritance: A superclass has more than one subclass that inherit from it.
- Multiple inheritance: A subclass inherits from more than one superclass.
- Hybrid inheritance: A combination of multiple and hierarchical inheritance.

Scala does not allow multiple inheritance for classes, but it can be achieved by using traits. Traits are abstract types that can contain fields and methods, and can be mixed in with classes using the `with` keyword. Traits can also extend other traits or classes, forming a linearization of the mixed-in types.

Some important points to remember about inheritance in Scala are:

- To inherit from a superclass, use the `extends` keyword after the subclass name.
- To override a method or a field in a subclass, use the `override` keyword before the method or field definition.
- To access a member of a superclass from a subclass, use the `super` keyword followed by a dot and the member name.
- To prevent a class from being inherited, use the `final` keyword before the class name.
- To prevent a method or a field from being overridden, use the `final` keyword before the method or field definition.
- To create an abstract class, use the `abstract` keyword before the class name. An abstract class can contain abstract methods or fields, which do not have a definition and must be overridden in a subclass.
- To create a trait, use the `trait` keyword before the trait name. A trait can contain concrete or abstract members, and can be mixed in with a class using the `with` keyword.
- To mix in multiple traits with a class, use the `with` keyword after the first trait name and before the next trait name. The order of the traits matters, as the rightmost trait is the first to be inherited, and the leftmost trait is the last to be inherited.