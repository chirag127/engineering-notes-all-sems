### Overloading of functions

- Function overloading is a feature of C++ that allows us to define multiple functions with the same name but different parameters.
- Function overloading enables us to create more than one version of a function that performs the same or similar tasks but with different types or numbers of arguments.
- Function overloading is useful for writing concise and readable code, as well as for implementing polymorphism, which is the ability of an object to behave differently depending on the context.
- The compiler determines which version of the function to call based on the types and number of arguments passed to the function at the time of invocation.
- The rules or conditions for overloading are:
  - The functions must have the same name but different parameter lists.
  - The parameter lists must differ in at least one of the following ways:
    - The number of parameters
    - The type of parameters
    - The order of parameters
  - The return type of the functions does not affect overloading, as the compiler only looks at the parameter lists to resolve the function call.
  - The functions can be defined in the same or different scopes, such as inside a class, a namespace, or a global scope.
- An example of function overloading is:

```cpp
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
std::string add(std::string a, std::string b) {
  return a + b;
}

// Main function
int main() {
  // Calling different versions of add function
  std::cout << add(10, 20) << std::endl; // Calls int add(int, int)
  std::cout << add(3.14, 2.71) << std::endl; // Calls double add(double, double)
  std::cout << add(10, 20, 30) << std::endl; // Calls int add(int, int, int)
  std::cout << add("Hello", "World") << std::endl; // Calls std::string add(std::string, std::string)
  return 0;
}
```

- The output of the above program is:

```
30
5.85
60
HelloWorld
```