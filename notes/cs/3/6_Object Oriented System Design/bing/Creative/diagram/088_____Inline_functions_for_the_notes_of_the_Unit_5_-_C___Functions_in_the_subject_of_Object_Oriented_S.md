### Inline functions

- Inline functions are a feature of C++ that allows the compiler to replace a function call with the function body at the point of the call.
- Inline functions can reduce the overhead of function calls, such as pushing and popping arguments and return values on the stack, and jumping to and from the function address.
- Inline functions can also enable the compiler to perform context-specific optimizations, such as constant folding, dead code elimination, and inlining of nested functions.
- Inline functions are declared with the `inline` keyword before the function definition, or implicitly by defining the function inside a class or a `constexpr` specifier.
- Inline functions are only a suggestion to the compiler, and the compiler may choose to ignore it and generate a normal function call instead, depending on various factors such as the size and complexity of the function, the optimization level, and the target architecture.
- Inline functions should be used for small and simple functions that are called frequently, such as getters and setters, arithmetic operations, and utility functions.
- Inline functions should not be used for large and complex functions that may increase the code size and affect the performance negatively, such as recursive functions, loops, I/O operations, and memory allocations.
- Inline functions are different from macros, which are textual replacements performed by the preprocessor before the compilation. Inline functions are subject to the normal rules of C++ syntax and semantics, such as type checking, scope resolution, and name mangling, while macros are not. Inline functions are also safer and more readable than macros.