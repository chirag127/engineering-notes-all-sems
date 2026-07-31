### Macro Vs. Inline functions

- A macro is a preprocessor directive that defines a text substitution rule. A macro can be used to replace a piece of code with another code at compile time.
- An inline function is a function that is expanded in place when it is called. An inline function can be used to avoid the function call overhead and improve the performance of the code.
- Some differences between macro and inline functions are:

  - A macro is not a function, but a text replacement. An inline function is a function with a special keyword.
  - A macro does not perform any type checking or parameter validation. An inline function does.
  - A macro can cause side effects or errors if the arguments are not enclosed in parentheses or if the macro body contains multiple statements. An inline function does not have these problems.
  - A macro is always expanded by the preprocessor. An inline function is only a suggestion to the compiler, which may or may not inline it depending on various factors.
  - A macro can be defined anywhere in the code. An inline function must be defined before it is used or in the same translation unit.