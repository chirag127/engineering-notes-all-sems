### Inheritance in Scala

Inheritance is a fundamental concept in object-oriented programming that allows the creation of hierarchical classifications. In Scala, inheritance works in a similar way to other object-oriented languages such as Java.

Here are some key points to remember about inheritance in Scala:

1. Inheritance allows a class to inherit the members (fields and methods) of another class.
2. The class that inherits from another class is called a subclass, derived class, or child class.
3. The class that is inherited from is called a superclass, base class, or parent class.
4. In Scala, a class can only inherit from one superclass. This is known as single inheritance.
5. To inherit from a superclass, the subclass uses the `extends` keyword.
6. The subclass can override the members of the superclass by using the `override` keyword.
7. The subclass can also add new members that are not present in the superclass.
8. In Scala, all classes inherit from a common superclass called `Any`.
9. The `Any` class defines several methods that are common to all objects, such as `equals`, `hashCode`, and `toString`.
10. Scala also has a special class called `AnyRef` that is the superclass of all reference types (i.e., all classes that are not primitive types).
11. In addition to inheritance, Scala also supports a form of multiple inheritance called mixin composition. This allows a class to inherit from multiple traits (similar to interfaces in Java) by using the `with` keyword.
