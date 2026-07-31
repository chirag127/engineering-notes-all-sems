### Friend Functions

- A friend function is a function that is not a member of a class, but can access the private and protected members of the class  .
- A friend function is declared using the `friend` keyword inside the body of the class, either in the public or private section   .
- A friend function can be called like a normal function, using any instance of any class or without any object.
- A friend function can be a global function, a member function of another class, or a member function of a nested class .
- A friend function can be declared anywhere in the class, but the definition must be outside the class .
- A friend function can be a template function or a template class .
- A friend function can access the private and protected members of the class directly, without using any object or scope resolution operator   .
- A friend function can be declared as a friend of more than one class .
- A friend function does not affect the encapsulation of the class, as it is explicitly declared as a friend by the class .
- A friend function can be used to perform operations that involve more than one class, such as overloading operators, comparing objects, or swapping values .

#### Example of a friend function

```cpp
// A class to represent a complex number
class Complex {
private:
    double real; // real part
    double imag; // imaginary part
public:
    // Constructor to initialize the complex number
    Complex(double r, double i) {
        real = r;
        imag = i;
    }
    // A friend function to print the complex number
    friend void printComplex(Complex c);
};

// A friend function definition
void printComplex(Complex c) {
    // Access the private members of the class directly
    std::cout << c.real << " + " << c.imag << "i\n";
}

// A main function to test the friend function
int main() {
    // Create a complex number object
    Complex c1(3.4, 5.6);
    // Call the friend function
    printComplex(c1); // Output: 3.4 + 5.6i
    return 0;
}
```