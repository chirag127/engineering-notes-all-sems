### Destructors

- A destructor is a special type of method that is invoked automatically just before the memory of the object is released.
- The purpose of a destructor is to free the extra allocated space by the memory and perform any cleanup tasks.
- A destructor has the same name as the class with which it is associated, but with a tilde (~) prefix in C++  and a ~this() name in D.
- A destructor does not have arguments, return type, static or const modifiers.
- A destructor cannot be inherited or overloaded.
- A destructor is usually used to deallocate memory and other resources allocated by the constructor or other methods.
- A destructor can be explicitly called by the programmer, but it is not recommended as it may cause undefined behavior.
- A destructor is different from a deconstructor, which is not a standard term in object-oriented programming, but may refer to a method that breaks down an object into simpler components.