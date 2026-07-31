### Inline Functions

- An inline function is a function that is expanded in line when it is called.
- When the inline function is called, the complete definition of the function is substituted for the function call.
- An inline function is defined using the `inline` keyword before the function definition.
- The use of inline functions can improve the execution time of a program, as it avoids the overhead of a function call.
- However, the use of inline functions can also increase the size of the compiled code, as the function code is duplicated for each call.
- The decision to make a function inline should be based on a trade-off between execution time and code size.
- The compiler may choose to ignore the `inline` keyword and not inline the function, if it determines that inlining the function would not be beneficial.
- Inline functions are commonly used for small, frequently called functions, such as accessor functions.
