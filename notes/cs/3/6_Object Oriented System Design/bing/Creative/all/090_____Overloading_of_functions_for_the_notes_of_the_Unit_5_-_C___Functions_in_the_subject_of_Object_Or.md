Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of overloading of functions in C++.

# Overloading of functions

- Function overloading is a feature of C++ that allows us to define multiple functions with the same name but different parameters or return types.
- Function overloading enables us to write generic and concise code that can handle different types of arguments without repeating the same logic.
- The compiler determines which function to call based on the number, type and order of the arguments passed to the function.
- Function overloading can be done in the same scope (global or class) or in different scopes (base and derived classes) using inheritance and polymorphism.
- Function overloading can also be done for operators, constructors and destructors, which are special types of functions in C++.

## Rules for function overloading

- The overloaded functions must have the same name but different parameter lists.
- The parameter lists can differ in the number, type or order of the parameters, but not in the parameter names.
- The return type of the overloaded functions can be different, but it is not considered by the compiler for resolving the function call.
- The overloaded functions must have the same scope, either global or within a class.
- The overloaded functions cannot differ only by the const or volatile qualifiers of the parameters or the function itself.
- The overloaded functions cannot differ only by the default values of the parameters.

## Examples of function overloading

- Here is an example of function overloading in the global scope:

```cpp
// A function to calculate the area of a circle
double area(double radius) {
  return 3.14 * radius * radius;
}

// A function to calculate the area of a rectangle
double area(double length, double width) {
  return length * width;
}

// A function to calculate the area of a triangle
double area(double base, double height, double angle) {
  return 0.5 * base * height * sin(angle);
}

// A function call to calculate the area of a circle with radius 5
double a1 = area(5);

// A function call to calculate the area of a rectangle with length 10 and width 8
double a2 = area(10, 8);

// A function call to calculate the area of a triangle with base 12, height 9 and angle 60 degrees
double a3 = area(12, 9, 3.14 / 3);
```

- Here is an example of function overloading in a class scope:

```cpp
// A class to represent a complex number
class Complex {
  private:
    double real; // The real part of the complex number
    double imag; // The imaginary part of the complex number
  public:
    // A constructor to initialize a complex number with real and imaginary parts
    Complex(double r, double i) {
      real = r;
      imag = i;
    }

    // A constructor to initialize a complex number with only real part
    Complex(double r) {
      real = r;
      imag = 0;
    }

    // A constructor to initialize a complex number with zero
    Complex() {
      real = 0;
      imag = 0;
    }

    // A function to print a complex number
    void print() {
      cout << real << " + " << imag << "i" << endl;
    }
};

// A function call to create a complex number with real and imaginary parts 3 and 4
Complex c1(3, 4);

// A function call to create a complex number with only real part 5
Complex c2(5);

// A function call to create a complex number with zero
Complex c3;

// A function call to print the complex numbers
c1.print();
c2.print();
c3.print();
```

- Here is an example of function overloading for operators:

```cpp
// A class to represent a vector
class Vector {
  private:
    int x; // The x-coordinate of the vector
    int y; // The y-coordinate of the vector
  public:
    // A constructor to initialize a vector with x and y coordinates
    Vector(int a, int b) {
      x = a;
      y = b;
    }

    // A function to print a vector
    void print() {
      cout << "(" << x << ", " << y << ")" << endl;
    }

    // An overloaded operator to add two vectors
    Vector operator+(Vector v) {
      Vector result(x + v.x, y + v.y);
      return result;
    }

    // An overloaded operator to compare two vectors
    bool