### Overloading of functions

- Function overloading is a feature of C++ that allows us to define multiple functions with the same name but different parameters.
- Function overloading enables us to write generic and concise code that can perform different tasks based on the arguments passed to the function.
- Function overloading is also an example of polymorphism, which is the ability of an object or a function to take different forms depending on the context.
- The compiler determines which function to call based on the number, type and order of the arguments passed to the function. This is called **overload resolution**.
- The functions that have the same name but different parameters are called **overloaded functions**.
- The parameters of the overloaded functions must differ in at least one of the following ways:
  - The number of parameters
  - The type of parameters
  - The order of parameters
- The return type of the overloaded functions is not considered for overload resolution. Therefore, we cannot overload functions based on their return type alone.
- We can also use default parameters in function overloading, which are parameters that have a predefined value if the user does not provide one. However, we must ensure that the default parameters do not create ambiguity or conflict with other overloaded functions.

- Here is an example of function overloading in C++:

```cpp
// A function to add two integers
int add(int a, int b) {
  return a + b;
}

// A function to add two doubles
double add(double a, double b) {
  return a + b;
}

// A function to add three integers
int add(int a, int b, int c) {
  return a + b + c;
}

// A function to add two integers with a default parameter
int add(int a, int b = 0) {
  return a + b;
}

int main() {
  // Calling the overloaded functions
  cout << add(10, 20) << endl; // calls the first function
  cout << add(10.5, 20.5) << endl; // calls the second function
  cout << add(10, 20, 30) << endl; // calls the third function
  cout << add(10) << endl; // calls the fourth function
  return 0;
}
```

- The output of the above program is:

```txt
30
31
60
10
```