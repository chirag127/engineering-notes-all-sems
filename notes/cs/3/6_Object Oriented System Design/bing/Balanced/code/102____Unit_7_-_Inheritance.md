Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn or discuss. You have chosen the topic of inheritance in object-oriented programming. Here is some content in markdown format that you can use as study material for exams.

## Unit 7 - Inheritance

- Inheritance is a mechanism that allows a class to acquire the properties and methods of another class.
- The class that inherits from another class is called the **subclass** or **child class**.
- The class that is inherited by another class is called the **superclass** or **parent class**.
- Inheritance enables code reuse, polymorphism, and abstraction.
- Code reuse means that a subclass can use the existing code of a superclass without having to rewrite it.
- Polymorphism means that a subclass can override or modify the behavior of a superclass method to suit its own needs.
- Abstraction means that a subclass can hide the implementation details of a superclass method and provide a simpler interface for the user.

### Syntax of inheritance

- In most object-oriented programming languages, the syntax of inheritance is similar to the following:

```java
class Subclass extends Superclass {
  // subclass fields and methods
}
```

- The keyword `extends` indicates that the subclass inherits from the superclass.
- The subclass can access the public and protected fields and methods of the superclass, but not the private ones.
- The subclass can also declare its own fields and methods, or override the ones inherited from the superclass.

### Types of inheritance

- There are different types of inheritance based on the number and relationship of classes involved. Some of the common types are:

  - **Single inheritance**: A subclass inherits from only one superclass.
  - **Multiple inheritance**: A subclass inherits from more than one superclass. This type of inheritance is not supported by some languages, such as Java, because it can cause ambiguity and complexity.
  - **Multilevel inheritance**: A subclass inherits from a superclass, which in turn inherits from another superclass, and so on. This creates a hierarchy of classes.
  - **Hierarchical inheritance**: More than one subclass inherits from the same superclass. This creates a tree-like structure of classes.
  - **Hybrid inheritance**: A combination of two or more types of inheritance. For example, a subclass can inherit from multiple superclasses, which in turn inherit from a common superclass.

### Advantages and disadvantages of inheritance

- Inheritance has some advantages and disadvantages that should be considered when designing a class hierarchy. Some of the advantages are:

  - It promotes code reuse and reduces duplication.
  - It facilitates polymorphism and abstraction, which make the code more flexible and maintainable.
  - It establishes a natural relationship between classes based on the real-world concepts they represent.

- Some of the disadvantages are:

  - It can create a tight coupling between classes, which makes the code less modular and harder to change.
  - It can introduce complexity and confusion when there are multiple or multilevel inheritance involved.
  - It can violate the principle of encapsulation, which states that a class should hide its internal details and expose only its essential features.