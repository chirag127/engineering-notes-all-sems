### Destructors

- A destructor is a special member function of a class that is executed whenever an object of its class goes out of scope or is explicitly deleted.
- The destructor is used to release any resources that the object may have acquired during its lifetime.
- The destructor has the same name as the class, preceded by a tilde (~).
- A class can have only one destructor, and it cannot have any parameters or return any value.
- The destructor is called automatically by the system when the object is destroyed.
- It is good practice to explicitly define a destructor for a class if it acquires resources that need to be released, such as memory or file handles.
- If a class does not define a destructor, the compiler generates a default destructor that does nothing.
- The destructor should not throw an exception. If an exception is thrown, the program may terminate abnormally.
- The order in which destructors are called for objects with static, thread, or automatic storage duration is the reverse of the order in which the constructors for those objects were called.
- If a class is derived from a base class, the destructor of the derived class is called first, followed by the destructor of the base class.
- If a class contains members that are objects of other classes, the destructors for those member objects are called before the destructor for the containing class is called.
- The destructor should release only the resources that the object itself has acquired. It should not release resources that were acquired by other objects or by the program as a whole.