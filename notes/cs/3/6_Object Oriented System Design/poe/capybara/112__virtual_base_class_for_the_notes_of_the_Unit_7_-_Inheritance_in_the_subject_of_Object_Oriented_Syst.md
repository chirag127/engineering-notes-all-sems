### Virtual Base Class for the Notes of Unit 7 - Inheritance in the Subject of Object Oriented System Design

Inheritance is one of the fundamental concepts of Object Oriented System Design. It allows a subclass to inherit properties and behavior from its superclass. Inheritance creates a hierarchy of classes, where a subclass is a specialized version of its superclass.

A virtual base class is a class that acts as a common ancestor for two or more classes. When a class inherits from a virtual base class, it shares a common copy of the base class with its sibling classes. This prevents the creation of multiple instances of the virtual base class in the object hierarchy.

Here are some key points to remember about virtual base class in the context of Unit 7 - Inheritance:

- A virtual base class is declared using the `virtual` keyword in the base class declaration.
- A class that inherits from a virtual base class must use the `virtual` keyword in its own declaration.
- A virtual base class is only constructed once and shared among all classes that inherit from it.
- Virtual base classes are used to avoid the "diamond problem" of multiple inheritance.
- The order of construction of virtual base classes is determined by the order of inheritance in the class hierarchy.

In summary, a virtual base class is an important concept in inheritance and object-oriented design. It allows for the creation of a common ancestor for multiple classes, reducing code duplication and ensuring consistency in the object hierarchy.