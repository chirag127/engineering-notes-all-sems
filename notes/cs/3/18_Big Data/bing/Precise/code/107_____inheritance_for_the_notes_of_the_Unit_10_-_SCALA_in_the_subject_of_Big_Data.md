### Inheritance in Scala

Inheritance is a mechanism in object-oriented programming that allows a new class to be created based on an existing class. The new class is called a subclass or derived class, and the existing class is called a superclass or base class. The subclass inherits all the members (fields, methods, and nested classes) from its superclass.

Here are some key points to remember about inheritance in Scala:

1. In Scala, a class can only extend one superclass. This is known as single inheritance.
2. A subclass can override methods and fields of its superclass.
3. The `override` keyword is used to explicitly indicate that a method or field is being overridden.
4. The `super` keyword is used to refer to members of the superclass.
5. A subclass can call the constructor of its superclass using the `super` keyword.
6. A subclass can inherit from a superclass using the `extends` keyword.
7. A subclass can inherit from a trait using the `with` keyword.
8. A subclass can inherit from multiple traits using multiple `with` keywords.
9. A subclass can inherit from both a superclass and one or more traits using the `extends` and `with` keywords together.
10. In Scala, all classes inherit from the `Any` class, which is the root of the class hierarchy.
