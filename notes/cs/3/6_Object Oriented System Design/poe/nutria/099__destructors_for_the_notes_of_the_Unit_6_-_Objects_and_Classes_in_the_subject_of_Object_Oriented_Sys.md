
### Destructors for the Notes of the Unit 6 - Objects and Classes in the Subject of Object Oriented System Design

1. Destructors are special member functions of a class which are executed automatically when an object of the class goes out of scope or is explicitly deleted.
2. Destructors are used to free up resources that were allocated during the lifetime of the object.
3. The destructor of a class is always called when an object of that class is destroyed.
4. The destructor's name is always the same as the class name preceded by a tilde (~).
5. Destructors do not take any arguments, and they cannot return any value.
6. Destructors are called in the reverse order of their constructors.
7. Destructors are not inherited, so if a derived class has a destructor, it must be explicitly declared in that class.
8. A class can have only one destructor.
9. A destructor can be declared as virtual if the class contains any virtual functions.
10. Destructors are useful for releasing any resources that were allocated during the lifetime of the object such as memory, file handles, etc.