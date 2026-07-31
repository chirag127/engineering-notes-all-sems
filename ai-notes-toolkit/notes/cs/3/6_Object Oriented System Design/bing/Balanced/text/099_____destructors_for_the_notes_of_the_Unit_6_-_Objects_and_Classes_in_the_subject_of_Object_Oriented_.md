### Destructors

- A destructor is a special member function of a class that is executed whenever an object of that class goes out of scope or is explicitly destroyed by a call to delete.
- A destructor has the same name as the class, preceded by a tilde (~).
- A destructor has no parameters and no return type.
- A destructor cannot be inherited, overloaded, or virtual, except for the base class destructor, which can be virtual to ensure proper deletion of derived class objects through base class pointers.
- A destructor is used to release any resources allocated by the object, such as memory, files, sockets, etc.
- A destructor is automatically invoked by the compiler at the end of the block in which the object is created, or when the object is deleted by the programmer using the delete operator.
- A destructor can also be explicitly called by the programmer, but this is not recommended as it may cause undefined behavior if the object is accessed after its destruction.
- A destructor should not throw any exceptions, as this may cause memory leaks or program termination.
- A destructor should not perform any complex operations, such as calling other functions, allocating memory, or using I/O, as this may cause unexpected errors or side effects.
- A destructor should be simple, fast, and safe, and only perform the necessary cleanup for the object.