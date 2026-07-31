# Inheritance in Scala

Inheritance is a fundamental concept in object-oriented programming that allows the creation of hierarchical classifications. In Scala, inheritance works in a similar way to other object-oriented languages such as Java.

Here are some key points to remember about inheritance in Scala:

1. In Scala, a class can inherit from another class using the `extends` keyword. For example, `class Dog extends Animal` means that the `Dog` class is a subclass of the `Animal` class.

2. A subclass inherits all the non-private members (fields and methods) of its superclass.

3. A subclass can override a method of its superclass by defining a method with the same name and signature. The `override` keyword must be used to indicate that the method is intended to override a method in the superclass.

4. Scala supports single class inheritance, meaning that a class can only extend one other class. However, a class can implement multiple traits, which is similar to multiple inheritance in other languages.

5. The primary constructor of a subclass must call the primary constructor of its superclass. This is done by placing the arguments for the superclass constructor after the `extends` keyword. For example, `class Dog(name: String, age: Int) extends Animal(name, age)`.

6. In Scala, the `super` keyword is used to refer to the superclass of the current object. It can be used to call methods or access fields of the superclass.

7. A subclass can also define its own fields and methods, in addition to those inherited from its superclass.

Inheritance is a powerful tool that allows for code reuse and the creation of complex class hierarchies. It is an important concept to understand when working with object-oriented programming in Scala.