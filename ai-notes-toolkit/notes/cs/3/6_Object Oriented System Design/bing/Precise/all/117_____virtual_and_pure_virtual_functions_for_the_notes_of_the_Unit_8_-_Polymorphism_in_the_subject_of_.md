### Unit 8 - Polymorphism in Object Oriented System Design: Virtual and Pure Virtual Functions

- **Virtual functions** are member functions of a class that can be redefined in its derived classes.
- Virtual functions allow for dynamic binding, which means that the function called is determined at runtime based on the type of the object pointed to by the pointer.
- To declare a virtual function, the keyword `virtual` is used in the base class's function declaration.
- The virtual function must be defined in the base class, even if it does not have any implementation.
- When a virtual function is called through a base class pointer, the appropriate function is called based on the type of the object pointed to by the pointer.
- **Pure virtual functions** are virtual functions that have no definition in the base class.
- A pure virtual function is declared by assigning it a value of 0 in the base class.
- A class that contains one or more pure virtual functions is called an **abstract class**.
- An abstract class cannot be instantiated, and its purpose is to provide a common interface for derived classes.
- Derived classes must provide a definition for all pure virtual functions in the base class, otherwise, they will also be abstract classes.
