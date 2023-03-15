## Unit 7 - Inheritance

- Inheritance is a mechanism that allows a class to inherit the properties and methods of another class.
- The class that inherits is called the **subclass** or **child class**. The class that is inherited from is called the **superclass** or **parent class**.
- Inheritance enables code reuse and polymorphism. Code reuse means that a subclass can use the existing code of the superclass without having to rewrite it. Polymorphism means that a subclass can modify or override the behavior of the superclass to suit its own needs.
- Inheritance is implemented using the **extends** keyword in Java. For example, `class Dog extends Animal` means that the Dog class inherits from the Animal class.
- A subclass inherits all the public and protected members of the superclass, but not the private members. Members are the fields and methods of a class.
- A subclass can access the inherited members directly, or use the **super** keyword to refer to the superclass. For example, `super.name` refers to the name field of the superclass.
- A subclass can also declare its own members, which are unique to the subclass. These members are not inherited by any other class.
- A subclass can override the inherited methods of the superclass by providing a new implementation with the same name and signature. For example, `public void makeSound()` is an overridden method in the Dog class if it is inherited from the Animal class.
- A subclass can also overload the inherited methods of the superclass by providing a new implementation with the same name but different parameters. For example, `public void makeSound(String sound)` is an overloaded method in the Dog class if it is inherited from the Animal class.
- A subclass can invoke the overridden or overloaded methods of the superclass by using the **super** keyword. For example, `super.makeSound()` calls the makeSound method of the Animal class from the Dog class.
- A subclass can also inherit from another subclass, forming a hierarchy of classes. For example, `class Labrador extends Dog` means that the Labrador class inherits from the Dog class, which in turn inherits from the Animal class.
- A subclass can only inherit from one superclass in Java, which is called **single inheritance**. However, a subclass can implement multiple interfaces, which is called **multiple inheritance**. Interfaces are a way of defining the behavior of a class without providing the implementation.