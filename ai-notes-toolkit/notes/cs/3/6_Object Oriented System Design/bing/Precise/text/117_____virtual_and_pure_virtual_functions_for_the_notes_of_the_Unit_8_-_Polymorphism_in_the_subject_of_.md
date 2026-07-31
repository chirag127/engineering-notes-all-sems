### Virtual and Pure Virtual Functions

Virtual functions are member functions in a base class that can be overridden by derived classes. They are declared using the `virtual` keyword and are used to implement dynamic polymorphism.

Here are some key points to remember about virtual functions:
- Virtual functions are declared in the base class using the `virtual` keyword.
- A virtual function can be overridden in a derived class by redefining the function with the same signature.
- When a virtual function is called on an object, the function that is called is determined by the dynamic type of the object, not its static type.
- Virtual functions are typically used to provide a common interface for a group of related classes.

Pure virtual functions are virtual functions that have no implementation in the base class. They are declared by setting the function equal to 0 in the base class.

Here are some key points to remember about pure virtual functions:
- Pure virtual functions are declared in the base class using the `virtual` keyword and by setting the function equal to 0.
- A pure virtual function must be overridden in a derived class, otherwise the derived class will also be abstract and cannot be instantiated.
- Pure virtual functions are used to create abstract base classes, which provide a common interface for a group of related classes.
- Abstract base classes cannot be instantiated, they are used only as base classes for other classes.
