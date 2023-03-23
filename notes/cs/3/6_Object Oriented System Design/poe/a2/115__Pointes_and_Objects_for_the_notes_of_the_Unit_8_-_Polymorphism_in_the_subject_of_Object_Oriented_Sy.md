 Here are the notes in markdown format with points on the topic of Polymorphism for Unit 8 of Object Oriented System Design:

### Pointes on Polymorphism

1. Polymorphism means having many forms. In OOP, polymorphism means that a call to a member function will cause a different function to be executed depending on the type of object that invokes the function.
2. Polymorphism can be of two types:
- Compile time Polymorphism: Achieved through function overloading and operator overloading.
- Runtime Polymorphism: Achieved through virtual functions. The overriding function is called based on the type of the object referred by the pointer or reference at runtime.
3. Virtual Functions: A virtual function is a member function that is declared within a base class and redefined by a derived class. To declare a virtual function, simply precede it with the virtual keyword.
4. Overriding: In the case of runtime polymorphism, a derived class function can override a base class function. The base class function doesn't cease to exist, but its functionality is superseded by the new definition. The override is resolved at run time based on the type of object.

Objects for Study:
1. Study pointers, references, base and derived classes, and virtual functions to understand runtime polymorphism.
2. Study function overloading and operator overloading to understand compile time polymorphism.
3. Code examples of overriding base class functions in derived class and calling them through base class pointer to see runtime polymorphism in action.
4. Do exercises involving polymorphism to get a strong grip on the concept.

Let me know if you would like me to elaborate on any of the points or add additional points and objects.