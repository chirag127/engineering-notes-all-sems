### Adjustment of inheritance

- Adjustment of inheritance is a technique of object design that aims to increase the amount of inheritance in a class hierarchy by modifying the definitions of classes and operations .
- Inheritance is a mechanism of object-oriented programming that allows a class to inherit the attributes and behaviors of another class, called the base class or the superclass.
- Inheritance can improve the reusability, extensibility, and maintainability of code by avoiding duplication and enabling polymorphism.
- Adjustment of inheritance can be done by following these steps  :
  - Rearrange and adjust classes and operations to increase inheritance. This can involve moving common attributes and operations to a superclass, or creating new superclasses or subclasses to group similar classes.
  - Abstract common behavior out of groups of classes. This can involve defining abstract classes or interfaces that specify the common operations of a group of classes, and making those classes implement or inherit from them.
  - Use delegation to share behavior when inheritance is semantically invalid. This can involve creating helper classes or objects that contain the shared behavior, and delegating the calls to those classes or objects from the classes that need them.
- Adjustment of inheritance should be done carefully, as it can also introduce some drawbacks, such as increased complexity, reduced readability, and increased coupling.
- The depth of inheritance, which is the maximum length from a class to the root of the class hierarchy, is a code metric that can indicate the potential impact of inheritance on the design and quality of code. A high depth of inheritance can indicate a high degree of abstraction and reuse, but also a high risk of errors and maintenance issues.