Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of virtual and pure virtual functions for the notes of the Unit 8 - Polymorphism in the subject of Object Oriented System Design.

### Virtual and Pure Virtual Functions

- Virtual functions are member functions of a class that can be overridden by derived classes.
- Virtual functions enable dynamic polymorphism, which means that the appropriate function to be executed is determined at run-time based on the type of the object pointed by the base class pointer.
- Virtual functions are declared using the keyword `virtual` in the base class and can be redefined in the derived classes with the same signature and return type.
- Virtual functions are resolved using a mechanism called virtual table (vtable), which is a table of function pointers that is maintained for each class that has virtual functions. Each object of such a class has a pointer to the vtable of its class, called vptr.
- When a virtual function is called through a base class pointer, the compiler inserts code to look up the vtable of the object pointed by the pointer and then invokes the function pointed by the corresponding entry in the vtable.
- Pure virtual functions are virtual functions that have no definition in the base class and are declared with a pure specifier (`= 0`) at the end of the declaration.
- Pure virtual functions are used to create abstract classes, which are classes that cannot be instantiated and only serve as base classes for other classes.
- Pure virtual functions must be overridden by all the concrete derived classes, otherwise the derived classes will also become abstract and cannot be instantiated.
- Pure virtual functions enable pure abstract polymorphism, which means that the base class only defines the interface for the derived classes and does not provide any implementation.
- Pure virtual functions can have a definition in the base class, but it is not required. The definition can be provided outside the class declaration using the scope resolution operator (`::`).
- If a pure virtual function has a definition in the base class, it can be invoked by the derived classes using the scope resolution operator and the base class name, such as `Base::func()`.