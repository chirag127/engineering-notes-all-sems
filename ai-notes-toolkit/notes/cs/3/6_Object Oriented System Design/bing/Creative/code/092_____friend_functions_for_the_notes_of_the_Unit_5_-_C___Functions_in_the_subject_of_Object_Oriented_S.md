# Friend Functions in C++

- A friend function is a function that is declared using the `friend` keyword inside the body of a class    .
- A friend function can access the private and protected data members of the class, as well as the public ones    .
- A friend function is not a member function of the class, and therefore does not have the `this` pointer or the scope resolution operator `::`  .
- A friend function can be defined anywhere in the program, either before or after the class definition  .
- A friend function can be a global function, a member function of another class, or a function template .
- A friend function can be declared in any section of the class (public, private, or protected), but the access specifier does not affect its meaning  .
- A friend function can be declared multiple times in the same or different classes, but it can be defined only once .
- A friend function can have default arguments, but they must be specified in the first declaration of the function .
- A friend function can be overloaded, but it cannot be overridden .
- A friend function can be called like a normal function, without using the object of the class  .

## Example of a friend function in C++

```cpp
#include <iostream>
using namespace std;

class Rectangle {
    private:
        int length;
        int width;
    public:
        Rectangle(int l, int w) {
            length = l;
            width = w;
        }
        // declare a friend function
        friend int area(Rectangle r);
};

// define the friend function
int area(Rectangle r) {
    // access the private data members of the class
    return r.length * r.width;
}

int main() {
    // create an object of the class
    Rectangle r(10, 20);
    // call the friend function
    cout << "Area of rectangle: " << area(r) << endl;
    return 0;
}
```

Output:

```
Area of rectangle: 200
```