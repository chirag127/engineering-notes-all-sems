### Inline functions

- Inline functions are a feature of C++ that allows the compiler to replace a function call with the function body at the point of the call  .
- Inline functions can improve the performance and speed of the program by avoiding the overhead of function calls, such as pushing and popping arguments and return values on the stack, and jumping to and from the function address  .
- Inline functions can also enable the compiler to perform context-specific optimizations, such as constant folding and dead code elimination .
- Inline functions can be declared using the `inline` keyword before the function definition, or by defining the function entirely inside a class, struct, or union definition  .
- Inline functions can also be declared as `constexpr`, which implies inline and also requires the function to be evaluated at compile time if possible.
- Inline functions are not guaranteed to be inlined by the compiler, as it may decide to ignore the inline request for various reasons, such as the function being too complex, recursive, or containing static variables   .
- Inline functions are different from macros, which are textual substitutions performed by the preprocessor. Inline functions are subject to type checking, scope rules, and debugging, while macros are not .
- Inline functions are best used for small and simple functions, such as getters and setters, that are called frequently and do not change the program logic  .
- Inline functions should be avoided for large and complex functions, as they may increase the code size and reduce the cache efficiency  .