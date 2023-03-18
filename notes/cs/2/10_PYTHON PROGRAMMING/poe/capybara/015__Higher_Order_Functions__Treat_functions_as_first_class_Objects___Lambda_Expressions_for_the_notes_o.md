### Higher Order Functions: Treat functions as first class Objects , Lambda Expressions

- In Python, functions are treated as first class objects. This means that functions can be assigned to variables, passed as arguments to other functions, and returned as values from functions.
- Higher-order functions are those functions that take other functions as arguments or return functions as their results. An example of a higher-order function is the `map()` function which applies a given function to each item of a given iterable.
- Lambda expressions, also known as anonymous functions, are a way to create small, one-time use functions without having to define them with a name. Lambda expressions are often used as arguments to higher-order functions.
- Lambda expressions are defined using the `lambda` keyword followed by the input arguments and the expression to be evaluated. For example, `lambda x: x**2` defines a lambda expression that takes one input argument and returns the square of that argument.
- Lambda expressions can be used to define simple functions for use in higher-order functions. For example, the `sorted()` function can take a lambda expression as an argument to define the sorting order.
- Lambda expressions can also be used to define functions that are passed as arguments to other functions. For example, the `filter()` function can take a lambda expression and an iterable as arguments, and returns an iterable containing only the elements that satisfy the condition defined by the lambda expression.

### Unit 3 - Function: Parts of A Function , Execution of A Function , Keyword and Default Arguments ,Scope Rules

- A function is a block of code that performs a specific task. Functions can be defined using the `def` keyword followed by the function name, input arguments (if any), and the code to be executed.
- Functions can be broken down into several parts: the function signature (function name and input arguments), the function body (code to be executed), and the return statement (if any).
- When a function is called, the input arguments are passed to the function and the code in the function body is executed. The `return` statement (if any) returns a value to the caller of the function.
- Keyword arguments are used to pass arguments to a function by specifying the argument name along with the value. This allows for more flexibility and readability when calling functions with multiple arguments.
- Default arguments are used to provide a default value for an argument if no value is provided when the function is called. This can be useful for cases where a default value is often used, but can be overridden if necessary.
- Scope rules define the visibility of variables within a program. In Python, variables defined inside a function are only visible within that function (local scope). Variables defined outside a function are visible throughout the program (global scope). However, global variables can be accessed and modified from within a function using the `global` keyword.