### Virtual Functions in C++

- A virtual function is a member function of a class that can be redefined in a derived class using the same name and signature  .
- A virtual function is declared using the `virtual` keyword in the base class  .
- A virtual function allows the compiler to perform dynamic binding or late binding, which means the function call is resolved at run time based on the type of the object pointed by the base class pointer   .
- A virtual function is used to achieve runtime polymorphism, which is the ability of an object to behave differently depending on its actual class  .
- A virtual function can be overridden in a derived class using the same name and signature as the base class function . Optionally, the `override` keyword can be used in C++11 to explicitly indicate that the function is overriding a virtual function from the base class.
- A virtual function can be declared as `virtual` in any intermediate class in the inheritance hierarchy, not necessarily in the base class.
- A virtual function can be pure or impure. A pure virtual function is declared as `virtual` followed by `= 0` in the base class, and it has no definition in the base class. A pure virtual function must be overridden in a derived class, otherwise the derived class will also be abstract and cannot be instantiated  . An impure virtual function is declared as `virtual` without `= 0` in the base class, and it has a definition in the base class. An impure virtual function can be overridden in a derived class, but it is not mandatory  .
- A virtual function can be called using a base class pointer or reference that points or refers to a derived class object. The function call will invoke the function definition of the derived class, not the base class  .
- A virtual function can also be called using a base class object or a derived class object directly, without using pointers or references. The function call will invoke the function definition of the class of the object, not the derived class  .
- A virtual function can be inherited by another derived class from the base class or an intermediate class. The inherited virtual function can be overridden again in the new derived class, or it can be inherited as it is.
- A virtual function can be invoked by another member function of the same class or a derived class, or by a friend function of the same class or a derived class.
- A virtual function can be public, protected, or private in the base class. However, the accessibility of the virtual function in the derived class depends on the type of inheritance (public, protected, or private) and the accessibility of the virtual function in the base class.
- A virtual function cannot be static, const, or volatile in the base class or the derived class.
- A virtual function cannot have default arguments in the base class or the derived class, as they can cause ambiguity and inconsistency in the function call.