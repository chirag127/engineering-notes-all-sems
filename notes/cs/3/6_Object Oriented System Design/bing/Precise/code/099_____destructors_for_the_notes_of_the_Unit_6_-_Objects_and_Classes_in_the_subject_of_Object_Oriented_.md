### Destructors

- A destructor is a special member function of a class that is executed whenever an object of its class goes out of scope or is explicitly deleted.
- A destructor has the same name as the class, preceded by a tilde (~).
- Destructors have no return type and cannot take any parameters.
- Destructors can be very useful for releasing resources that the object may have acquired during its lifetime.
- Destructors are called automatically by the system, not by the user.
- The order of destruction is the reverse of the order of construction.
- If a class has a base class with a virtual destructor, its destructor must also be virtual.
- If a class has a virtual destructor, all of its derived classes should also have virtual destructors.
- If a class does not have a virtual destructor, deleting an object of a derived class using a pointer to the base class results in undefined behavior.
- Destructors should not throw exceptions. If a destructor throws an exception, the behavior is undefined.