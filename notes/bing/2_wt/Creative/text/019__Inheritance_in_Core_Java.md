#### Inheritance in Core Java

- Inheritance is a mechanism that allows one class to acquire the properties and behaviors of another class.
- The class that inherits from another class is called the subclass or derived class, and the class that is inherited from is called the superclass or base class.
- Inheritance is used to achieve code reusability, polymorphism, and abstraction in Java.
- In Java, inheritance is implemented using the `extends` keyword, which specifies that a subclass inherits from a superclass.
- For example, `class Dog extends Animal` means that the Dog class inherits from the Animal class.
- A subclass can access the public and protected members of its superclass, but not the private members.
- A subclass can also override the methods of its superclass, which means that it can provide a different implementation for a method that is already defined in the superclass.
- For example, the Dog class can override the `makeSound()` method of the Animal class and provide a different sound for dogs.
- In Java, a class can only inherit from one superclass, which means that Java does not support multiple inheritance. However, a class can implement multiple interfaces, which are similar to abstract classes that only contain abstract methods and constants.
- For example, `class Dog extends Animal implements Pet, Runnable` means that the Dog class inherits from the Animal class and implements the Pet and Runnable interfaces.