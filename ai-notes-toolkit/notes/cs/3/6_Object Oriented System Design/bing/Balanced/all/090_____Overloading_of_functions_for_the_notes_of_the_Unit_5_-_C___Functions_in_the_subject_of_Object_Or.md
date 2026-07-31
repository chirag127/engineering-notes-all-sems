# Overloading of functions

- Function overloading is a feature of C++ that allows you to define multiple functions with the same name but different parameters  .
- Function overloading enables you to write generic and concise code that can perform different tasks based on the arguments passed to the function .
- Function overloading is an example of **compile-time polymorphism**, which means the compiler determines which function to call based on the type and number of arguments at compile time.
- The rules or conditions for overloading functions are :
  - The function name must be the same.
  - The parameter list must be different, either in type, number, or order of the arguments.
  - The return type of the function does not affect overloading, as the compiler does not consider it while resolving the function call.
- An example of function overloading in C++ is:

```c++
// Function to add two integers
int add(int a, int b) {
  return a + b;
}

// Function to add two doubles
double add(double a, double b) {
  return a + b;
}

// Function to add three integers
int add(int a, int b, int c) {
  return a + b + c;
}

// Function to add two strings
string add(string a, string b) {
  return a + b;
}

int main() {
  cout << add(10, 20) << endl; // calls the first function, prints 30
  cout << add(3.14, 2.71) << endl; // calls the second function, prints 5.85
  cout << add(10, 20, 30) << endl; // calls the third function, prints 60
  cout << add("Hello", "World") << endl; // calls the fourth function, prints HelloWorld
  return 0;
}
```
- Default parameters in C++ are a special case of function overloading, as they allow you to call the same function with different number of arguments by providing default values for some parameters. For example:

```c++
// Function to calculate the area of a rectangle
// with default parameters for length and width
double area(double length = 1.0, double width = 1.0) {
  return length * width;
}

int main() {
  cout << area() << endl; // calls the function with no arguments, prints 1
  cout << area(2.0) << endl; // calls the function with one argument, prints 2
  cout << area(2.0, 3.0) << endl; // calls the function with two arguments, prints 6
  return 0;
}
```
- Function overloading is a powerful and useful feature of C++ that allows you to write flexible and expressive code that can handle different types and scenarios. However, you should also be careful not to overload functions in a way that causes ambiguity or confusion for the compiler or the reader. For example, avoid overloading functions that have the same parameter list but different return types, or functions that have parameters that can be implicitly converted to each other.