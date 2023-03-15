# Basics of Object and Class in C++

## Unit 6 - Objects and Classes in Object Oriented System Design

1. **Object**: An object is an instance of a class. It represents a real-world entity with its own set of attributes and behaviors. In C++, an object is created using the `new` keyword or by declaring a variable of the class type.

2. **Class**: A class is a blueprint for creating objects. It defines the attributes and behaviors of the objects that are created from it. In C++, a class is defined using the `class` keyword, followed by the class name and the class body enclosed in curly braces.

3. **Attributes**: Attributes, also known as data members, are the variables that define the characteristics of an object. They are declared within the class body and can be of any data type.

4. **Behaviors**: Behaviors, also known as member functions or methods, are the functions that define the actions that an object can perform. They are declared within the class body and can access the object's attributes.

5. **Access Specifiers**: Access specifiers define the visibility of the class members. In C++, there are three access specifiers: `public`, `private`, and `protected`. Public members can be accessed from anywhere, private members can only be accessed within the class, and protected members can be accessed within the class and its derived classes.

6. **Constructors**: Constructors are special member functions that are called when an object is created. They are used to initialize the object's attributes. In C++, constructors have the same name as the class and do not have a return type.

7. **Destructors**: Destructors are special member functions that are called when an object is destroyed. They are used to release any resources that the object may have acquired during its lifetime. In C++, destructors have the same name as the class, preceded by a tilde (~), and do not have a return type.

8. **Encapsulation**: Encapsulation is the process of combining data and functions that operate on that data into a single unit, called a class. It provides a way to hide the internal details of an object and only expose the necessary interface to the outside world.

9. **Inheritance**: Inheritance is the process by which one class acquires the properties and behaviors of another class. It allows for code reuse and the creation of more complex objects from simpler ones. In C++, inheritance is achieved using the `:` symbol, followed by the access specifier and the name of the base class.

10. **Polymorphism**: Polymorphism is the ability of an object to take on many forms. It allows for the creation of more flexible and reusable code. In C++, polymorphism is achieved through the use of virtual functions and function overloading.
