### Adjustment of inheritance

- Adjustment of inheritance is a technique of object design that aims to increase the amount of inheritance in a class hierarchy by modifying the definitions of classes and operations .
- Inheritance is a mechanism of object-oriented programming that allows a class to reuse, extend, and modify the behavior defined in another class, called the base class or the superclass.
- Inheritance can improve the reusability, extensibility, and maintainability of code by avoiding duplication and enabling polymorphism.
- Adjustment of inheritance can be done by following these steps  :
  - Rearrange and adjust classes and operations to increase inheritance. This can involve moving common attributes and methods to a superclass, or creating new superclasses or subclasses to group related classes.
  - Abstract common behavior out of groups of classes. This can involve defining abstract classes or interfaces that specify the common behavior of subclasses, or using design patterns such as template method or strategy to encapsulate common algorithms.
  - Use delegation to share behavior when inheritance is semantically invalid. This can involve using composition or aggregation to associate a class with another class that provides the desired behavior, or using design patterns such as adapter or decorator to modify the behavior of an existing class.
- Adjustment of inheritance should consider the trade-offs between the benefits and costs of inheritance. Some of the factors that affect the trade-offs are:
  - Depth of inheritance: the number of levels in the class hierarchy. A deeper inheritance tree can increase the reusability and extensibility of code, but also increase the complexity and coupling of the system.
  - Width of inheritance: the number of subclasses in each level of the class hierarchy. A wider inheritance tree can increase the flexibility and polymorphism of the system, but also increase the redundancy and ambiguity of the code.
  - Stability of inheritance: the frequency and extent of changes in the class hierarchy. A stable inheritance tree can improve the maintainability and reliability of the system, but also limit the adaptability and evolution of the code.