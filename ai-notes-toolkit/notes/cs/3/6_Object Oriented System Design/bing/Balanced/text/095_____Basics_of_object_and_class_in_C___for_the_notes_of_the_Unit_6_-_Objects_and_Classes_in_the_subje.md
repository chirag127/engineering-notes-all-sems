### Basics of object and class in C++

- A class is a user-defined data type that can contain data members (variables) and member functions (methods) that operate on the data members.
- A class is a blueprint or template for creating objects of that class type.
- An object is an instance of a class that has its own state (values of the data members) and behavior (actions of the member functions).
- To define a class, the keyword `class` is used followed by the class name and a pair of curly braces that enclose the data members and member functions.
- To create an object of a class, the class name is used followed by the object name and an optional assignment operator and constructor arguments.
- A constructor is a special member function that is automatically called when an object is created. It is used to initialize the data members of the object.
- A destructor is a special member function that is automatically called when an object is destroyed. It is used to release any resources allocated by the object.
- To access the data members and member functions of an object, the dot operator (`.`) is used followed by the name of the member.
- To access the data members and member functions of a class, the scope resolution operator (`::`) is used followed by the name of the member.
- A static member is a class member that belongs to the class rather than to its objects. There is only one copy of the static member for the entire class. To declare a static member, the keyword `static` is used before the member declaration. To access a static member, the class name and the scope resolution operator are used.
- A structure is a user-defined data type that can contain data members but not member functions. It is similar to a class but by default, all the members of a structure are public. To define a structure, the keyword `struct` is used followed by the structure name and a pair of curly braces that enclose the data members.
- A structure can be converted to a class by adding member functions and changing the access specifiers of the data members. A class can be converted to a structure by removing member functions and making all the data members public.