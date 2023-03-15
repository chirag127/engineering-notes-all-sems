### Macro Vs. Inline functions

- A macro is a preprocessor directive that defines a text substitution rule. A macro can be used to replace a piece of code with another code at compile time.
- An inline function is a function that is expanded in line when it is called. An inline function can be used to avoid the function call overhead and improve the performance of the code.
- Some differences between macro and inline functions are:

  - A macro is not a function, but a text replacement. An inline function is a function with a special keyword.
  - A macro does not perform any type checking or parameter validation. An inline function performs type checking and parameter validation as any other function.
  - A macro can cause side effects or errors if the arguments are not enclosed in parentheses or if the arguments are expressions with operators. An inline function does not cause such problems as the arguments are evaluated only once.
  - A macro can be defined anywhere in the code, even inside another macro. An inline function can be defined only at the global scope or inside a class.
  - A macro can be undefined using the #undef directive. An inline function cannot be undefined.
  - A macro can be used to define constants, expressions, or statements. An inline function can be used to define only functions.