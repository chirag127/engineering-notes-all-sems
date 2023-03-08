 Here are the notes for Unit 7 - Inheritance in Object Oriented System Design:

### Inheritance

Inheritance is an important concept in Object Oriented Programming. It is a mechanism in which one class acquires the properties and behaviors of another class.

- The class that inherits the properties from another class is called a `Subclass` or `Child Class`.
- The class that allows its properties to be inherited is called a `Superclass` or `Base Class` or `Parent Class`.

#### Advantages of Inheritance

- Code Reusability - The code of the superclass can be reused by the subclass.
- Reduces duplication of code.
- Provides abstraction. The subclass inherits the traits of the superclass and can modify or extend the behavior.
- Simplifies maintenance. If the superclass changes, the change automatically reflects in the subclass.

#### Disadvantages of Inheritance

- The inheritance hierarchy can become complex with many levels of inheritance which can make the code hard to understand and debug.
- The private members of the superclass are not accessible in the subclass which can be a limitation at times.
- The subclass is tightly coupled with the superclass. If the superclass changes, the subclass is also affected.

#### Types of Inheritance

- Single Inheritance - A subclass can inherit from only one superclass.
- Multi-level Inheritance - A subclass can inherit from another subclass which in turn inherits from the superclass.
- Hierarchical Inheritance - More than one subclass inherits from the same superclass.
- Multiple Inheritance - A subclass can inherit properties from multiple superclasses.

[Details and examples of types of inheritance with diagrams can be added here]

Applications of Inheritance:

- Used to model `is-a` relationship. For example, `Square` is a `Shape`, so Square can inherit from Shape.
- Code reusability and reduced duplication.
- Providing abstraction. The subclass can override/extend the methods of the superclass.
- Developing frameworks where inheritance can be extensively used.

[More applications and examples can be added here with codes]