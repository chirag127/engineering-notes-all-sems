### Inline functions for the notes of the Unit 5 - C++ Functions in the subject of Object Oriented System Design

Inline functions are a type of function in C++ that are used to reduce the function call overhead. They are typically used for small functions that are called frequently in a program.

Some important points to remember about inline functions are:

- They are defined using the `inline` keyword before the function definition.
- They are expanded inline by the compiler, which means that the code of the function is directly inserted at the place where the function is called.
- They are usually used for small functions to avoid the overhead of function call, but it is not necessary for all small functions to be defined inline.
- They can be defined inside a class definition or outside it.
- They can be called like any other function using the function name and arguments.

Advantages of using inline functions:

- They can reduce the function call overhead and improve the performance of the program.
- They can be used for small functions that are called frequently, to avoid the overhead of function call.
- They can be used to optimize the program by reducing the number of function calls.

Disadvantages of using inline functions:

- They can increase the size of the executable code, as the code of the function is directly inserted at the place where it is called.
- They can cause code bloat if used extensively, which can increase the memory usage of the program.

Example of an inline function:

```c++
inline int square(int n) {
    return n * n;
}
```

Applications of inline functions:

- They are commonly used in performance-critical applications, such as games and real-time systems, to improve the performance of the program.
- They can be used in libraries and frameworks to provide optimized functions for the users.

In conclusion, inline functions are a useful tool in C++ programming to improve the performance of the program by reducing the overhead of function call. However, they should be used judiciously, as they can cause code bloat and increase the size of the executable code.