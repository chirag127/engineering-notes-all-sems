### Points and Objects for the notes of the Unit 8 - Polymorphism in the subject of Object Oriented System Design

Polymorphism is a fundamental concept of object-oriented programming that allows objects to take on multiple forms, depending on the context in which they are used. In this unit, we will discuss pointers and objects in the context of polymorphism.

Here are some important points to keep in mind:

- A pointer is a variable that holds the memory address of another variable. Pointers are used extensively in C++ to manipulate objects and their data.
- Pointers are declared using the `*` operator, and can be initialized to the address of an existing object using the `&` operator.
- Dereferencing a pointer means accessing the value stored at the memory address pointed to by the pointer. This is done using the `*` operator.
- Polymorphism can be achieved through the use of pointers to base class objects. This allows different derived classes to be treated as if they were of the same type, allowing for more flexible and modular code.
- Virtual functions are a key component of polymorphism. They allow derived classes to override the behavior of base class functions, ensuring that the correct function is called at runtime based on the type of object being used.
- The `virtual` keyword is used to declare a function as virtual in the base class. This allows derived classes to override the function's behavior.
- The `override` keyword is used in derived classes to indicate that the function is intended to override a virtual function in the base class.
- When using polymorphism, it is important to ensure that the base class destructor is virtual. This ensures that the correct destructor is called when deleting objects of derived classes through a base class pointer.
- Object slicing is a potential issue when using polymorphism. This occurs when a derived class object is copied to a base class object, and the derived class-specific data is lost in the process.
- To avoid object slicing, pointers to objects should be used instead of objects themselves. This allows for polymorphic behavior while retaining the specific data of the derived class.

In summary, pointers and objects are essential components of polymorphism in object-oriented programming. By using pointers to base class objects and virtual functions, we can achieve more flexible and modular code that can handle multiple types of objects with ease. However, care must be taken to avoid object slicing and ensure that the correct functions and destructors are called at runtime.