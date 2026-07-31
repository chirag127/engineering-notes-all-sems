# Unit 8 - Polymorphism in Object Oriented System Design

## this pointer

- In C++ programming, `this` is a keyword that refers to the current instance of the class.
- Every object in C++ has access to its own address through an important pointer called `this` pointer.
- The `this` pointer is an implicit parameter to all member functions.
- There can be 3 main usage of `this` keyword in C++:
  - To return the current instance of the class from a member function.
  - To access the data members of the current instance of the class when they are hidden by local variables or parameters with the same name.
  - To pass the current instance of the class as an argument to another function.
- The type of `this` pointer in C++ is `ClassName* const`.
- The `this` pointer is constant and cannot be modified.
- The `this` pointer is not available in static member functions as they are not associated with any object.
- The `this` pointer can be used to implement method chaining in C++. Method chaining is a technique of calling multiple methods on the same object in a single statement.
- The `this` pointer can also be used to implement self-referential classes in C++. Self-referential classes are classes that contain a pointer to their own type as a data member. For example, a linked list node class can have a pointer to the next node of the same type.