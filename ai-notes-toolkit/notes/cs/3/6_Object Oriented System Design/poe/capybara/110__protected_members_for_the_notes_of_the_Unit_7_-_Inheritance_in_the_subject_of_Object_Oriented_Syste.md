### Protected Members for the Notes of Unit 7 - Inheritance in the Subject of Object Oriented System Design

Inheritance is an important concept in Object Oriented System Design. It allows a class to inherit properties and behavior from another class. Protected members are an important part of inheritance. Here are some key points to keep in mind regarding protected members:

- Protected members are accessible within the class and its subclasses only. They cannot be accessed by code outside of the class hierarchy.
- Protected members can be used to implement the "is-a" relationship between classes. For example, a subclass can inherit protected members from a superclass and use them to implement its own behavior.
- Protected members include both data members and member functions (methods). Data members are typically declared as protected to prevent direct access from outside of the class hierarchy. Member functions are declared as protected to allow subclasses to use them in their own implementation.
- Protected members can be overridden in subclasses. This means that a subclass can provide its own implementation of a protected member that is different from the implementation in the superclass.
- Protected members are often used in conjunction with public members to provide a well-defined interface for a class hierarchy. Public members define the interface that is visible to clients of the class hierarchy, while protected members provide the implementation details that are only accessible within the class hierarchy.

In summary, protected members are an important part of inheritance in Object Oriented System Design. They allow subclasses to inherit behavior and properties from a superclass, while still maintaining encapsulation and information hiding. Understanding the use of protected members is essential for designing effective class hierarchies.