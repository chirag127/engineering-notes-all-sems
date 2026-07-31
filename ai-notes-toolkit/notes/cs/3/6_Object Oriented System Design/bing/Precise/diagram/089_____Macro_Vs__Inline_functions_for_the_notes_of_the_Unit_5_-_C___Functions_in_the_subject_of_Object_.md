### Macro Vs. Inline functions for the notes of the Unit 5 - C++ Functions in the subject of Object Oriented System Design

- **Macro functions** are preprocessor directives that are used to define a piece of code that can be used multiple times in a program. They are defined using the `#define` directive and are replaced by the preprocessor with the defined code before the program is compiled.

- **Inline functions** are functions that are defined with the `inline` keyword. The compiler replaces the function call with the function code, similar to a macro, but with some differences.

- One key difference between macro and inline functions is that inline functions are type-safe, while macros are not. This means that the compiler checks the data types of the arguments passed to an inline function, while it does not do so for macros.

- Another difference is that inline functions can be used in expressions, while macros cannot. For example, an inline function can be used as an argument to another function, while a macro cannot.

- Inline functions can also be used in classes, while macros cannot. This means that inline functions can be used as member functions of a class, while macros cannot.

- In terms of performance, inline functions can be faster than macros because the compiler can optimize the code, while macros are simply text replacements.

- However, inline functions can also increase the size of the code because the function code is duplicated at each function call. Macros do not have this issue because they are replaced by the preprocessor before the program is compiled.

- In general, it is recommended to use inline functions over macros because they are type-safe, can be used in expressions and classes, and can be optimized by the compiler. However, macros can still be useful in certain situations, such as when defining constants or simple text replacements.