
### Macro Vs. Inline functions

* A **macro** is a fragment of code which has been given a name. When the name is used, it is replaced by the body of the macro. Macros are typically used to define constants or to create short snippets of code that can be used over and over again. 

* An **inline function** is a function that is expanded in line when it is called. This means that the code inside the function is inserted in place of the function call, allowing the compiler to optimize the code and make it more efficient. 

* Macros are generally used for simple operations that don't require any parameters, while inline functions are generally used for more complex operations that involve parameters. 

* Macros are generally faster than inline functions, since they don't require the overhead of a function call. However, they can be more difficult to debug, since they don't have the same level of control flow as a function. 

* Inline functions are generally easier to debug, since they have the same control flow as a function. However, they can be slower than macros, since they require the overhead of a function call.