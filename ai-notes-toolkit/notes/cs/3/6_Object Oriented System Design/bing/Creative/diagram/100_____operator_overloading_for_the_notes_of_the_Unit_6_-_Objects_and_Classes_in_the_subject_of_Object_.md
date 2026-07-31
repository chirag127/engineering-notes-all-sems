### Operator Overloading

- Operator overloading is a feature of object-oriented programming that allows the same operator name or symbol to be used for different operations on different types of operands.
- Operator overloading enables us to define the behavior of operators on user-defined data types such as classes and structs.
- Operator overloading can make the code more readable and intuitive by allowing the use of natural syntax such as `a + b` for adding two complex numbers.
- Operator overloading can also improve the performance of the code by avoiding unnecessary function calls and type conversions.
- Operator overloading is implemented by defining a special function called operator function that specifies what the operator does when applied to the operands of the specified type.
- The general syntax of an operator function is:

```c++
return_type operator op (argument_list)
{
  // body of the function
}
```

- The operator keyword is followed by the operator symbol or name that is being overloaded, such as `+`, `-`, `*`, `/`, `<<`, `>>`, etc.
- The argument list specifies the operands that the operator function can take. For unary operators, there is only one argument, and for binary operators, there are two arguments.
- The return type specifies the type of the value that the operator function returns. It can be any valid C++ type, including user-defined types.
- The body of the function contains the statements that define the logic of the operator function. It can use any C++ features, such as variables, expressions, control structures, etc.
- Some examples of operator functions are:

```c++
// Operator function to overload + for complex numbers
complex operator+ (complex a, complex b)
{
  complex c;
  c.real = a.real + b.real;
  c.imaginary = a.imaginary + b.imaginary;
  return c;
}

// Operator function to overload << for printing complex numbers
ostream& operator<< (ostream& out, complex a)
{
  out << a.real << " + " << a.imaginary << "i";
  return out;
}

// Operator function to overload int() for converting complex numbers to integers
complex::operator int()
{
  return (int) sqrt(real*real + imaginary*imaginary);
}
```

- Operator functions can be either member functions or non-member functions of a class.
- Member functions are defined inside the class definition and have access to the private data members of the class.
- Non-member functions are defined outside the class definition and need to be declared as friends of the class to access the private data members of the class.
- Member functions can be used to overload unary operators and binary operators that have the class object as the left operand.
- Non-member functions can be used to overload binary operators that have the class object as the right operand or both operands.
- Some examples of member and non-member operator functions are:

```c++
// Member function to overload - for complex numbers
complex complex::operator- (complex b)
{
  complex c;
  c.real = real - b.real;
  c.imaginary = imaginary - b.imaginary;
  return c;
}

// Non-member function to overload * for complex numbers
complex operator* (complex a, complex b)
{
  complex c;
  c.real = a.real*b.real - a.imaginary*b.imaginary;
  c.imaginary = a.real*b.imaginary + a.imaginary*b.real;
  return c;
}
```

- Some operators cannot be overloaded in C++. These are:

  - Scope resolution operator `::`
  - Member access operator `.`
  - Member access through pointer operator `.*`
  - Ternary conditional operator `?:`
  - sizeof operator `sizeof`
  - Alignof operator `alignof`
  - typeid operator `typeid`
  - The pointer-to-member operator `->*`
  - The dot operator `.` (but `->` can be overloaded)
  - The cast operator `(type)`
  - The `?:` operator

- Some operators should be overloaded with caution in C++. These are:

  - Logical operators `&&` and `||`
  - Comma operator `,`
  - Bitwise operators `&`, `|`, `^`, `~`, `<<`, `>>`
  - Increment and decrement operators `++` and `--`
  - Assignment operator `=`
  - Relational operators `==`, `!=`, `<`,