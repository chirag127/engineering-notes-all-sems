# Higher Order Functions: Treat functions as first class Objects, Lambda Expressions

## Unit 3 - Function: Parts of A Function, Execution of A Function, Keyword and Default Arguments, Scope Rules

### Higher Order Functions
- Higher order functions are functions that operate on other functions, either by taking them as arguments or by returning them.
- In Python, functions are first-class objects, which means they can be treated like any other object, such as an integer, string, or list.
- This allows us to pass functions as arguments to other functions, return functions from other functions, and assign functions to variables.

### Lambda Expressions
- Lambda expressions are a way to create small, anonymous functions in Python.
- They are often used as arguments to higher-order functions that expect a function as one of their arguments.
- Lambda expressions are written using the `lambda` keyword, followed by a list of arguments, a colon, and an expression.
- The expression is evaluated and returned when the lambda function is called.

### Parts of a Function
- A function in Python is defined using the `def` keyword, followed by the function name, a pair of parentheses containing the function's parameters, and a colon.
- The body of the function is indented and contains the statements that define what the function does.
- The `return` statement is used to specify the value that the function should return.

### Execution of a Function
- When a function is called, the statements in the function's body are executed in the order in which they appear.
- If the function includes a `return` statement, the function will return the value specified by the `return` statement and the execution of the function will end.
- If the function does not include a `return` statement, the function will return `None` by default.

### Keyword and Default Arguments
- When calling a function, you can specify the values of the function's arguments using either positional or keyword arguments.
- Positional arguments are specified in the order in which they appear in the function's definition.
- Keyword arguments are specified using the argument's name, followed by an equal sign and the value of the argument.
- Default arguments are arguments that have a default value specified in the function's definition. If a default argument is not specified when calling the function, the default value will be used.

### Scope Rules
- The scope of a variable refers to the region of the program where the variable can be accessed.
- In Python, there are two main types of scope: global and local.
- Global variables are defined outside of any function and can be accessed from anywhere in the program.
- Local variables are defined within a function and can only be accessed within that function.
- If a variable with the same name is defined in both the global and local scope, the local variable will take precedence within the function where it is defined.
