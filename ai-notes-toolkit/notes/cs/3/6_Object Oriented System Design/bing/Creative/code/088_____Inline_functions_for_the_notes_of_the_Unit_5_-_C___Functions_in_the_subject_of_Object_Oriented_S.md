### Inline functions

- Inline functions are a feature of C++ that allows the compiler to replace a function call with the function body at the point of the call.
- Inline functions can reduce the overhead of function calls, such as pushing and popping arguments and return values on the stack, and jumping to and from the function address .
- Inline functions can also enable the compiler to perform context-specific optimizations, such as constant folding, dead code elimination, and inlining of nested calls.
- Inline functions are best used for small and simple functions, such as getters and setters, that are called frequently and do not have loops, recursion, or static variables .
- Inline functions are not guaranteed to be inlined by the compiler, as it may decide to ignore the inline request for various reasons, such as code size, debugging, or complexity .
- To declare an inline function, the keyword `inline` is used before the function definition, or the function definition is placed entirely inside the class or struct definition .
- A function declared with the `constexpr` specifier is implicitly an inline function.
- An example of an inline function is:

```cpp
// inline function declaration
inline int max(int a, int b) {
  return (a > b) ? a : b;
}

// inline function definition inside class
class Point {
  private:
    int x, y;
  public:
    Point(int x, int y) : x(x), y(y) {} // inline constructor
    int getX() { return x; } // inline getter
    int getY() { return y; } // inline getter
    void setX(int x) { this->x = x; } // inline setter
    void setY(int y) { this->y = y; } // inline setter
};
```