### Inline functions for the notes of the Unit 5 - C++ Functions in the subject of Object Oriented System Design:

- An inline function is a function that is expanded in line when it is called. 
- In C++, inline functions are used to optimize the code and reduce the function call overhead.
- Inline functions are defined using the 'inline' keyword before the function definition.
- Inline functions are usually small functions that are called frequently in the code. 
- The function code is directly inserted in place of the function call at the call site, eliminating the function call overhead. 
- The use of inline functions can improve the performance of the program.
- Inline functions are resolved at compile-time, unlike normal functions that are resolved at run-time.
- Inline functions are not suitable for large functions as they can increase the size of the executable file.
- It is not necessary that a function declared as inline will be inlined by the compiler. It is only a suggestion to the compiler.
- Inline functions can be defined in the header file, which can be included in multiple source files.
- Inline functions can also be overloaded like normal functions.
- Inline functions can access private data members of a class if they are defined inside the class body.
- Inline functions should be used judiciously as their misuse can lead to code bloat and decrease the overall performance of the program.

In conclusion, inline functions are a useful optimization technique in C++ that can improve the performance of the program. However, they should be used carefully and only for small functions that are called frequently.