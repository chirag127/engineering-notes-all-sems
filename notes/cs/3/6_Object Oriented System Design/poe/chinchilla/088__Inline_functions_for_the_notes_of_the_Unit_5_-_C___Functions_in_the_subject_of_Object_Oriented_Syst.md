### Inline functions for the notes of the Unit 5 - C++ Functions in the subject of Object Oriented System Design

In C++, a function can be defined as inline by using the `inline` keyword. Inline functions are a special kind of function that are expanded in place of a function call at compile time, rather than being called at runtime. This can result in faster code execution, as the overhead of a function call is eliminated.

Here are some important points to keep in mind when working with inline functions:

- Inline functions are typically used for small, frequently-called functions, such as accessors and mutators.
- The `inline` keyword should be placed before the function declaration in the header file.
- The function definition should be included in the header file, rather than a separate implementation file.
- Inline functions can only be defined within the same translation unit (i.e. source file) as where they are called from. This means that if an inline function is defined in a header file, it should be included in every source file that uses it.
- Inline functions can be more efficient than regular functions, but they can also increase the size of the compiled code. This is because the code for the function is copied into every place where it is called, rather than being located in a single place.
- It is important to note that the `inline` keyword is only a suggestion to the compiler. The compiler may choose not to inline a function if it determines that doing so would not result in faster code execution.
- Finally, it is good practice to only use the `inline` keyword for functions that are actually performance-critical. Overuse of inline functions can lead to larger code size and longer compile times, without any significant performance benefits.

In summary, inline functions can be a useful tool for improving the performance of C++ code, but they should be used judiciously and with care. By following the guidelines outlined above, developers can ensure that their inline functions are both efficient and maintainable.