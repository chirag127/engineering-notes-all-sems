# Friend Functions in C++

- A friend function is a function that is declared using the `friend` keyword inside the body of a class    .
- A friend function can access the private and protected data members of the class, as well as the public ones    .
- A friend function is not a member function of the class, and therefore does not have the `this` pointer or the scope resolution operator `::`  .
- A friend function can be defined either inside or outside the class, but it must be declared inside the class   .
- A friend function can be a global function, a member function of another class, or a function template  .
- A friend function can be declared in any access section of the class (private, protected, or public), but it does not affect its access level   .
- A friend function can be declared in multiple classes, and it can access the data members of all those classes .
- A friend function can be overloaded, but it cannot be inherited by the derived classes .

## Example of a friend function

```cpp
// A class to represent a complex number
class Complex {
    private:
        double real; // real part
        double imag; // imaginary part
    public:
        // Constructor to initialize the complex number
        Complex(double r = 0, double i = 0) {
            real = r;
            imag = i;
        }
        // A friend function to print the complex number
        friend void print(Complex c);
};

// A friend function definition
void print(Complex c) {
    std::cout << c.real << " + " << c.imag << "i" << std::endl;
}

// A main function to test the friend function
int main() {
    Complex c1(3, 4); // create a complex number 3 + 4i
    print(c1); // call the friend function
    return 0;
}
```

Output:

```
3 + 4i
```

In this example, the `print` function is a friend function of the `Complex` class, and it can access the private data members `real` and `imag` of the class. The `print` function is not a member function of the `Complex` class, and it does not need to use the `this` pointer or the scope resolution operator `::` to access the data members. The `print` function is declared inside the `Complex` class using the `friend` keyword, and it is defined outside the class. The `print` function can be called with any object of the `Complex` class as an argument.