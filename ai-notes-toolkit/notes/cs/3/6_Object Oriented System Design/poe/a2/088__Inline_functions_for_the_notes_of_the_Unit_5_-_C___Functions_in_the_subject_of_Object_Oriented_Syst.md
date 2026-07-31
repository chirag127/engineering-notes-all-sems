 Here is the content in Markdown format without any emojis or external links, being formal and not showing any feelings:

### Inline functions for the notes of the Unit 5 - C++ Functions in the subject of Object Oriented System Design:

1. Inline functions are the functions whose body is substituted or replaced at each call site. This means that the compiler inserts the code of the inline function at each call site, instead of jumping to the function definition to execute it.
2. The main advantage of inline functions is that the overhead of function calls (like parameter passing and return value) can be avoided. This can improve the performance.
3. However, inlining is not always beneficial. If the function body is large, inlining may lead to code bloat as the code size can increase significantly. This can actually degrade the performance due to increased instruction cache miss rate.
4. Inlining is just a request to the compiler, not a command. The compiler can ignore the request if it deems fit. Usually the compiler does not inline a function if:
- It is too large
- It is called in few places (as inlining may lead to unnecessary bloat)
- It is recursive or has loop constructs (as inlining may lead to complicated code)

To summarize, inline functions can improve performance by avoiding function call overhead but inlining large or complex functions may degrade performance due to code bloat. The compiler makes the final decision whether to inline a function or not.