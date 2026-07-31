### Basics of Object and Class in C++

- **Object**: An object is an instance of a class. It is a basic unit of Object Oriented Programming and represents the real-life entities. An object contains data and methods to manipulate the data.

- **Class**: A class is a blueprint for creating objects. It is a user-defined data type that contains data members and member functions. The data members represent the attributes of an object, and the member functions represent the behavior of an object.

- **Creating a Class**: A class is defined using the `class` keyword, followed by the class name and the class body enclosed in curly braces. The class body contains the data members and member functions.

```c++
class ClassName {
    // data members
    // member functions
};
```

- **Creating an Object**: An object is created by defining a variable of the class type. The syntax for creating an object is:

```c++
ClassName objectName;
```

- **Accessing Data Members and Member Functions**: The data members and member functions of an object can be accessed using the dot (`.`) operator. The syntax for accessing a data member or member function is:

```c++
objectName.dataMember;
objectName.memberFunction();
```

- **Constructors**: A constructor is a special member function that is called automatically when an object is created. It is used to initialize the data members of an object. A constructor has the same name as the class and no return type.

```c++
class ClassName {
    public:
        ClassName() {
            // constructor body
        }
};
```

- **Destructors**: A destructor is a special member function that is called automatically when an object is destroyed. It is used to release any resources that the object may have acquired during its lifetime. A destructor has the same name as the class, preceded by a tilde (`~`) and no return type.

```c++
class ClassName {
    public:
        ~ClassName() {
            // destructor body
        }
};
```