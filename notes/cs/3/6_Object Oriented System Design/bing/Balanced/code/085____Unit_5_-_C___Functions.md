## Unit 5 - C++ Functions

A function is a block of code that performs a specific task. Functions are used to modularize, reuse, and simplify the code. In C++, functions can be defined in different ways, such as:

- Using the **function declaration** and **function definition** syntax, where the function declaration specifies the name, parameters, and return type of the function, and the function definition provides the body of the function. For example:

```cpp
// Function declaration
int add(int a, int b);

// Function definition
int add(int a, int b) {
  return a + b;
}
```

- Using the **function prototype** syntax, where the function declaration is placed before the main function, and the function definition is placed after the main function. For example:

```cpp
// Function prototype
int add(int a, int b);

int main() {
  // Function call
  int sum = add(3, 4);
  return 0;
}

// Function definition
int add(int a, int b) {
  return a + b;
}
```

- Using the **inline function** syntax, where the function definition is preceded by the keyword `inline`, and the function is expanded at the point of the function call. Inline functions are used to optimize the performance of the code by avoiding the function call overhead. For example:

```cpp
// Inline function definition
inline int add(int a, int b) {
  return a + b;
}

int main() {
  // Function call
  int sum = add(3, 4);
  return 0;
}
```

Some of the benefits of using functions in C++ are:

- They improve the readability and maintainability of the code by dividing it into smaller and meaningful units.
- They avoid the repetition of the code by allowing the reuse of the same function in different parts of the program.
- They facilitate the debugging and testing of the code by isolating the errors and bugs in a single function.
- They enhance the modularity and flexibility of the code by allowing the use of different parameters and return values for the same function.