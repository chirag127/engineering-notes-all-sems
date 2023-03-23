 Here is the content in markdown format without any emojis or external links:

### Virtual Functions

- Virtual functions are member functions which are declared within a base class and redefined(overridden) by a derived class.
- They are mainly used to achieve Runtime polymorphism.
- A virtual function is prefixed with a virtual keyword.
- The derived class overrides the base class virtual function. This means that the derived class function replaces the base class function.
- The base class pointer can point to the object of derived class and invoke overridden function. This is known as virtual function call.
- The compiler determines which function to call at compile time in case of non-virtual function. In case of virtual function, the appropriate function to be called is determined at runtime depending upon the type of object pointed to by the pointer.
- Only the functions of the base class which are marked as virtual can be overridden in the derived class.
- The prototype of virtual functions should be the same in both the base as well as derived class. The return type can be a subclass of the return type of the base virtual function.

- This helps in achieving dynamic binding or late binding.
- Example:
class Shape {
public:
    virtual int area() = 0;  // Pure Virtual Function
};

class Rectangle : public Shape {
public:
    int area() { return length * breadth; }
    int length;
    int breadth;
};

class Circle : public Shape {
public:
    int area() { return 3.14 * r * r; }
    int r;
};