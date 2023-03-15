# Call and Return by Reference

- Call by reference is a technique of passing arguments to a function in which the actual memory addresses of the arguments are passed to the function. This means that any changes made to the parameters inside the function will affect the original variables in the caller function.
- Return by reference is a technique of returning a value from a function in which the function returns a reference to a variable, rather than a copy of its value. This means that the caller function can access and modify the returned variable directly, without creating a new variable.
- Call and return by reference are useful for implementing operators, modifying arrays, swapping values, and avoiding unnecessary copying of large objects.
- To pass an argument by reference, we use the & operator before the parameter name in the function declaration and definition. For example:

```cpp
// A function that swaps two integers using call by reference
void swap(int &a, int &b) {
  int temp = a;
  a = b;
  b = temp;
}

// A function that calls swap
void test() {
  int x = 10, y = 20;
  swap(x, y); // Pass x and y by reference
  cout << "x = " << x << ", y = " << y << endl; // Prints x = 20, y = 10
}
```

- To return a value by reference, we use the & operator after the return type in the function declaration and definition. We also need to make sure that the returned variable is not a local variable of the function, as it will be destroyed when the function exits. For example:

```cpp
// A global variable
int g = 100;

// A function that returns a reference to g
int& getG() {
  return g;
}

// A function that calls getG
void test() {
  int &r = getG(); // Get a reference to g
  r = 200; // Modify g through r
  cout << "g = " << g << endl; // Prints g = 200
}
```

- Call and return by reference are important concepts in C++ that allow us to manipulate data more efficiently and flexibly. However, we should also be careful about the scope and lifetime of the variables that are passed or returned by reference, as they may cause unexpected errors or undefined behavior if used incorrectly.