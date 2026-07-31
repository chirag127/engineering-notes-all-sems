#### Inheritance in Core Java

- Inheritance is a mechanism that allows one class to acquire the properties and behaviors of another class.
- The class that inherits from another class is called the subclass or derived class.
- The class that is inherited by another class is called the superclass or base class.
- Inheritance enables code reuse, polymorphism, and abstraction.
- In Java, inheritance is achieved by using the `extends` keyword.
- A subclass can inherit from only one superclass in Java, but a superclass can have multiple subclasses.
- A subclass inherits all the public and protected members of its superclass, but not the private members.
- A subclass can access the inherited members directly, or override them to provide its own implementation.
- A subclass can also define new members that are not present in its superclass.
- A subclass can use the `super` keyword to refer to its immediate superclass, and invoke its constructors and methods.
- A subclass can also use the `this` keyword to refer to itself, and invoke its own constructors and methods.
- Java supports multiple levels of inheritance, where a subclass can inherit from another subclass, and so on.
- Java also supports a special type of inheritance called interface inheritance, where a class can implement one or more interfaces that declare abstract methods.
- A class that implements an interface must provide concrete implementations for all the abstract methods declared in the interface, or be declared as abstract itself.
- A class can implement multiple interfaces, but an interface can extend only one other interface.
- A class that implements an interface can also inherit from another class, and vice versa.
- A class that implements an interface can use the `implements` keyword, and an interface that extends another interface can use the `extends` keyword.