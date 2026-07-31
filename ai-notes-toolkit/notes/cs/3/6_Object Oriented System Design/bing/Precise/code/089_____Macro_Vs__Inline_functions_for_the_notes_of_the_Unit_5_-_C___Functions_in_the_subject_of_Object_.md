### Macro Vs. Inline functions for the notes of the Unit 5 - C++ Functions in the subject of Object Oriented System Design

- **Macro functions** are preprocessor directives that are expanded by the preprocessor before the program is compiled. They are defined using the `#define` directive and can take arguments like a function.

- **Inline functions** are functions that are expanded by the compiler at the point of call, rather than being called like a normal function. They are defined using the `inline` keyword before the function definition.

- The main difference between macro and inline functions is the way they are expanded. Macro functions are expanded by the preprocessor, while inline functions are expanded by the compiler.

- Macro functions can be faster than normal functions because they avoid the overhead of a function call. However, they can also be less efficient because they are expanded every time they are used, which can increase the size of the code.

- Inline functions can also be faster than normal functions because they avoid the overhead of a function call. However, the compiler may choose not to inline a function if it determines that it would not be beneficial.

- Macro functions do not have the same type checking and scoping rules as normal functions. This can lead to errors and unexpected behavior if not used carefully.

- Inline functions have the same type checking and scoping rules as normal functions, which can make them safer to use.

- In general, it is recommended to use inline functions over macro functions whenever possible, as they provide better type checking and scoping, and can be more efficient in some cases. However, there may be situations where macro functions are more appropriate, such as when working with low-level code or when performance is critical.