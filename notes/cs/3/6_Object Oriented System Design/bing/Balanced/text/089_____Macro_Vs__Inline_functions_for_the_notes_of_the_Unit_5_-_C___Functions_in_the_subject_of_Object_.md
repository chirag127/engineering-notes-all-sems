### Macro Vs. Inline functions

- A macro is a preprocessor directive that defines a text substitution rule. A macro can be used to replace a piece of code with another code at compile time.
- An inline function is a function that is expanded in place of its call site by the compiler. An inline function can be used to avoid the overhead of function calls and improve performance.
- Some differences between macro and inline functions are:

  - Macros are processed by the preprocessor, while inline functions are processed by the compiler.
  - Macros do not perform type checking or argument validation, while inline functions do.
  - Macros can cause side effects or errors if not used carefully, while inline functions are safer and more reliable.
  - Macros can be used for any text substitution, while inline functions can only be used for function definitions.
  - Macros are always expanded at the call site, while inline functions are only expanded if the compiler decides to do so. The inline keyword is only a suggestion to the compiler, not a command.