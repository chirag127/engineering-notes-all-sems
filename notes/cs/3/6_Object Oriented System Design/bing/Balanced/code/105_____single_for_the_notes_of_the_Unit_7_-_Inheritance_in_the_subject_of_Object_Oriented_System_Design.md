# Unit 7 - Inheritance

- Inheritance is one of the core concepts of object-oriented programming (OOP) languages.
- It is a mechanism where you can to derive a class from another class for a hierarchy of classes that share a set of attributes and methods.
- The class whose members are inherited is called the base class, and the class that inherits those members is called the derived class.
- A derived class can have only one direct base class. However, inheritance is transitive, which means that a derived class inherits all the members of its base class and its base class's base class, and so on.
- Inheritance enables you to create new classes that reuse, extend, and modify the behavior defined in other classes.
- Inheritance also supports the concept of polymorphism, which allows you to use a derived class object as if it were a base class object.
- Inheritance can be implemented in different ways depending on the programming language, such as class-based inheritance or prototype-based inheritance.
- In class-based inheritance, classes are defined using a class declaration or a class expression, and objects are created from classes using the new operator.
- In prototype-based inheritance, objects are created from other objects using a prototype link, and new properties and methods can be added to an object at any time.
- Some of the benefits of inheritance are:
  - Code reuse: You can avoid writing the same code in multiple classes by inheriting common functionality from a base class.
  - Code maintenance: You can make changes in one place (the base class) and affect all the derived classes that inherit from it.
  - Code organization: You can group related classes in a logical hierarchy and use abstract classes to define common interfaces.
- Some of the drawbacks of inheritance are:
  - Tight coupling: Changes in the base class can affect the derived classes in unexpected ways, and derived classes may depend too much on the implementation details of the base class.
  - Complexity: Inheritance can introduce multiple levels of abstraction, which can make the code harder to understand and debug.
  - Inflexibility: Inheritance is a static relationship that cannot be changed at runtime, and some languages do not support multiple inheritance, which limits the design choices.