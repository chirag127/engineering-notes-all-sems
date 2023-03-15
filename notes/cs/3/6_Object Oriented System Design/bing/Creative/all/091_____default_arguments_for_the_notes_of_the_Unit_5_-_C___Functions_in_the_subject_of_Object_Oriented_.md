Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of default arguments for the notes of the Unit 5 - C++ Functions in the subject of Object Oriented System Design.

# Default Arguments

- Default arguments are arguments that have a predefined value in the function declaration.
- Default arguments can be used to simplify the function call and avoid passing unnecessary arguments.
- Default arguments are specified by assigning a value to the parameter in the function declaration, after the parameter type and name, such as `void print(int x = 10)`.
- Default arguments can only be omitted from the rightmost parameters in the function call, such as `print()` or `print(5)`, but not `print(, 5)`.
- Default arguments can be overridden by passing a different value in the function call, such as `print(20)`.
- Default arguments can be used in combination with regular arguments, as long as the regular arguments are placed before the default arguments in the function declaration and call, such as `void print(int x, int y = 10, int z = 20)`.
- Default arguments can be used in any type of function, such as constructors, member functions, friend functions, etc.
- Default arguments can be expressions that involve constants, variables, or function calls, as long as they are valid and can be evaluated at the time of the function call, such as `void print(int x = a + b, int y = pow(2, 3))`.
- Default arguments can be declared only once in the function declaration, and not in the function definition, if they are separate. If the function declaration and definition are combined, the default arguments can be specified only in the combined definition.