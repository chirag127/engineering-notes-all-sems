### Adjustment of inheritance

- Adjustment of inheritance is a technique of object design that aims to increase the amount of inheritance in the class structure .
- Inheritance is a mechanism of object-oriented programming that allows a class to reuse, extend, and modify the behavior defined in another class.
- Inheritance can improve the reusability, maintainability, and extensibility of the code by reducing duplication and enhancing abstraction.
- Adjustment of inheritance involves the following steps  :
  - Rearrange and adjust classes and operations to increase inheritance. This may include moving common attributes and methods to a superclass, creating new subclasses, or changing the inheritance hierarchy.
  - Abstract common behavior out of groups of classes. This may involve defining abstract classes or interfaces that capture the essential features of a set of related classes, and making those classes implement or inherit from them.
  - Use delegation to share behavior when inheritance is semantically invalid. This means using composition instead of inheritance when the relationship between classes is not a "is-a" type, but rather a "has-a" or "uses-a" type. For example, a car is not a type of engine, but it has an engine and uses its methods.
- Adjustment of inheritance can affect the depth of inheritance, which is a code metric that measures the maximum length from a class to the root of the inheritance tree. A high depth of inheritance may indicate a complex and fragile design, while a low depth of inheritance may indicate a lack of abstraction and reusability. A balanced depth of inheritance is desirable for a good object design.