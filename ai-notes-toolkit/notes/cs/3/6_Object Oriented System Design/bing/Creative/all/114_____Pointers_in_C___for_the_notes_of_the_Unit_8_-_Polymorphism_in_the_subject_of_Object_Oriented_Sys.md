# Pointers in C++ for Polymorphism

- Polymorphism is the ability of an object to behave differently depending on the context.
- In C++, polymorphism is achieved by using inheritance and virtual functions.
- Inheritance allows a derived class to inherit the properties and methods of a base class, and optionally override or extend them.
- Virtual functions are functions that are declared with the `virtual` keyword in the base class, and can be redefined by the derived classes.
- To use polymorphism in C++, we need to use pointers or references to access the objects of the derived classes through the base class interface.
- Pointers are variables that store the memory address of another variable or object.
- References are aliases for another variable or object, and do not have their own memory address.
- Pointers and references allow us to access the actual object that they point or refer to, regardless of the type of the pointer or reference variable.
- This way, we can invoke the appropriate virtual function of the derived class object at run time, based on the type of the object that the pointer or reference points or refers to.
- This is called dynamic or run-time polymorphism, and it is one of the key features of object-oriented programming in C++.

## Example of polymorphism with pointers in C++

```cpp
#include <iostream>
using namespace std;

// Base class
class Shape {
    public:
    // Virtual function to calculate the area of the shape
    virtual double area() {
        return 0;
    }
};

// Derived class 1
class Circle : public Shape {
    private:
    double radius;
    public:
    // Constructor to initialize the radius
    Circle(double r) {
        radius = r;
    }
    // Override the area function of the base class
    double area() override {
        return 3.14 * radius * radius;
    }
};

// Derived class 2
class Rectangle : public Shape {
    private:
    double length;
    double width;
    public:
    // Constructor to initialize the length and width
    Rectangle(double l, double w) {
        length = l;
        width = w;
    }
    // Override the area function of the base class
    double area() override {
        return length * width;
    }
};

int main() {
    // Create a pointer of type Shape
    Shape* shapePtr;
    // Create a Circle object and assign its address to the pointer
    shapePtr = new Circle(5);
    // Call the area function of the Circle object through the pointer
    cout << "The area of the circle is " << shapePtr->area() << endl;
    // Create a Rectangle object and assign its address to the pointer
    shapePtr = new Rectangle(10, 20);
    // Call the area function of the Rectangle object through the pointer
    cout << "The area of the rectangle is " << shapePtr->area() << endl;
    // Delete the dynamically allocated objects
    delete shapePtr;
    return 0;
}
```

## Output

```
The area of the circle is 78.5
The area of the rectangle is 200
```