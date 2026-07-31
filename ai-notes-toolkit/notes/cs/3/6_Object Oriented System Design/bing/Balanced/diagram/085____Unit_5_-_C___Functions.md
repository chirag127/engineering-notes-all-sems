## Unit 5 - C++ Functions

A function is a block of code that performs a specific task. Functions are used to modularize, reuse, and simplify the code. In C++, functions can be defined in different ways, such as:

- Using the **function declaration** and **function definition** syntax, where the function declaration specifies the name, return type, and parameters of the function, and the function definition provides the body of the function. For example:

```cpp
// Function declaration
int add(int a, int b);

// Function definition
int add(int a, int b) {
  return a + b;
}
```

- Using the **function prototype** syntax, where the function declaration is placed before the main function, and the function definition is placed after the main function. This allows the compiler to check the validity of the function calls before the function definition is encountered. For example:

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

- Using the **inline function** syntax, where the function definition is preceded by the keyword `inline`. This instructs the compiler to replace the function call with the function code at compile time, which can improve the performance of the program. However, inline functions should be used sparingly and only for short and simple functions. For example:

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

- They improve the readability and maintainability of the code by breaking it into smaller and meaningful units.
- They avoid the repetition of code by allowing the reuse of the same function in different parts of the program.
- They facilitate the testing and debugging of the code by isolating the errors and bugs in a single function.
- They enhance the modularity and extensibility of the code by allowing the addition or modification of functions without affecting the rest of the program.