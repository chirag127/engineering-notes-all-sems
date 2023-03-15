Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for Unit 5 - C++ Functions.

# Unit 5 - C++ Functions

## What is a function?

- A function is a block of code that performs a specific task.
- A function can be called by other parts of the program to execute the code inside the function.
- A function can have parameters, which are variables that are passed to the function when it is called.
- A function can also return a value, which is the result of the function's computation.

## Why use functions?

- Functions help to organize the code into smaller and simpler units.
- Functions help to avoid repetition of code and improve readability and maintainability.
- Functions help to modularize the code and make it easier to test and debug.
- Functions help to reuse the code and implement abstraction and encapsulation.

## How to define a function?

- A function definition consists of four parts: the function name, the parameter list, the return type, and the function body.
- The function name is an identifier that is used to call the function.
- The parameter list is a comma-separated list of variables that are passed to the function when it is called. The parameters are also called arguments or inputs of the function.
- The return type is the data type of the value that the function returns. If the function does not return any value, the return type is void.
- The function body is a block of code that contains the statements that perform the task of the function. The function body is enclosed by curly braces { }.

## How to call a function?

- A function call is an expression that invokes the function and passes the arguments to the function.
- A function call consists of the function name followed by a pair of parentheses ( ) that contain the arguments.
- The arguments must match the parameters in number, order, and data type.
- The function call evaluates to the return value of the function, if any.

## How to declare a function?

- A function declaration is a statement that tells the compiler the name, parameters, and return type of the function, without defining the function body.
- A function declaration is also called a function prototype or a function signature.
- A function declaration is usually placed at the beginning of the program, before the main function, or in a header file.
- A function declaration allows the compiler to check the validity of the function calls and avoid errors.

## How to pass arguments by value and by reference?

- Passing arguments by value means that the function receives a copy of the arguments and does not modify the original variables.
- Passing arguments by reference means that the function receives the memory address of the arguments and can modify the original variables.
- To pass arguments by reference, the parameters must be declared with an ampersand (&) before the variable name, and the arguments must be passed with an ampersand (&) before the variable name.
- Passing arguments by reference can improve the performance and efficiency of the function, as it avoids copying large amounts of data.

## How to use default arguments and const parameters?

- Default arguments are arguments that have a default value assigned to them in the function declaration, and can be omitted in the function call.
- Default arguments are useful when some parameters have a common or expected value, and can simplify the function call and reduce the number of overloaded functions.
- Default arguments must be specified from right to left, and cannot be skipped in the function call.
- Const parameters are parameters that are declared with the keyword const, and cannot be modified by the function.
- Const parameters are useful when the function does not need to change the arguments, and can prevent accidental or unintended changes to the arguments.
- Const parameters can also improve the performance and efficiency of the function, as they can be passed by reference without copying.