### Inline functions

- An inline function is a function that is expanded in line when it is called. That is, the compiler replaces the function call with the function code at compile time.
- The main purpose of inline functions is to reduce the function call overhead, which includes the cost of passing arguments, saving and restoring registers, and jumping to and from the function code.
- Inline functions can also improve the performance of the program by enabling the compiler to perform context-specific optimizations, such as constant folding, dead code elimination, and inlining of nested functions.
- Inline functions are declared using the `inline` keyword before the function definition. For example:

```cpp
inline int max(int a, int b) {
  return (a > b) ? a : b;
}
```

- Inline functions can also be defined inside a class or a struct, in which case they are implicitly inline. For example:

```cpp
class Point {
  private:
    int x, y;
  public:
    Point(int x, int y) : x(x), y(y) {} // inline constructor
    int getX() const { return x; } // inline getter
    int getY() const { return y; } // inline getter
    void setX(int x) { this->x = x; } // inline setter
    void setY(int y) { this->y = y; } // inline setter
};
```

- Inline functions can also be declared as `constexpr`, which means they can be evaluated at compile time if their arguments are constant expressions. For example:

```cpp
constexpr int factorial(int n) {
  return (n <= 1) ? 1 : n * factorial(n - 1);
}

int main() {
  constexpr int f5 = factorial(5); // computed at compile time
  int x = 6;
  int f6 = factorial(x); // computed at run time
  return 0;
}
```

- Inline functions have some advantages and disadvantages compared to regular functions. Some of them are:

  - Advantages:
    - They can reduce the execution time and improve the performance of the program by avoiding function call overhead.
    - They can enable the compiler to perform more optimizations, such as inlining of nested functions, constant folding, and dead code elimination.
    - They can be used with C++ classes and templates, which can improve the readability and maintainability of the code.
  - Disadvantages:
    - They can increase the code size and memory usage of the program, which can affect the cache efficiency and loading time.
    - They can make the debugging and testing of the program more difficult, as the function code is not available at run time.
    - They can cause multiple definitions of the same function in different translation units, which can lead to linker errors or inconsistent behavior.

- Inline functions are not guaranteed to be inlined by the compiler, as the compiler may decide to ignore the `inline` keyword based on various factors, such as the complexity, size, and frequency of the function. Therefore, inline functions should be used judiciously and only for small and simple functions that are called frequently.