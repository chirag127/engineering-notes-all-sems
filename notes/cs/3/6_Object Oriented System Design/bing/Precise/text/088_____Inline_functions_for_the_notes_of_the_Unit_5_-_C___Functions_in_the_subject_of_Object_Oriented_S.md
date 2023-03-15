### Inline functions
- Inline functions are a feature of C++ that allows the compiler to expand the function code in place of the function call, instead of generating a call to the function.
- This can improve the performance of the code by reducing the overhead of calling a function.
- To define an inline function, the keyword `inline` is used before the function definition.
- The decision to inline a function is ultimately made by the compiler, and it may choose not to inline a function even if it is declared as inline.
- Inline functions are best used for small, frequently called functions, as inlining large functions can increase the size of the compiled code.
- It is important to note that the definition of an inline function must be present in the same translation unit as the call to the function, otherwise the compiler will not be able to inline the function.