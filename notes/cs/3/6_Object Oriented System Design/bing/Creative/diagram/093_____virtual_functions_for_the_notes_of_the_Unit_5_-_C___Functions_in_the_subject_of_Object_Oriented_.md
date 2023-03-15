### Virtual Functions in C++

- A virtual function is a member function of a class that can be redefined in a derived class using the same name and signature  .
- A virtual function is declared using the `virtual` keyword in the base class  .
- A virtual function allows the compiler to perform dynamic linkage or late binding on the function, which means the function call is resolved at run time based on the type of the object pointed by the base class pointer   .
- A virtual function is used to achieve runtime polymorphism, which is the ability of an object to behave differently depending on its actual class  .
- A virtual function can be overridden in a derived class using the same name and signature as the base class function, and optionally the `override` keyword to indicate that the function is intended to override a base class function .
- A virtual function can be declared as `virtual` in any intermediate class in the inheritance hierarchy, and it will remain virtual in all the derived classes.
- A virtual function can be declared as `final` to prevent any further overriding in the derived classes.
- A virtual function can be declared as `pure virtual` by assigning it a value of zero in the base class, which makes the base class abstract and forces the derived classes to provide a definition for the function  .
- A virtual function can be invoked using a base class pointer or reference that points to or refers to a derived class object  .
- A virtual function can also be invoked using the scope resolution operator `::` to specify the class name and the function name, which bypasses the virtual mechanism and calls the function of that class directly .