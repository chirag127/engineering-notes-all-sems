Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of Macro Vs. Inline functions for the notes of the Unit 5 - C++ Functions in the subject of Object Oriented System Design.

### Macro Vs. Inline functions

- A macro is a preprocessor directive that defines a name for a piece of code that can be substituted wherever the name is used. An inline function is a function that is defined with the keyword `inline` and is expanded by the compiler at the point of call.
- Macros are processed before compilation, while inline functions are processed during compilation.
- Macros do not perform type checking or argument validation, while inline functions do.
- Macros can cause side effects or errors due to multiple evaluations of arguments or operator precedence issues, while inline functions avoid these problems by using local variables and parentheses.
- Macros can be used to define constants, expressions, or statements, while inline functions can only be used to define functions.
- Macros have global scope and can be undefined using the `#undef` directive, while inline functions have the same scope as regular functions and cannot be undefined.
- Macros can be used to achieve generic programming by using the `##` operator or variadic arguments, while inline functions can use templates or overloading to achieve the same.
- Macros can be debugged using the `#line` directive or by examining the preprocessed code, while inline functions can be debugged using the normal debugging tools.
- Macros can improve performance by avoiding function call overhead, while inline functions can also improve performance by allowing the compiler to perform optimizations such as constant folding, code inlining, or dead code elimination. However, both macros and inline functions can also increase the code size and affect the cache efficiency.