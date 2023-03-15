# Unit 5 - C++ Functions in Object Oriented System Design

### Macro Vs. Inline functions

- **Macro functions** are preprocessor directives that are expanded by the preprocessor before the code is compiled. They are defined using the `#define` directive and can take arguments like a function.

- **Inline functions** are functions that are expanded in line when they are called. The compiler replaces the function call with the function code, similar to how a macro is expanded.

- The main difference between macro and inline functions is that inline functions are parsed by the compiler, while macro functions are expanded by the preprocessor.

- This means that inline functions have the benefits of type checking and can use features such as default arguments and function overloading, while macro functions cannot.

- Inline functions can also be more efficient than macro functions, as the compiler can optimize the function code when it is expanded in line.

- However, inline functions can increase the size of the compiled code, as the function code is duplicated each time the function is called.

- In general, it is recommended to use inline functions over macro functions, as they provide better type safety and can be more efficient. However, there may be cases where macro functions are more appropriate, such as when defining simple, frequently used operations.