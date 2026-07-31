# Macro Vs. Inline functions

- A macro is a preprocessor directive that defines a text substitution rule. A macro can be used to replace a piece of code with another code at compile time.
- An inline function is a function that is expanded in place of its call site by the compiler. An inline function can be used to avoid the overhead of function calls and improve performance.
- Some differences between macro and inline functions are:

  - A macro is not a function, but a text replacement. Therefore, it does not follow the syntax and semantics of C++ functions. A macro can cause errors or unexpected results if not used carefully.
  - An inline function is a function, but with a hint to the compiler to expand it inline. Therefore, it follows the syntax and semantics of C++ functions. An inline function can be safer and more reliable than a macro.
  - A macro can be defined anywhere in the source code, and it is visible until it is undefined or the end of the file is reached. A macro can have global or local scope, depending on where it is defined.
  - An inline function can be defined only inside a class or a namespace, and it is visible only within its scope. An inline function can have public, private, or protected access, depending on how it is declared.
  - A macro can take any number of arguments, and the arguments are not checked for type or number. A macro can also have no arguments, or use variable arguments.
  - An inline function can take only a fixed number of arguments, and the arguments are checked for type and number. An inline function cannot have no arguments, or use variable arguments.
  - A macro can be used to define constants, expressions, statements, or even entire functions. A macro can also be used to conditionally compile code, using #ifdef and #endif directives.
  - An inline function can be used to define only functions. An inline function cannot be used to conditionally compile code, as it is always compiled.