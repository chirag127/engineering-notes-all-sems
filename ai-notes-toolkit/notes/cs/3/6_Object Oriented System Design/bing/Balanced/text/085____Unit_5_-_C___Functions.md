## Unit 5 - C++ Functions

- A function is a block of code that performs a specific task, such as calculating the area of a circle, printing a message, or sorting an array.
- A function can be called by other parts of the program, or by itself, to execute the code inside it.
- A function can have zero or more parameters, which are variables that hold the values passed to the function by the caller.
- A function can also return a value to the caller, or no value at all, depending on its type and purpose.
- A function can be defined in two ways: using a function prototype and a function definition, or using a function definition only.
- A function prototype is a declaration of the function that specifies its name, return type, and parameters, but not its body. It is usually placed at the beginning of the program, before the main function, or in a header file.
- A function definition is the actual implementation of the function that contains the body of the code. It can be placed anywhere in the program, as long as it is after the function prototype (if any).
- The syntax of a function prototype is:

```cpp
return_type function_name(parameter_list);
```

- The syntax of a function definition is:

```cpp
return_type function_name(parameter_list)
{
  // function body
  // statements
  return value; // optional
}
```

- To call a function, use its name followed by parentheses, and pass the arguments (if any) inside the parentheses. For example:

```cpp
int sum(int a, int b); // function prototype
int main()
{
  int x = 10, y = 20;
  int z = sum(x, y); // function call
  cout << "The sum is " << z << endl;
  return 0;
}
int sum(int a, int b) // function definition
{
  int c = a + b;
  return c;
}
```

- The output of this program is:

```text
The sum is 30
```

- A function can also be called without arguments, or with default arguments, which are values that are assigned to the parameters if the caller does not provide them. For example:

```cpp
void greet(string name = "user"); // function prototype with default argument
int main()
{
  greet(); // function call without argument
  greet("Alice"); // function call with argument
  return 0;
}
void greet(string name) // function definition
{
  cout << "Hello, " << name << "!" << endl;
}
```

- The output of this program is:

```text
Hello, user!
Hello, Alice!
```

- A function can also be overloaded, which means that multiple functions can have the same name, but different parameters or return types. The compiler will choose the appropriate function to call based on the arguments and the return value. For example:

```cpp
int max(int a, int b); // function prototype for int parameters
double max(double a, double b); // function prototype for double parameters
int main()
{
  int x = 10, y = 20;
  double u = 3.14, v = 2.71;
  cout << "The max of " << x << " and " << y << " is " << max(x, y) << endl; // function call for int parameters
  cout << "The max of " << u << " and " << v << " is " << max(u, v) << endl; // function call for double parameters
  return 0;
}
int max(int a, int b) // function definition for int parameters
{
  if (a > b)
    return a;
  else
    return b;
}
double max(double a, double b) // function definition for double parameters
{
  if (a > b)
    return a;
  else
    return b;
}
```

- The output of this program is:

```text
The max of 10 and 20 is 20
The max of 3.14 and 2.71 is 3.14
```

- A function can also be recursive, which means that it can call itself within its body. This can be useful for solving problems that have a repetitive or recursive nature, such as factorial, Fibonacci, or binary search. For example:

```cpp
int factorial(int n); // function prototype
int main()
{
  int x = 5;
  cout << "The factorial of " << x << " is " << factorial(x) << endl; // function call
  return 0;
}
int factorial(int n) // function definition

```
