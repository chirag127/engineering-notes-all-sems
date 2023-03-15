### Basics of object and class in C++

Here are some points to understand the basics of object and class in C++:

- A class is a user-defined data type that can contain data members (variables) and member functions (methods) that operate on the data members.
- A class is a blueprint or template for creating objects of the same type. For example, a class named Car can define the attributes and behaviors of a car, such as color, speed, start, stop, etc.
- An object is an instance of a class that has its own copy of the data members and can access the member functions defined in the class. For example, an object named myCar can be created from the Car class and have its own color, speed, etc.
- To define a class in C++, the keyword class is used followed by the class name and a pair of curly braces that enclose the data members and member functions. For example:

```cpp
class Car {
  // data members
  string color;
  int speed;

  // member functions
  public:
    void start();
    void stop();
    void setColor(string c);
    string getColor();
};
```

- To create an object of a class in C++, the class name is used followed by the object name and an optional assignment operator and constructor. For example:

```cpp
Car myCar; // create an object named myCar of the class Car
Car yourCar = Car(); // create an object named yourCar of the class Car using the default constructor
```

- To access the data members and member functions of an object, the dot operator (.) is used followed by the name of the data member or member function. For example:

```cpp
myCar.setColor("red"); // call the member function setColor of the object myCar and pass "red" as an argument
cout << myCar.getColor(); // call the member function getColor of the object myCar and print the return value
```

- A constructor is a special member function that is automatically called when an object is created. It is used to initialize the data members of the object with some default or user-defined values. A constructor has the same name as the class and no return type. For example:

```cpp
class Car {
  // data members
  string color;
  int speed;

  // member functions
  public:
    // constructor
    Car() {
      color = "white"; // initialize color with "white"
      speed = 0; // initialize speed with 0
    }

    // other member functions
    void start();
    void stop();
    void setColor(string c);
    string getColor();
};
```

- A destructor is a special member function that is automatically called when an object is destroyed. It is used to perform any cleanup operations before the object is deleted from memory. A destructor has the same name as the class with a tilde (~) prefix and no return type. For example:

```cpp
class Car {
  // data members
  string color;
  int speed;

  // member functions
  public:
    // constructor
    Car() {
      color = "white"; // initialize color with "white"
      speed = 0; // initialize speed with 0
    }

    // destructor
    ~Car() {
      cout << "Car object destroyed" << endl; // print a message before deleting the object
    }

    // other member functions
    void start();
    void stop();
    void setColor(string c);
    string getColor();
};
```

- A static member is a class member that belongs to the class rather than to its objects. There is only one copy of the static member that is shared by all the objects of the class. A static member can be a data member or a member function. To declare a static member, the keyword static is used before the data type or the return type. To access a static member, the class name and the scope resolution operator (::) are used instead of the object name and the dot operator. For example:

```cpp
class Car {
  // data members
  string color;
  int speed;
  static int count; // static data member to count the number of objects created

  // member functions
  public:
    // constructor
    Car() {
      color = "white"; // initialize color with "white"
      speed = 0; // initialize speed with 0
      count++; // increment the static data member count by 1
    }

    // static member function to display the count
    static void displayCount() {
      cout << "The number