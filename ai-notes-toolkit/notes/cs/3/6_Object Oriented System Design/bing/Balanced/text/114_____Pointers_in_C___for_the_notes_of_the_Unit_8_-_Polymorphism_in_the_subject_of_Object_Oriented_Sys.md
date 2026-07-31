### Pointers in C++ for the notes of the Unit 8 - Polymorphism in the subject of Object Oriented System Design

- A pointer is a variable that stores the address of another variable in memory.
- Pointers can be used to access and modify the values of variables that are passed as arguments to functions, or to create dynamic data structures such as linked lists, trees, and graphs.
- Pointers can also be used to implement polymorphism, which is the ability of an object to behave differently depending on its type or context.
- Polymorphism can be achieved in C++ using virtual functions, abstract classes, and inheritance.
- A virtual function is a member function that can be overridden by a derived class to provide a different implementation for the same function name and signature.
- An abstract class is a class that has at least one pure virtual function, which is a virtual function that has no definition and is declared with a = 0 suffix.
- An abstract class cannot be instantiated, but it can be used as a base class for other classes that provide concrete implementations for the pure virtual functions.
- Inheritance is the mechanism of creating new classes from existing ones, by inheriting their data members and member functions.
- Inheritance can be single, multiple, or multilevel, depending on the number and hierarchy of base classes and derived classes.
- To implement polymorphism using pointers, we need to declare a pointer of the base class type and assign it the address of an object of the derived class type.
- Then, we can use the pointer to call the virtual functions of the base class, which will be dynamically resolved to the corresponding functions of the derived class at run time.
- This way, the pointer can point to different types of objects and invoke different behaviors depending on the actual type of the object.
- For example, consider the following code snippet:

```cpp
// A base class for shapes
class Shape {
  public:
    // A pure virtual function for calculating the area of the shape
    virtual double area() = 0;
};

// A derived class for circles
class Circle : public Shape {
  private:
    double radius; // The radius of the circle
  public:
    // A constructor that initializes the radius
    Circle(double r) {
      radius = r;
    }
    // An override of the area function for circles
    double area() {
      return 3.14 * radius * radius;
    }
};

// A derived class for squares
class Square : public Shape {
  private:
    double side; // The side of the square
  public:
    // A constructor that initializes the side
    Square(double s) {
      side = s;
    }
    // An override of the area function for squares
    double area() {
      return side * side;
    }
};

// A function that takes a pointer to a shape and prints its area
void printArea(Shape* s) {
  cout << "The area of the shape is " << s->area() << endl;
}

// A main function that creates different shapes and prints their areas using polymorphism
int main() {
  // A pointer to a shape
  Shape* s;
  // A circle object with radius 5
  Circle c(5);
  // A square object with side 10
  Square sq(10);
  // Assign the pointer to the address of the circle object
  s = &c;
  // Print the area of the circle using the pointer
  printArea(s);
  // Assign the pointer to the address of the square object
  s = &sq;
  // Print the area of the square using the pointer
  printArea(s);
  return 0;
}
```

- The output of the program is:

```
The area of the shape is 78.5
The area of the shape is 100
```

- As we can see, the pointer s can point to different types of shapes and call the appropriate area function for each type, demonstrating polymorphism.