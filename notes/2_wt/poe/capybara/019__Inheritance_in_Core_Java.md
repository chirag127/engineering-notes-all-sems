#### Inheritance in Core Java

Inheritance is an important feature of object-oriented programming that allows one class to inherit the properties and methods of another class. In Core Java, the inheritance is achieved through the use of the `extends` keyword.

Here are some important points to note about inheritance in Core Java:

- A class that is derived from another class is called a subclass or child class, and the class that is being inherited from is called the superclass or parent class.
- The subclass can access all the variables and methods of the superclass, but the superclass cannot access the variables and methods of the subclass.
- In Java, a subclass can only inherit from one superclass, but a superclass can have multiple subclasses.
- The `Object` class is the ultimate superclass of all classes in Java. If a class does not explicitly extend another class, it implicitly extends the `Object` class.
- The `protected` access modifier is used to allow subclasses to access the variables and methods of the superclass, while still preventing direct access from other classes.
- Inheritance can be used to create a hierarchy of classes that share common functionality, with each subclass adding or modifying the behavior of the superclass.
- The `super` keyword is used to refer to the superclass from within a subclass. It can be used to call the superclass constructor, access the superclass variables, and invoke the superclass methods.
- The `final` keyword can be used to prevent a class from being inherited, or a method from being overridden in a subclass.

In conclusion, inheritance is a powerful feature of Core Java that allows for the creation of complex class hierarchies and the sharing of common functionality between classes. Understanding inheritance is essential for any Java developer who wants to create robust and maintainable code.