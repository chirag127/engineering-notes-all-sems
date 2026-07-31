#### Inheritance in Core Java

- Inheritance is one of the object-oriented programming concepts in Java     .
- It enables developers to inherit data members and properties from one class to another     .
- It is used when we have an **is-a** relationship between objects   .
- For example, a `Dog` is an `Animal`, so the `Dog` class can inherit from the `Animal` class.
- Inheritance is implemented using the **extends** keyword    .
- For example, `class Dog extends Animal { ... }`
- The class that inherits from another class is called the **subclass** or **child class**    .
- The class that is inherited from is called the **superclass** or **parent class**    .
- A subclass can access the public and protected members of its superclass    .
- A subclass can also override the methods of its superclass to provide a different implementation    .
- For example, the `Dog` class can override the `makeSound()` method of the `Animal` class to return `"Woof"` instead of `"Generic animal sound"`.
- A subclass can also use the **super** keyword to refer to its superclass and invoke its constructor or methods    .
- For example, the `Dog` class can use `super(name, age)` to invoke the constructor of the `Animal` class with the given parameters.
- A subclass can also inherit from multiple interfaces using the **implements** keyword  .
- For example, the `Dog` class can implement the `Pet` and `Runnable` interfaces to provide additional behaviors.
- An interface can also inherit from other interfaces using the **extends** keyword  .
- For example, the `Pet` interface can extend the `Animal` interface to inherit its methods.

- Advantages of inheritance in Java:
  - Code reusability: Inheritance allows for code reuse and reduces the amount of code that needs to be written.
  - Abstraction: Inheritance allows for the creation of abstract classes that define a common interface for a group of subclasses.
  - Class hierarchy: Inheritance creates a natural hierarchy of classes that reflects the real-world entities and relationships.
  - Polymorphism: Inheritance enables polymorphism, which is the ability of an object to take different forms depending on its type.

- Disadvantages of inheritance in Java:
  - Complexity: Inheritance can increase the complexity of the code and make it harder to understand and maintain.
  - Coupling: Inheritance creates a tight coupling between the superclass and the subclass, which can affect the flexibility and modularity of the code.
  - Overriding: Inheritance can lead to overriding issues, where a subclass may unintentionally change the behavior of a superclass method.

- A possible mnemonic to remember the concept of inheritance in Java is:

  - **I**nheritance is **I**mplemented using **I**s-a relationship and **I**nterfaces.
  - **E**xtends is the keyword for **E**xtending a class or an interface.
  - **S**ubclass is the **S**ame as **C**hild class, and **S**uperclass is the **S**ame as **P**arent class.
  - **O**verriding is **O**verwriting the method of the superclass.
  - **U**sing **S**uper is **U**sing the constructor or method of the superclass.
  - **P**olymorphism is **P**ossible with