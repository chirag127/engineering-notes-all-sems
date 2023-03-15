# Virtual and Pure Virtual Functions

- Virtual functions are member functions of a base class that can be overridden by the derived classes.
- Virtual functions allow polymorphism, which means that the appropriate function is called at run time depending on the type of the object.
- Virtual functions are declared using the `virtual` keyword in the base class and can be redefined in the derived classes without the `virtual` keyword.
- Virtual functions are resolved using a mechanism called **virtual table** or **vtable**, which is a pointer to an array of function pointers that store the addresses of the virtual functions for each class.
- Pure virtual functions are virtual functions that have no definition in the base class and must be defined in the derived classes.
- Pure virtual functions are declared using the `virtual` keyword and a `= 0` at the end of the function declaration in the base class.
- Pure virtual functions make the base class **abstract**, which means that it cannot be instantiated and can only be used as a base for other classes.
- Pure virtual functions ensure that the derived classes provide their own implementation of the function and do not inherit the default behavior from the base class.