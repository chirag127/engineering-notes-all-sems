### Pointers in C++ for Polymorphism

- Polymorphism is the ability of an object to behave differently depending on the context.
- In C++, polymorphism is achieved by using inheritance and virtual functions.
- Inheritance allows a derived class to inherit the properties and methods of a base class, and optionally override or extend them.
- Virtual functions are functions that are declared with the `virtual` keyword in the base class, and can be redefined by the derived classes.
- To use polymorphism in C++, we need to use pointers or references to access the objects of the derived classes through the base class interface.
- Pointers are variables that store the memory address of another variable or object.
- References are aliases for another variable or object, and do not have their own memory address.
- Pointers and references allow us to treat the objects of different derived classes as if they were of the same base class type, and invoke the appropriate virtual function at run time.
- This is called dynamic or run-time polymorphism, and it is one of the key features of object-oriented programming.

#### Example of polymorphism with pointers in C++

```cpp
// A base class
class Shape {
  public:
    // A virtual function
    virtual void draw() {
      cout << "Drawing a shape" << endl;
    }
};

// A derived class
class Circle : public Shape {
  public:
    // Override the virtual function
    void draw() {
      cout << "Drawing a circle" << endl;
    }
};

// Another derived class
class Square : public Shape {
  public:
    // Override the virtual function
    void draw() {
      cout << "Drawing a square" << endl;
    }
};

// A function that takes a pointer to a Shape object
void drawShape(Shape* s) {
  // Call the virtual function through the pointer
  s->draw();
}

// A main function
int main() {
  // Create a pointer to a Shape object
  Shape* s = new Shape();
  // Call the drawShape function with the pointer
  drawShape(s); // Output: Drawing a shape

  // Create a pointer to a Circle object
  Circle* c = new Circle();
  // Call the drawShape function with the pointer
  drawShape(c); // Output: Drawing a circle

  // Create a pointer to a Square object
  Square* sq = new Square();
  // Call the drawShape function with the pointer
  drawShape(sq); // Output: Drawing a square

  // Delete the pointers
  delete s;
  delete c;
  delete sq;

  return 0;
}
```

- In this example, we have a base class `Shape` and two derived classes `Circle` and `Square`.
- The base class has a virtual function `draw` that is overridden by the derived classes.
- We have a function `drawShape` that takes a pointer to a `Shape` object as a parameter, and calls the `draw` function through the pointer.
- In the main function, we create pointers to different objects of the derived classes, and pass them to the `drawShape` function.
- The function invokes the appropriate `draw` function depending on the actual type of the object pointed by the pointer, and not the declared type of the pointer.
- This demonstrates how pointers enable polymorphism in C++.