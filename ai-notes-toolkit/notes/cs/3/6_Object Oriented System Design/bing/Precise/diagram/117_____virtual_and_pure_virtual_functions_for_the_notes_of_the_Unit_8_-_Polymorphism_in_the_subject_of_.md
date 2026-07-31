### Unit 8 - Polymorphism in Object Oriented System Design
#### Virtual and Pure Virtual Functions

1. **Virtual functions** are member functions of a class that can be redefined in its derived classes.
2. The virtual keyword is used to declare a virtual function.
3. Virtual functions are used to achieve runtime polymorphism.
4. A virtual function is defined in the base class and can be overridden by the derived class.
5. The function resolution is done at runtime, based on the type of the object pointed to by the pointer.
6. A **pure virtual function** is a virtual function that has no definition in the base class.
7. A pure virtual function is declared by assigning 0 in the declaration.
8. A class containing a pure virtual function is called an **abstract class**.
9. An abstract class cannot be instantiated, and it is meant to be inherited by other classes.
10. The derived class must override the pure virtual function, otherwise, it will also become an abstract class.
