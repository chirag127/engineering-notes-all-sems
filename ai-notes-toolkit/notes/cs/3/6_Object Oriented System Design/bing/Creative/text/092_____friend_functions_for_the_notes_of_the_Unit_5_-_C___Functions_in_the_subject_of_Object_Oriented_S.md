### Friend Functions

- A friend function is a function that is not a member of a class, but can access the private and protected data members of the class  .
- A friend function is declared using the `friend` keyword inside the class definition   .
- A friend function can be defined anywhere in the program, either before or after the class definition   .
- A friend function can be a global function, a member function of another class, or a function template   .
- A friend function can access the data members of the class directly, without using the object name or the dot operator   .
- A friend function can be declared in any access specifier section of the class, such as public, private, or protected   .
- A friend function can be declared multiple times in the same class, but it is not necessary   .
- A friend function can be a friend of more than one class   .
- A friend function does not affect the encapsulation of the class, as it is not a member of the class   .
- A friend function is used to enhance the functionality of the class, by allowing external functions to access the data members of the class    .

Example of a friend function:

```cpp
// A class to represent a complex number
class Complex {
private:
    double real; // real part of the complex number
    double imag; // imaginary part of the complex number
public:
    // Constructor to initialize the complex number
    Complex(double r, double i) {
        real = r;
        imag = i;
    }
    // A friend function to print the complex number
    friend void printComplex(Complex c);
};

// A global function to print the complex number
void printComplex(Complex c) {
    // Access the private data members of the class directly
    std::cout << c.real << " + " << c.imag << "i" << std::endl;
}

// A main function to test the friend function
int main() {
    // Create a complex number object
    Complex c1(3.14, 2.71);
    // Call the friend function to print the complex number
    printComplex(c1);
    return 0;
}
```

Output:

```
3.14 + 2.71i
```