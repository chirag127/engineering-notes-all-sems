### Inline functions

- Inline functions are a feature of C++ that allows the compiler to replace a function call with the function body at the point of the call  .
- Inline functions can improve the performance and speed of the program by avoiding the overhead of function calls, such as pushing and popping arguments and return values on the stack, and jumping to and from the function address  .
- Inline functions can also enable the compiler to perform context-specific optimizations, such as constant folding and dead code elimination .
- Inline functions are declared with the `inline` keyword before the function definition   . For example:

```cpp
// inline function declaration
inline int add(int a, int b)
{
    return a + b;
}

// function call
int c = add(2, 3); // the compiler may replace this with int c = 2 + 3;
```

- A function defined entirely inside a class, struct, or union definition, whether it is a member function or a non-member friend function, is implicitly an inline function, unless it is attached to a named module. For example:

```cpp
// class definition with inline functions
class Point
{
    private:
        int x, y;
    public:
        // constructor is implicitly inline
        Point(int a, int b) : x(a), y(b) {}

        // member functions are implicitly inline
        int getX() { return x; }
        int getY() { return y; }

        // friend function is implicitly inline
        friend int distance(Point p1, Point p2);
};

// friend function definition
int distance(Point p1, Point p2)
{
    return sqrt((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y));
}
```

- A function declared `constexpr` is implicitly an inline function. For example:

```cpp
// constexpr function declaration
constexpr int factorial(int n)
{
    return (n <= 1) ? 1 : n * factorial(n - 1);
}

// function call
constexpr int f = factorial(5); // the compiler may evaluate this at compile time
```

- The `inline` keyword is only a suggestion to the compiler, and it may choose to ignore it if it deems it inappropriate or impossible to inline a function   . Some factors that may prevent a function from being inlined are:
  - The function is too large or complex, such as having loops, recursion, or multiple return statements  .
  - The function is virtual, and the compiler cannot determine the exact function to be called at compile time  .
  - The function is defined in a different translation unit or module  .
  - The function has external or static linkage .
  - The function uses `goto` statements or `try-catch` blocks .
  - The function has a variable number of arguments .

- Inline functions should be used with caution, as they may increase the size of the executable and the compilation time, and they may reduce the readability and maintainability of the code   .
- Inline functions are best used for small and simple functions, such as getters and setters, constructors, and operators  .
- Inline functions should not be confused with macros, which are textual substitutions performed by the preprocessor . Inline functions have several advantages over macros, such as:
  - Inline functions are type-safe and respect the scope rules of C++ .
  - Inline functions can be debugged more easily than macros .
  - Inline functions can be overloaded and templated, unlike macros .
  - Inline functions do not have side effects or unexpected behaviors, such as multiple