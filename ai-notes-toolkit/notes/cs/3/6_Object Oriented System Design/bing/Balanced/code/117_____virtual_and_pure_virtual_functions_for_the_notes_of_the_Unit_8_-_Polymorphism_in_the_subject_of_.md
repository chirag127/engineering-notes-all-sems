### Virtual and Pure Virtual Functions

- Virtual functions are member functions of a base class that can be overridden by the derived classes.
- Virtual functions allow polymorphism, which is the ability of objects of different types to be treated uniformly by a common interface.
- Virtual functions are declared with the `virtual` keyword in the base class and can be redefined in the derived classes without the `virtual` keyword.
- Virtual functions are resolved at run time using a mechanism called dynamic binding or late binding, which means the function call is matched with the appropriate function definition based on the type of the object that invokes it.
- Pure virtual functions are virtual functions that have no definition in the base class and must be defined in the derived classes.
- Pure virtual functions are declared with the `virtual` keyword and a `= 0` expression at the end of the function declaration in the base class.
- Pure virtual functions make the base class abstract, which means it cannot be instantiated and can only be used as a base for other classes.
- Pure virtual functions ensure that the derived classes provide their own implementation of the function and do not inherit the default behavior from the base class.
- An example of virtual and pure virtual functions in C++ is:

```cpp
// Base class
class Shape {
public:
    // A pure virtual function
    virtual double area() = 0;

    // A virtual function
    virtual void draw() {
        cout << "Drawing a shape" << endl;
    }
};

// Derived class
class Circle : public Shape {
private:
    double radius;
public:
    // Constructor
    Circle(double r) {
        radius = r;
    }

    // Override the pure virtual function
    double area() {
        return 3.14 * radius * radius;
    }

    // Override the virtual function
    void draw() {
        cout << "Drawing a circle" << endl;
    }
};

// Main function
int main() {
    // Shape s; // Error: cannot create object of abstract class
    Shape* s = new Circle(5); // OK: create a pointer to a Shape object
    cout << "Area: " << s->area() << endl; // Calls Circle::area()
    s->draw(); // Calls Circle::draw()
    delete s; // Delete the object
    return 0;
}
```