#### Inheritance in Scala

Inheritance is one of the fundamental concepts of object-oriented programming. It is a mechanism that allows a class to inherit properties and behaviors from another class. In Scala, inheritance is achieved using the `extends` keyword.

Here are some important points to keep in mind while working with inheritance in Scala:

1. Inheritance is used to create a hierarchy of classes, where the child class (also known as a subclass) inherits properties and behaviors from the parent class (also known as a superclass).

2. The `extends` keyword is used to indicate that a class is inheriting from another class. For example, `class Child extends Parent`.

3. In Scala, a class can only inherit from one parent class. Multiple inheritance is not supported, but we can achieve similar functionality using traits (which we'll discuss in a separate topic).

4. The subclass can access all the public and protected members of the superclass. Private members are not accessible.

5. Constructors of the superclass are also inherited by the subclass. When creating an instance of the subclass, the constructor of the superclass is called first, followed by the constructor of the subclass.

Here are some mnemonics and learning tricks that can be helpful when working with inheritance in Scala:

1. "extends" sounds like "stretching" - just like we stretch our arms to borrow something from someone, a subclass stretches itself to borrow properties and behaviors from a superclass.

2. Think of a family tree - just like how children inherit traits from their parents, a subclass inherits properties and behaviors from a superclass.

Overall, inheritance is an important concept in object-oriented programming, and understanding how it works in Scala is essential for building robust and maintainable applications.