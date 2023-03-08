 Here is the content in markdown format for the topic ### Macro Vs. Inline functions for the notes of the Unit 5 - C++ Functions in the subject of Object Oriented System Design:

## Macro Vs. Inline functions

### Macros:

- Macros are preprocessor directives. They are not actual functions.
- Macros are replaced by the preprocessor with the actual code/text before actual compilation.
- Macros are faster as they are just find and replace actions by the preprocessor. No function call overhead.
- Macros can lead to syntax errors if not defined properly as they just do textual replacement.
- Macros can be redefined and cause unintended side effects if not handled properly.
- Macros are generally used for conditional compilations and simple replacements.

### Inline functions:

- Inline functions are actual functions defined in the code.
- The compiler inserts the function body into the call site to avoid the function call overhead.
- Inline functions retain type safety as they are proper functions with parameters and return types.
- The size of the code increases as the function body is duplicated at each call site.
- The compiler may ignore the inline keyword if the function body is too large.
- Inline functions are used to improve performance for small function calls.

Advantages and disadvantages can be compared and suited use cases can be chosen based on the requirements. Both have specific use cases where one would be more suitable than the other. Detailed examples and codes can be included to learn the concepts in depth. Applications in real world scenarios can also be discussed to understand the practical usage of macros and inline functions.