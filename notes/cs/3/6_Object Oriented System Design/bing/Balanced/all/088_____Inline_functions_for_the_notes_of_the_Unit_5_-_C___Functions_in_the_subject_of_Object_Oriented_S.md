# Inline functions

- Inline functions are a feature of C++ that allows the compiler to replace the function call with the function body at the point of the call  .
- Inline functions can reduce the overhead of function calls, such as pushing and popping arguments and return values on the stack, and jumping to and from the function address .
- Inline functions can also enable the compiler to perform context-specific optimizations, such as constant folding, dead code elimination, and inlining of nested functions .
- Inline functions are declared with the `inline` keyword before the function name or definition   .
- Inline functions can also be implicitly declared by defining them entirely inside a class, struct, or union definition, or by declaring them `constexpr`.
- Inline functions are only a suggestion to the compiler, and the compiler may choose to ignore it and generate a normal function call instead    .
- Inline functions are best used for small and simple functions, such as getters and setters, that are called frequently and do not have loops, recursion, or static variables  .
- Inline functions should not be used for large and complex functions, such as those that perform input/output, memory allocation, or exception handling, as they may increase the code size and reduce the cache efficiency  .
- Inline functions are different from macros, which are textual substitutions performed by the preprocessor, and do not follow the rules of C++ syntax and semantics .
- Inline functions have the following advantages over macros :
  - Inline functions are type-safe and can perform type checking and conversions.
  - Inline functions can be debugged and stepped into with a debugger.
  - Inline functions can have default arguments and overloaded versions.
  - Inline functions can be scoped and have access specifiers.