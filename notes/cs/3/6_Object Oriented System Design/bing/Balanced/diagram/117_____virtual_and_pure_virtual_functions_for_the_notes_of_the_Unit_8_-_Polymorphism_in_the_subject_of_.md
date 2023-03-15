### Virtual and Pure Virtual Functions

- Virtual functions are member functions of a class that can be overridden by derived classes.
- Virtual functions enable dynamic polymorphism, which means that the appropriate function is called at run time based on the type of the object pointed by the base class pointer.
- Virtual functions are declared with the keyword `virtual` in the base class and can be redefined in the derived classes with or without the keyword `virtual`.
- Virtual functions are resolved using a mechanism called virtual table (vtable), which is a table of function pointers maintained for each class that has virtual functions.
- The vtable is initialized by the compiler with the addresses of the virtual functions of the class. Each object of the class has a pointer to the vtable, called vptr, which is set by the constructor.
- When a virtual function is called through a base class pointer, the compiler inserts code to access the vtable of the object and find the correct function address to call.
- Pure virtual functions are virtual functions that have no definition in the base class and are declared with the syntax `virtual function_name() = 0;`.
- Pure virtual functions are used to create abstract classes, which are classes that cannot be instantiated and only serve as base classes for other classes.
- Abstract classes can have both pure virtual and non-pure virtual functions, as well as data members and constructors.
- Derived classes of abstract classes must override all the pure virtual functions of the base class, otherwise they will also become abstract classes.
- Pure virtual functions enable pure abstract polymorphism, which means that the base class only defines the interface and the derived classes provide the implementation.