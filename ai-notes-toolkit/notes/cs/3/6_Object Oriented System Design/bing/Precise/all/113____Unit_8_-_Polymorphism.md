## Unit 8 - Polymorphism

Polymorphism is one of the four fundamental principles of Object-Oriented Programming (OOP). It refers to the ability of a single function or method to operate on multiple types of data. This allows for greater flexibility and reusability of code.

There are two main types of polymorphism: compile-time polymorphism and runtime polymorphism.

1. **Compile-time polymorphism** is achieved through function overloading and operator overloading. Function overloading allows multiple functions with the same name but different signatures (i.e., different number or types of parameters) to be defined within the same scope. Operator overloading allows custom behavior to be defined for operators when applied to user-defined data types.

2. **Runtime polymorphism** is achieved through the use of virtual functions and inheritance. A virtual function is a member function that is declared within a base class and redefined by a derived class. When a derived class object is assigned to a base class pointer or reference, the virtual function call is resolved at runtime based on the dynamic type of the object, rather than its static type.

Polymorphism allows for greater flexibility and reusability of code by enabling a single function or method to operate on multiple types of data. It is an important concept in OOP and is widely used in the design of software systems.