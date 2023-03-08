 Here is the content in markdown format for the topic ### Inline functions for the notes of the Unit 5 - C++ Functions in the subject of Object Oriented System Design:

Inline functions:
- Inline functions are functions whose bodies are expanded in line when they are called.
- The expansion happens by replacing the function call with the actual function body.
- This results in potentially faster execution as the overhead of function call like jumping to the function, setting up stack frame etc is avoided.
- The size of the code increases due to repetition. So inlining is useful for small functions.
- The keyword `inline` is used to suggest to the compiler that it may be beneficial to insert the body of the function in line. The compiler may or may not follow the suggestion.
- Advantages:
  - Faster execution due to avoiding overhead of function calls.
  - May enable more optimizations as more code is visible to the compiler.
- Disadvantages:
  - Code size increase leading to larger executable size.
  - Too much inlining can lead to inefficient use of instruction cache.
- Whether to make a function inline or not is decided by the compiler based on the above factors. The `inline` keyword is just a suggestion.
- Example:

```cpp
inline int max(int a, int b) {
    return a > b ? a : b;
}
```

- Application: Inline functions are useful for very small functions like getters and setters. Mathematical functions with simple logic can also benefit from inlining.