# Inline functions

- Inline functions are a feature of C++ that allows the compiler to replace the function call with the function body at the point of the call  .
- The main advantage of inline functions is that they reduce the function call overhead, such as pushing and popping arguments and return values on the stack, and jumping to and from the function address .
- Inline functions can also improve the performance of the program by enabling the compiler to perform context-specific optimizations, such as constant folding, dead code elimination, and inlining of nested functions .
- Inline functions can be declared using the `inline` keyword before the function definition, or by defining the function entirely inside a class, struct, or union definition  .
- A function declared `constexpr` is implicitly an inline function.
- The `inline` keyword is only a suggestion to the compiler, and the compiler may choose to ignore it and not inline the function, depending on the complexity and size of the function   .
- Inline functions should be used for small and simple functions, such as getters and setters, arithmetic operations, and logical expressions  .
- Inline functions should not be used for large and complex functions, such as recursive functions, loops, switch statements, and input/output operations  .
- Inline functions are different from macros, which are textual substitutions performed by the preprocessor. Inline functions are type-safe, respect the scope rules, and can be debugged  .