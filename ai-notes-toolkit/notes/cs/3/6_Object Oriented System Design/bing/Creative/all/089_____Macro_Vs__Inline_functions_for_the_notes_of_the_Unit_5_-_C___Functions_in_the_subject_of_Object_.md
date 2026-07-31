# Macro Vs. Inline functions

- A macro is a preprocessor directive that defines a text substitution for a given identifier. An inline function is a function that is expanded at the point of call, avoiding the overhead of a function call.
- Some of the differences between macro and inline functions are:

  - Macros work through text substitution, whereas inline functions duplicate the logic of a function.
  - Macros are error prone due to substitution, especially when the arguments have side effects, whereas inline functions are safe to use.
  - Macros can't be assigned to function pointers, whereas inline functions can.
  - Macros can be used for any text substitution, not just functions, whereas inline functions are limited to functions.
  - Macros are processed by the preprocessor before compilation, whereas inline functions are expanded by the compiler during compilation.
  - Macros do not perform any type checking or argument validation, whereas inline functions do.
  - Macros do not obey the scope rules, whereas inline functions do.
  - In C++, inline functions may be defined either inside the class or outside the class, whereas macros are always defined at the beginning of the program.
  - In C++, short length functions inside the class are automatically made inline functions, whereas macros are explicitly defined.

- Some of the advantages of using inline functions over macros are:

  - Inline functions are more readable and maintainable than macros.
  - Inline functions can be debugged easily, whereas macros can cause problems during debugging.
  - Inline functions can be overloaded and inherited, whereas macros can't.
  - Inline functions can use templates, whereas macros can't.

- Some of the disadvantages of using inline functions over macros are:

  - Inline functions may increase the code size and memory usage, whereas macros do not.
  - Inline functions may not be inlined by the compiler in some cases, such as recursive functions, virtual functions, or functions with loops.
  - Inline functions may cause multiple definitions of the same function in different translation units, whereas macros do not.

- Some of the situations where macros are preferred over inline functions are:

  - When the text substitution is not a function, such as a constant or an expression.
  - When the text substitution is very simple and does not involve any computation or logic.
  - When the text substitution needs to access the line number, file name, or other predefined macros.
  - When the text substitution needs to be conditional based on the compiler or platform.