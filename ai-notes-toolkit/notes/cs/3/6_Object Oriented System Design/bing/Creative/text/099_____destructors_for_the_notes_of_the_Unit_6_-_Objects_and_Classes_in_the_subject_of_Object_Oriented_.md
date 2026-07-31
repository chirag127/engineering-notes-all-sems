### Destructors

- A destructor is a special member function of a class that is executed whenever an object of that class goes out of scope or is explicitly destroyed by a call to delete.
- A destructor has the same name as the class, preceded by a tilde (~).
- A destructor has no parameters and no return type.
- A destructor cannot be inherited, overloaded, or virtual, except for the base class destructor, which can be virtual.
- A destructor is used to release any resources allocated by the object, such as memory, file handles, sockets, etc.
- A destructor is automatically invoked by the compiler when the object is destroyed, either by going out of scope, or by an explicit call to delete.
- A destructor can also be explicitly invoked by the programmer using the scope resolution operator (::) followed by the class name and a tilde (~).
- A destructor should not throw any exceptions, because there is no way to handle them if the object is being destroyed by the compiler.
- A destructor should not perform any complex operations, such as calling other functions, allocating memory, or accessing global variables, because the state of the program may be unstable when the object is being destroyed.
- A destructor should not access any members of other objects that may have already been destroyed, because this may cause undefined behavior or memory corruption.
- A destructor should not call the destructor of its base class explicitly, because the compiler will do that automatically after executing the derived class destructor.
- A destructor should not call the destructor of its members explicitly, because the compiler will do that automatically after executing the class destructor.
- A destructor should not call the destructor of any object that is not owned by the class, such as a pointer or a reference, because this may cause double deletion or memory leaks.
- A destructor should not modify any static or global variables, because this may affect other objects that are still alive or that will be created later.
- A destructor should not create any new objects, because this may cause memory leaks or circular dependencies.