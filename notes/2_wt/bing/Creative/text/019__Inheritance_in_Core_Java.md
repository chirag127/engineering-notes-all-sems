#### Inheritance in Core Java

- Inheritance is one of the core principles of Object-Oriented Programming (OOP) in Java.
- It is the mechanism by which one class can inherit the features (fields and methods) of another class.
- It enables us to reuse existing code or extend an existing type.
- A class that inherits from another class is called a subclass or a child class.
- A class that is inherited by another class is called a superclass or a parent class.
- A subclass can access the non-static protected and public members of the superclass, as well as the members with default access if they are in the same package.
- A subclass cannot access the private and static members of the superclass.
- A subclass can also define its own fields and methods, or override the methods of the superclass.
- A subclass can use the keyword `super` to refer to the members of the superclass, or to invoke the constructor of the superclass.
- A subclass can use the keyword `extends` to declare that it inherits from a superclass.
- A class can inherit only one superclass in Java, but it can implement multiple interfaces.
- An interface can inherit other interfaces using the keyword `extends`.
- Inheritance supports the concept of polymorphism, which allows us to use a subclass object as a superclass reference.
- Inheritance also supports the concept of abstraction, which allows us to hide the implementation details and show only the functionality to the user.

Some examples of inheritance in Java are:

- The class `Object` is the superclass of all classes in Java.
- The class `String` inherits from the class `Object`.
- The class `Exception` inherits from the class `Throwable`.
- The class `ArrayList` inherits from the class `AbstractList` and implements the interface `List`.
- The interface `List` inherits from the interface `Collection`.
- The interface `Runnable` inherits from the interface `FunctionalInterface`.