Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of virtual functions for the unit 5 - C++ Functions in the subject of Object Oriented System Design.

### Virtual Functions

- A virtual function is a member function of a class that can be overridden by a derived class.
- A virtual function is declared with the keyword `virtual` in the base class.
- A virtual function can be redefined by a derived class with the same name, return type, and parameters as the base class function.
- A virtual function enables polymorphism, which is the ability of an object to behave differently depending on its type at run time.
- A virtual function is called using a pointer or a reference to the base class type, which can point or refer to an object of the derived class type.
- A virtual function is resolved dynamically, which means the compiler determines which function to call based on the actual type of the object pointed or referred by the base class pointer or reference at run time.
- A virtual function can be pure or non-pure. A pure virtual function is declared with `= 0` after the function prototype in the base class, and it has no definition in the base class. A pure virtual function must be defined by all the derived classes that inherit from the base class. A non-pure virtual function has a definition in the base class, which can be overridden by the derived classes.
- A class that has at least one pure virtual function is called an abstract class. An abstract class cannot be instantiated, but it can be used as a base class for other classes. A class that has no pure virtual functions is called a concrete class. A concrete class can be instantiated and can also be used as a base class for other classes.
- A virtual function can be invoked using the scope resolution operator `::` to specify the class name before the function name. This is called static binding, which means the compiler determines which function to call based on the class name at compile time. Static binding can be used to call the base class version of a virtual function from a derived class, or to avoid polymorphism when calling a virtual function using a base class pointer or reference.
- A virtual function can also be invoked using the keyword `virtual` before the function name. This is called dynamic binding, which means the compiler determines which function to call based on the actual type of the object at run time. Dynamic binding can be used to call the derived class version of a virtual function from a base class, or to enforce polymorphism when calling a virtual function using a base class pointer or reference.

Here is an example of a virtual function in C++:

```cpp
// Base class
class Shape {
public:
  // Constructor
  Shape(double a) {
    area = a;
  }
  // Virtual function to display the area
  virtual void display() {
    cout << "The area of the shape is " << area << endl;
  }
protected:
  double area; // Area of the shape
};

// Derived class
class Circle : public Shape {
public:
  // Constructor
  Circle(double r) : Shape(3.14 * r * r) {
    radius = r;
  }
  // Override the display function
  void display() override {
    cout << "The area of the circle with radius " << radius << " is " << area << endl;
  }
private:
  double radius; // Radius of the circle
};

// Main function
int main() {
  // Create a pointer to the base class
  Shape* ptr;
  // Create an object of the derived class
  Circle c(5);
  // Assign the address of the derived class object to the base class pointer
  ptr = &c;
  // Call the display function using the base class pointer
  ptr->display(); // This will call the display function of the derived class
  // Call the display function using the scope resolution operator
  ptr->Shape::display(); // This will call the display function of the base class
  return 0;
}
```