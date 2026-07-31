#### Inheritance in Scala
Inheritance is a fundamental concept in object-oriented programming that allows the creation of hierarchical classifications. Scala, being an object-oriented language, supports inheritance. Here are some key points to remember about inheritance in Scala:

1. Inheritance allows a class to reuse code from another class. In Scala, a class can inherit from another class using the `extends` keyword.
2. A subclass inherits all the non-private members (fields and methods) of its superclass.
3. Constructors are not inherited by subclasses, but a subclass constructor can call a superclass constructor.
4. Scala supports single class inheritance, meaning a class can only inherit from one superclass.
5. Scala also supports multiple inheritance of behavior through traits. A class can inherit behavior from multiple traits using the `with` keyword.
6. A subclass can override a non-private method of its superclass by using the `override` keyword.
7. A subclass can also override a field of its superclass, but this is not common practice.
8. Inheritance creates an `is-a` relationship between the subclass and the superclass. For example, if class `Dog` extends class `Animal`, then a `Dog` is an `Animal`.

These are some of the key points to remember about inheritance in Scala. It is a powerful tool that allows for code reuse and the creation of hierarchical classifications. It is important to use inheritance appropriately and understand its implications in order to write effective and maintainable code.