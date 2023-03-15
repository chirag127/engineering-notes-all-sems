## Unit 7 - Inheritance

- Inheritance is a mechanism that allows a class to inherit the properties and methods of another class.
- The class that inherits is called the **subclass** or the **child class**.
- The class that is inherited from is called the **superclass** or the **parent class**.
- Inheritance enables code reuse and polymorphism.
- Code reuse means that a subclass can use the existing code of the superclass without having to rewrite it.
- Polymorphism means that a subclass can modify or override the behavior of the superclass to suit its own needs.
- Inheritance can be implemented using the **extends** keyword in Java.
- For example, `class Dog extends Animal` means that the Dog class inherits from the Animal class.
- A subclass can access the public and protected members of the superclass, but not the private members.
- A subclass can also define its own members that are specific to its type.
- A subclass can invoke the constructor of the superclass using the **super** keyword.
- For example, `super(name, age)` means that the subclass calls the superclass constructor with the name and age parameters.
- A subclass can override the methods of the superclass using the **@Override** annotation.
- For example, `@Override public void makeSound()` means that the subclass defines its own implementation of the makeSound method that was inherited from the superclass.
- A subclass can also call the superclass method using the **super** keyword.
- For example, `super.makeSound()` means that the subclass invokes the superclass method inside its own method.