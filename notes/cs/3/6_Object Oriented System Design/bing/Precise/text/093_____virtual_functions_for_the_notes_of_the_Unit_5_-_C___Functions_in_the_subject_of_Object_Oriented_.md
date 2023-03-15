### Virtual Functions

Virtual functions are a powerful feature of C++ that allows for runtime polymorphism. They are member functions of a class that can be redefined in derived classes. When a derived class redefines a virtual function, the function is said to be "overridden."

Here are some key points to remember about virtual functions:

1. Virtual functions are declared in the base class using the `virtual` keyword.
2. A virtual function can be redefined in a derived class by providing a new implementation with the same signature.
3. When a virtual function is called on an object, the version of the function that is executed is determined by the type of the object at runtime, not by the type of the pointer or reference used to call the function.
4. Virtual functions are typically used to provide a common interface for a group of related classes, allowing objects of different types to be treated interchangeably.
5. The `virtual` keyword is not required when redefining a virtual function in a derived class, but it is good practice to include it for clarity.
6. A virtual function can be declared as `= 0` in the base class to make it a pure virtual function. This means that the base class cannot be instantiated and must be derived from in order to be used.
7. Virtual functions can be called from constructors or destructors, but the version of the function that is called is determined by the type of the object being constructed or destroyed, not by the type of the object at runtime.
