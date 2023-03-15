Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of overloading of functions in C++.

### Overloading of functions

- Function overloading is a feature of C++ that allows us to define multiple functions with the same name, but different parameters or return types.
- Function overloading enables us to write generic and concise code, by avoiding the need to create different names for similar functions that perform the same task on different types of data.
- The compiler determines which function to call based on the number, type and order of the arguments passed to the function at the time of invocation. This is also known as **static binding** or **compile-time polymorphism**.
- To overload a function, we need to declare and define multiple functions with the same name, but different parameter lists. The parameter lists can differ in the following ways:
  - The number of parameters can be different. For example, `int add(int a, int b)` and `int add(int a, int b, int c)` are overloaded functions.
  - The type of parameters can be different. For example, `int add(int a, int b)` and `double add(double a, double b)` are overloaded functions.
  - The order of parameters can be different. For example, `int add(int a, double b)` and `int add(double a, int b)` are overloaded functions.
- The return type of the function alone cannot be used to overload a function. For example, `int add(int a, int b)` and `double add(int a, int b)` are not overloaded functions, but redefined functions, which will cause a compile-time error.
- The function overloading resolution is done by the compiler based on the **best match** rule, which means that the compiler will choose the most specific function that matches the arguments. For example, if we have the following overloaded functions:

```cpp
int add(int a, int b);
double add(double a, double b);
int add(int a, double b);
```

and we call `add(10, 20)`, the compiler will choose the first function, as it matches the types of both arguments exactly. If we call `add(10.0, 20.0)`, the compiler will choose the second function, for the same reason. If we call `add(10, 20.0)`, the compiler will choose the third function, as it matches the types of both arguments without any conversion. However, if we call `add(10.0, 20)`, the compiler will report an ambiguity error, as it cannot decide between the second and the third function, as both require one argument to be converted.