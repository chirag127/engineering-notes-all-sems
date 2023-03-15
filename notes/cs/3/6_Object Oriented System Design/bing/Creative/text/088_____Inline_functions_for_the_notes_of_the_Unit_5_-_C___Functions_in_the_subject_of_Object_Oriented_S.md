### Inline functions

- Inline functions are a feature of C++ that allows the compiler to replace a function call with the function body at the point of the call.
- The main advantage of inline functions is that they can reduce the overhead of function calls, such as pushing and popping arguments and return values on the stack, and jumping to and from the function address .
- Inline functions can also enable the compiler to perform context-specific optimizations, such as constant folding, dead code elimination, and inlining of nested functions.
- Inline functions are best used for small and simple functions, such as getters and setters, that are called frequently and do not contain loops, recursion, or static variables .
- Inline functions are not guaranteed to be inlined by the compiler, as it may decide to ignore the inline request based on various factors, such as the size and complexity of the function, the optimization level, and the target architecture .
- To declare an inline function, the keyword `inline` is used before the function definition, or the function definition is placed entirely inside the class or struct definition .
- A function declared with the `constexpr` specifier is implicitly an inline function.
- An example of an inline function is:

```cpp
// inline function declaration
inline int max(int a, int b) {
  return (a > b) ? a : b;
}

// function call
int x = max(10, 20); // replaced by int x = (10 > 20) ? 10 : 20;
```