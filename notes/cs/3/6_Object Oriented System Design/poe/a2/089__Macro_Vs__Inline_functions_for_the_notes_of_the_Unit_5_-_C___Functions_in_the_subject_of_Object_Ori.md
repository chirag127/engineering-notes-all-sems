 Here is the content in Markdown format without any emojis or external links, written in points and in a formal tone:

### Macro Vs. Inline functions for the notes of the Unit 5 - C++ Functions

1. Macros:
- Macros are preprocessor directives.
- They are not functions, but are replaced by the preprocessor with the actual code before compilation.
- They are faster than functions as no function call overhead.
- They do not support data types and parameters are replaced textually, leading to issues like variable name collisions.
- They are suitable for conditional compilation and simple replacements.

2. Inline functions:
- Inline functions are real functions defined with the inline keyword.
- The compiler replaces the function call with the function body, potentially leading to faster code.
- However, if the function body is complex, it can lead to code bloat and slower compilation times.
- They support data types and parameters, eliminating issues like variable name collisions.
- They are suitable when the function body is small and speed is a priority. The performance gain depends on the compiler optimization.

In conclusion, while macros and inline functions both lead to faster execution than regular functions by avoiding function call overhead, inline functions are safer and more robust with support for data types. The choice between macros and inline functions depends on the use case and balancing of speed versus other factors.