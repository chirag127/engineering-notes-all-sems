### Basics of Object and Class in C++ for the Notes of the Unit 6 - Objects and Classes in the Subject of Object Oriented System Design

1. **Object**: An object is an instance of a class. It is a basic unit of Object Oriented Programming and represents the real-life entities. An object contains data and methods to manipulate the data.

2. **Class**: A class is a blueprint for creating objects. It is a user-defined data type that contains data members and member functions. The data members represent the attributes of an object and the member functions represent the behavior of an object.

3. **Creating a Class**: A class is defined using the `class` keyword, followed by the name of the class and a pair of curly braces `{}`. The data members and member functions are defined within the curly braces.

```c++
class ClassName {
    // data members
    // member functions
};
```

4. **Creating an Object**: An object is created by declaring a variable of the class type. The syntax for creating an object is:

```c++
ClassName objectName;
```

5. **Accessing Data Members and Member Functions**: The data members and member functions of an object can be accessed using the dot `.` operator. The syntax for accessing a data member or member function is:

```c++
objectName.dataMember;
objectName.memberFunction();
```

6. **Constructors**: A constructor is a special member function of a class that is executed whenever an object of the class is created. It is used to initialize the data members of an object.

7. **Destructors**: A destructor is a special member function of a class that is executed whenever an object of the class is destroyed. It is used to release any resources that the object may have acquired during its lifetime.

8. **Encapsulation**: Encapsulation is the process of combining data and functions that operate on the data into a single unit called a class. It is one of the fundamental principles of Object Oriented Programming.

9. **Inheritance**: Inheritance is the process by which one class acquires the properties and methods of another class. It is used to create a new class from an existing class, with the new class inheriting the data members and member functions of the existing class.

10. **Polymorphism**: Polymorphism is the ability of an object to take on many forms. It allows objects of different classes to be treated as objects of a common superclass. Polymorphism is achieved through the use of virtual functions and function overriding.
