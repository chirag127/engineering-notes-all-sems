### Virtual and Pure Virtual Functions

Virtual functions are a key feature of object-oriented programming and are used to implement polymorphism. They allow derived classes to override the behavior of base class functions.

- A virtual function is a member function of a class that is declared with the `virtual` keyword.
- When a virtual function is called through a base class pointer or reference, the function that is called is determined by the dynamic type of the object pointed to or referenced.
- This allows derived classes to provide their own implementation of the virtual function, which can be different from the base class implementation.

Pure virtual functions are virtual functions that have no implementation in the base class. They are declared with the `= 0` syntax after the function declaration.

- A class that contains one or more pure virtual functions is called an abstract class.
- Abstract classes cannot be instantiated, and must be derived from in order to be used.
- Derived classes must provide an implementation for all pure virtual functions in the base class, otherwise they will also be abstract.

In summary, virtual functions allow for dynamic dispatch, where the function called is determined at runtime based on the dynamic type of the object. Pure virtual functions are used to create abstract classes, which serve as a base for derived classes to provide their own implementation of the virtual functions. This is a key feature of polymorphism in object-oriented programming.