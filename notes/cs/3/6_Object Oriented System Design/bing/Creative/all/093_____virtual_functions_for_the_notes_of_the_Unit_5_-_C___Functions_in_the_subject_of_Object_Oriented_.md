# Virtual Functions in C++

- A virtual function is a member function of a class that can be redefined in a derived class using the same signature and return type  .
- A virtual function is declared using the `virtual` keyword in the base class  .
- A virtual function allows the compiler to perform dynamic linkage or late binding on the function call, which means the function to be executed is determined at run time based on the type of the object pointed by the base class pointer   .
- A virtual function is used to achieve runtime polymorphism, which is the ability of an object to behave differently depending on its actual class  .
- A virtual function can be overridden in a derived class using the same signature and return type as the base class function    .
- A virtual function can be declared as `override` in a derived class to explicitly indicate that the function is overriding a base class function .
- A virtual function can be declared as `final` in a base class or a derived class to prevent further overriding by any other derived class.
- A virtual function can be declared as `pure` in a base class by assigning it a value of zero, which makes the base class abstract and forces the derived classes to provide a definition for the function  .
- A virtual function can be invoked using a base class pointer or reference that points to or refers to a derived class object    .
- A virtual function can also be invoked using the scope resolution operator `::` to specify the class name and the function name, which bypasses the dynamic linkage and calls the function of the specified class .