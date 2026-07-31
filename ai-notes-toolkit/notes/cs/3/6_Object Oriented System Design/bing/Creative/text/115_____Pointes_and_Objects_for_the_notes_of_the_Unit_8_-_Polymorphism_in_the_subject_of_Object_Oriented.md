### Pointers and Objects for the notes of the Unit 8 - Polymorphism in the subject of Object Oriented System Design

- Polymorphism is one of the core concepts of object-oriented programming (OOP) and describes situations in which something occurs in several different forms.
- In computer science, it describes the concept that you can access objects of different types through the same interface.
- Polymorphism has two distinct aspects: **static** and **dynamic**.
- Static polymorphism, also known as **compile-time** polymorphism, is when the type of the object is determined at compile time. For example, function overloading and operator overloading are forms of static polymorphism.
- Dynamic polymorphism, also known as **run-time** polymorphism, is when the type of the object is determined at run time. For example, virtual functions and inheritance are forms of dynamic polymorphism.
- Pointers are variables that store the address of another variable or object in memory. Pointers can be used to access objects of different types through the same interface, which enables polymorphism.
- For example, consider a base class `Shape` and two derived classes `Circle` and `Square`. We can declare a pointer of type `Shape` and assign it the address of an object of type `Circle` or `Square`. Then, we can use the pointer to invoke the appropriate method on the object, such as `area()` or `perimeter()`, depending on the actual type of the object.
- This way, we can achieve polymorphism using pointers and objects in object-oriented system design.