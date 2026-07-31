### Destructors

- A destructor is a special type of method that is invoked automatically just before the memory of the object is released  .
- The purpose of a destructor is to free the extra allocated space by the memory and perform any cleanup tasks .
- A destructor has the same name as the class with which it is associated, but with a tilde (~) prefix in C++ , and with the keyword `__del__` in Python.
- A destructor cannot be declared static or const, and it does not have arguments or return type.
- A destructor cannot be explicitly called by the programmer, it is automatically called by the system.
- A class can have only one destructor, and it is usually defined in the public section of the class.
- A destructor is different from a deconstructor, which is not a standard term in object-oriented programming, but may refer to a method that breaks down an object into its constituent parts.