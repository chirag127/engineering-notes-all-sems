# Operator Overloading

- Operator overloading is a feature of object-oriented programming languages that allows the programmer to redefine the behavior of built-in operators for user-defined types.
- Operator overloading can make the code more concise, readable, and intuitive by enabling natural syntax for operations on objects.
- For example, in C++, the operator `+` can be overloaded to perform addition on complex numbers, matrices, strings, etc., by writing a function that takes two operands of the desired type and returns the result of the operation.
- Operator overloading is usually implemented by defining special member functions or friend functions for the class that represents the user-defined type. These functions have the same name as the operator, preceded by the keyword `operator`.
- For example, to overload the operator `+` for a class `Complex`, one can write a member function like this:

```cpp
class Complex {
  // ...
  public:
    // Overload + as a member function
    Complex operator+(const Complex& other) const {
      // Return a new Complex object that is the sum of this and other
      return Complex(real + other.real, imag + other.imag);
    }
};
```

- Alternatively, one can write a friend function like this:

```cpp
class Complex {
  // ...
  public:
    // Declare + as a friend function
    friend Complex operator+(const Complex& a, const Complex& b);
};

// Define + as a friend function
Complex operator+(const Complex& a, const Complex& b) {
  // Return a new Complex object that is the sum of a and b
  return Complex(a.real + b.real, a.imag + b.imag);
}
```

- The difference between a member function and a friend function is that a member function can access the private data members of the class directly, while a friend function needs to use the public accessor methods or the overloaded operator `[]`.
- Some operators, such as `=` (assignment), `[]` (subscript), `()` (function call), and `->` (member access), can only be overloaded as member functions, while others, such as `<<` (output) and `>>` (input), are usually overloaded as friend functions.
- Some operators, such as `.` (member access), `?:` (conditional), `sizeof` (size of), and `::` (scope resolution), cannot be overloaded at all, because they are fundamental to the language syntax and semantics.
- When overloading operators, one should follow the principle of least surprise, which means that the overloaded operator should behave as closely as possible to the built-in operator for the built-in types. For example, the operator `+` should always return a new object, not modify the existing one, and the operator `==` should always return a boolean value, not an integer.
- Operator overloading can also be used to implement user-defined literals, which are constants of a user-defined type that can be written using a special syntax. For example, in C++, one can write a user-defined literal for complex numbers like this:

```cpp
// Define a user-defined literal for complex numbers
Complex operator"" _i(long double imag) {
  // Return a new Complex object with the given imaginary part
  return Complex(0.0, imag);
}

// Use the user-defined literal for complex numbers
Complex z = 3.0 + 4.0_i; // Equivalent to Complex(3.0, 4.0)
```

- User-defined literals can only be defined as global or namespace-scope functions, not as class members or friends. They must have a parameter of one of the following types: `const char*`, `unsigned long long`, `long double`, `char`, `wchar_t`, `char16_t`, `char32_t`, or a `std::string`-like type. They must also have a suffix that does not start with an underscore, to avoid conflicts with the predefined literals.