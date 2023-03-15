## Unit 7 - Inheritance

- Inheritance is a mechanism that allows a class to inherit the properties and methods of another class.
- The class that inherits is called the **subclass** or **child class**. The class that is inherited from is called the **superclass** or **parent class**.
- Inheritance enables code reuse and polymorphism. Code reuse means that a subclass can use the existing code of the superclass without having to rewrite it. Polymorphism means that a subclass can modify or override the behavior of the superclass to suit its own needs.
- In Java, inheritance is achieved by using the **extends** keyword. For example, `class Dog extends Animal` means that the Dog class inherits from the Animal class.
- A subclass inherits all the public and protected members of the superclass, but not the private members. Members are the fields and methods of a class.
- A subclass can access the inherited members directly, or by using the **super** keyword. The super keyword refers to the superclass object and can be used to invoke the superclass constructor or methods.
- A subclass can also declare its own fields and methods that are not present in the superclass. These are called **subclass-specific** members.
- A subclass can override the inherited methods of the superclass by providing a new implementation with the same name and signature. The **@Override** annotation is used to indicate that a method is overridden.
- A subclass can also overload the inherited methods of the superclass by providing a new implementation with a different name or signature. Overloading means having multiple methods with the same name but different parameters.
- A subclass can also inherit from multiple superclasses by using **interfaces**. Interfaces are abstract classes that only declare the methods without providing any implementation. A subclass can implement multiple interfaces by using the **implements** keyword. For example, `class Dog extends Animal implements Pet` means that the Dog class inherits from the Animal class and implements the Pet interface.