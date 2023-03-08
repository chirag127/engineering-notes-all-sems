 Here is the content in markdown format on the topic of virtual and pure virtual functions for the notes of Unit 8 - Polymorphism in Object Oriented System Design:

### Virtual and Pure Virtual Functions

- Virtual functions are member functions in base class that are overridden in derived class. They are resolved at runtime depending upon the type of object.
- They allow us to achieve runtime polymorphism.
- They are declared using the `virtual` keyword before the function declaration in the base class.
- The resolution of which function to call is done by matching the type of object to the function at runtime.
- If the base class has a virtual function, the derived class can override it by redefining the function with the same signature.
- Pure virtual functions are functions that have no implementation in the base class. They are declared using the syntax: `virtual return_type function_name() = 0;`
- A class containing a pure virtual function is called an abstract class. We cannot instantiate an object of an abstract class.
- Abstract classes are useful as base classes to derive further subclasses from. The derived classes must implement the pure virtual functions, else they also become abstract.
- This enforces a level of standard implementation in the subclasses and promotes code reusability.

Advantages:
- Achieves runtime polymorphism.
- Standard implementation can be enforced using pure virtual functions.
- Code reusability is promoted.

Disadvantages:
- There is some overhead in using virtual functions due to runtime resolution of functions.
- If the derived class forgets to override a pure virtual function, it also becomes abstract and cannot be instantiated.

Examples and applications:
- Base class `Shape` with pure virtual function `area()` and virtual function `printArea()`. Derived classes `Circle`, `Square` override these functions to calculate area for specific shapes.
- Used in frameworks to define interfaces that subclasses must implement.

```cpp
class Shape {
    public:
        virtual void printArea() = 0; // Pure virtual function
        virtual double area() = 0; // Pure virtual function
};

class Circle : public Shape {
    public:
        void printArea() override {
            // Print circle area
        }
        double area() override {
            // Return circle area
        }
};
```