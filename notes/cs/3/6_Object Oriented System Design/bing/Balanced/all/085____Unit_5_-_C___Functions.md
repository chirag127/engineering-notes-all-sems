## Unit 5 - C++ Functions

- A function is a block of code that performs a specific task, such as calculating the area of a circle, printing a message, or sorting an array.
- A function can be called by other parts of the program, or by itself, to execute the code inside it.
- A function can have zero or more parameters, which are variables that hold the values passed to the function by the caller.
- A function can also return a value to the caller, or no value at all, using the return statement.
- A function can be defined before or after the main function, or in a separate file, as long as it is declared before it is used.
- A function declaration tells the compiler the name, return type, and parameters of the function, but not the body. For example:

```cpp
// function declaration
int add(int a, int b);

// function definition
int add(int a, int b) {
  return a + b;
}
```

- A function definition provides the body of the function, which contains the statements that execute when the function is called. For example:

```cpp
// function definition
int add(int a, int b) {
  return a + b;
}

// function call
int sum = add(3, 4); // sum is 7
```

- A function can be overloaded, which means that multiple functions can have the same name, but different parameters or return types. For example:

```cpp
// function overloading
int add(int a, int b); // add two integers
double add(double a, double b); // add two doubles
string add(string a, string b); // concatenate two strings
```

- A function can be recursive, which means that it can call itself within its body, either directly or indirectly. For example:

```cpp
// recursive function
int factorial(int n) {
  if (n == 0 || n == 1) {
    return 1;
  }
  else {
    return n * factorial(n - 1);
  }
}
```

- A function can be passed as an argument to another function, or returned as a value from another function, using function pointers. For example:

```cpp
// function pointer
int (*p)(int, int); // declare a pointer to a function that takes two ints and returns an int
p = add; // assign the pointer to the add function
int sum = p(3, 4); // call the function using the pointer
```

- A function can be defined as inline, which means that the compiler will replace the function call with the function body, to avoid the overhead of a function call. For example:

```cpp
// inline function
inline int add(int a, int b) {
  return a + b;
}

// function call
int sum = add(3, 4); // the compiler will replace this with sum = 3 + 4;
```

- A function can be defined as a lambda expression, which is an anonymous function that can be used as a value. For example:

```cpp
// lambda expression
auto add = [](int a, int b) { return a + b; }; // define a lambda function that adds two ints
int sum = add(3, 4); // call the lambda function
```

- A function can be defined as a template, which is a generic function that can work with different types of arguments. For example:

```cpp
// template function
template <typename T>
T add(T a, T b) {
  return a + b;
}

// function call
int sum1 = add(3, 4); // call the template function with ints
double sum2 = add(3.5, 4.5); // call the template function with doubles
string sum3 = add("Hello", "World"); // call the template function with strings
```