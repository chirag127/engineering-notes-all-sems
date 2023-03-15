### Basics of object and class in C++

- A class is a user-defined data type that groups related data and functions together. It is a blueprint or template for creating objects of that type.
- An object is an instance of a class that has its own state and behavior. It is a variable that can store data and perform operations defined by the class.
- A class can have two types of members: data members and member functions. Data members are variables that store the state of the object. Member functions are functions that define the behavior of the object.
- A class can also have static members, which are members that belong to the class rather than to its objects. Static members have only one copy for the entire class and can be accessed without creating an object of the class.
- A class can be defined using the keyword `class` followed by the class name and a pair of curly braces that enclose the class members. For example:

```cpp
class Rectangle {
  // data members
  int length;
  int width;

  // member functions
  public:
  void setLength(int l);
  void setWidth(int w);
  int getArea();
};
```

- An object can be created using the class name followed by the object name and an optional initialization list. For example:

```cpp
Rectangle r1; // create an object r1 of class Rectangle
Rectangle r2 {10, 20}; // create an object r2 of class Rectangle and initialize its data members
```

- The data members and member functions of an object can be accessed using the dot operator (`.`) or the arrow operator (`->`) if the object is a pointer. For example:

```cpp
r1.setLength(15); // call the member function setLength on object r1
r1.length = 15; // access the data member length of object r1
r2.getArea(); // call the member function getArea on object r2
Rectangle *ptr = &r1; // create a pointer to object r1
ptr->setWidth(10); // call the member function setWidth on the object pointed by ptr
ptr->width = 10; // access the data member width of the object pointed by ptr
```

- The static members of a class can be accessed using the scope resolution operator (`::`) and the class name. For example:

```cpp
class Counter {
  // static data member
  static int count;

  // member function
  public:
  void increment();
};

// define and initialize the static data member outside the class
int Counter::count = 0;

// access the static data member using the class name
cout << Counter::count << endl; // prints 0
```