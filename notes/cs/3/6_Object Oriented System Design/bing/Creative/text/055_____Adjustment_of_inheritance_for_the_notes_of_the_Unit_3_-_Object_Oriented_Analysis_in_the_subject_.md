### Adjustment of inheritance

- Adjustment of inheritance is a technique of object design that aims to increase the amount of inheritance in a class hierarchy by modifying the definitions of classes and operations .
- Inheritance is a mechanism of object-oriented programming that allows a class to inherit the attributes and behaviors of another class, called the base class or the superclass.
- Inheritance can improve the reusability, extensibility, and maintainability of code by avoiding duplication and enabling polymorphism.
- Adjustment of inheritance can be done by following these steps  :
  - Rearrange and adjust classes and operations to increase inheritance. This can involve moving common attributes and operations to a superclass, or creating new superclasses or subclasses to capture the similarities and differences among classes.
  - Abstract common behavior out of groups of classes. This can involve defining abstract classes or interfaces that specify the common operations that subclasses must implement, or using design patterns such as Template Method or Strategy to encapsulate the common algorithm or behavior.
  - Use delegation to share behavior when inheritance is semantically invalid. This can involve using composition or aggregation to associate a class with another class that provides the desired behavior, or using design patterns such as Adapter or Decorator to modify or enhance the behavior of an existing class.
- Adjustment of inheritance should be done carefully and with consideration of the trade-offs involved. Some of the factors that can affect the decision are:
  - The depth of inheritance, which is the maximum length from a class to the root of the class hierarchy. A deeper inheritance can increase the complexity and coupling of the code, and make it harder to understand and test.
  - The width of inheritance, which is the number of subclasses that a class has. A wider inheritance can increase the flexibility and reuse of the code, but also introduce more variability and inconsistency among the subclasses.
  - The cohesion and coupling of the classes, which are the measures of how well the attributes and operations of a class are related to each other and to other classes. A higher cohesion and a lower coupling can improve the quality and modularity of the code, and make it easier to change and maintain.