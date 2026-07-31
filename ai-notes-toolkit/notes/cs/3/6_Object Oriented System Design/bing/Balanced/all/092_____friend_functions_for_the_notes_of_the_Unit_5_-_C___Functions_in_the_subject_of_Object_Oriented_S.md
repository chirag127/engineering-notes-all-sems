# Friend Functions in C++

- A friend function is a function that is declared using the `friend` keyword inside the body of a class    .
- A friend function can access the private and protected data members of the class, as well as the public ones    .
- A friend function is not a member function of the class, and it does not inherit the access privileges of the class  .
- A friend function can be defined anywhere in the program, either before or after the class definition   .
- A friend function can be a global function, a member function of another class, or a function template .
- A friend function can be declared in any section of the class (private, protected, or public), but it does not affect its access level   .
- A friend function can be declared multiple times in the same or different classes, but it can be defined only once.
- A friend function can have default arguments, but they must be specified in the function definition, not in the friend declaration.
- A friend function can be overloaded, but it cannot be overridden.
- A friend function can be used to implement operator overloading, input/output operations, and comparison operations for a class  .

## Example of a Friend Function

```cpp
#include <iostream>
using namespace std;

// class declaration
class Rectangle {
    private:
        int length;
        int width;
    public:
        // constructor
        Rectangle(int l, int w) {
            length = l;
            width = w;
        }
        // friend function declaration
        friend int area(Rectangle r);
};

// friend function definition
int area(Rectangle r) {
    return r.length * r.width;
}

// main function
int main() {
    // create a Rectangle object
    Rectangle rect(10, 5);
    // call the friend function
    cout << "Area of rectangle: " << area(rect) << endl;
    return 0;
}
```

Output:

```
Area of rectangle: 50
```

In this example, the function `area` is declared as a friend of the class `Rectangle`, and it can access the private data members `length` and `width` of the class. The function `area` is not a member of the class `Rectangle`, and it can be defined anywhere in the program. The function `area` can be called with a `Rectangle` object as an argument, and it returns the area of the rectangle.