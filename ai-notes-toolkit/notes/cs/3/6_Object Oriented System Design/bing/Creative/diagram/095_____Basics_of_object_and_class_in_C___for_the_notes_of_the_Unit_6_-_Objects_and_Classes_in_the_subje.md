### Basics of object and class in C++

- A class is a user-defined data type that can contain data members (variables) and member functions (methods) that operate on the data members.
- A class is a blueprint or template for creating objects of that class type.
- An object is an instance of a class that has its own state (values of the data members) and behavior (actions of the member functions).
- To define a class, the keyword `class` is used followed by the class name and the class body enclosed in curly braces.
- To create an object of a class, the class name is used followed by the object name and an optional initialization list.
- To access the data members and member functions of an object, the dot operator (`.`) is used followed by the name of the member.
- A class can have different types of access specifiers for its members: `public`, `private` and `protected`.
- `public` members are accessible from anywhere, `private` members are accessible only within the class and `protected` members are accessible within the class and its derived classes.
- A class can also have static members, which are shared by all the objects of that class and belong to the class itself.
- To declare a static member, the keyword `static` is used before the member declaration.
- To access a static member, the scope resolution operator (`::`) is used followed by the class name and the member name.
- A class can also have constructors and destructors, which are special member functions that are invoked when an object is created or destroyed.
- A constructor has the same name as the class and can have parameters to initialize the data members of the object.
- A destructor has the same name as the class preceded by a tilde (`~`) and has no parameters or return value.
- A class can also have friend functions and friend classes, which are not members of the class but can access its private and protected members.
- To declare a friend function or a friend class, the keyword `friend` is used before the function or class declaration.