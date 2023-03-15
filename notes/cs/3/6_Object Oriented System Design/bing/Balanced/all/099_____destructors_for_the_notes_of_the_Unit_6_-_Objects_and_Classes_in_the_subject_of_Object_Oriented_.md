### Destructors

- A destructor is a special member function of a class that is executed whenever an object of that class goes out of scope or is explicitly destroyed by a call to delete.
- A destructor has the same name as the class, preceded by a tilde (~).
- A destructor takes no arguments and has no return type.
- A destructor is used to release any resources allocated by the object, such as memory, file handles, sockets, etc.
- A destructor can be declared as virtual, which means that the appropriate destructor will be called depending on the type of the object pointed by a base class pointer.
- A destructor can also be declared as pure virtual, which means that the class is abstract and cannot be instantiated.
- A destructor can be inherited from a base class, but it cannot be overloaded or overridden by a derived class.
- A destructor can call other member functions of the class, but it cannot access any static data members of the class.
- A destructor can throw an exception, but it is not recommended as it may cause undefined behavior if the exception is not caught.