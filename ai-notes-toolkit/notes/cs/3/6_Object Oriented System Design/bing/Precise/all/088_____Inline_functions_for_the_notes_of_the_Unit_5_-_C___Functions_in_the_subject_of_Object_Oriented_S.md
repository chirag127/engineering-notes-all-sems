# Inline Functions

An inline function is a function that is expanded in line when it is called. When the inline function is called, the complete body of the function is substituted at the point of the call. This substitution is performed by the C++ compiler at compile time.

Here are some key points to remember about inline functions:

1. Inline functions are used to reduce the function call overhead.
2. Inline functions are similar to macros, but they are safer and more powerful.
3. The inline keyword is used to define an inline function.
4. The inline keyword is a request to the compiler, not a command. The compiler may choose to ignore the request and treat the function as a normal function.
5. Inline functions should be small and simple. Complex functions should not be made inline.
6. Inline functions are defined in the header file, not in the source file.
7. The use of inline functions can improve the performance of a program, but it can also increase the size of the executable file.
