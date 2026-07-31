### Adjustment of inheritance

- Adjustment of inheritance is a technique of object design that aims to increase the amount of inheritance in a class hierarchy by modifying the definitions of classes and operations .
- Inheritance is a mechanism of object-oriented programming that allows a class to reuse, extend, and modify the behavior defined in another class, called the base class or the superclass.
- Inheritance can improve the reusability, extensibility, and maintainability of code by avoiding duplication and enabling polymorphism.
- However, inheritance can also introduce complexity and coupling in the class hierarchy, especially if the depth of inheritance is too high.
- Therefore, adjustment of inheritance should be done carefully and judiciously, following some guidelines:
  - Rearrange and adjust classes and operations to increase inheritance, but avoid creating unnecessary or artificial classes.
  - Abstract common behavior out of groups of classes, and define abstract classes or interfaces to represent the common behavior.
  - Use delegation to share behavior when inheritance is semantically invalid or impractical. Delegation is a technique of object design that allows an object to use another object to perform a specific task, rather than inheriting from it.
  - Balance the trade-offs between inheritance and delegation, considering factors such as performance, readability, and flexibility.