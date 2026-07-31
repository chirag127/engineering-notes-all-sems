### Higher Order Functions: Treat functions as first class Objects , Lambda Expressions

- In Python, functions are treated as first-class objects. This means that they can be passed as arguments to other functions, returned from functions, and assigned to variables.

- A higher-order function is a function that takes one or more functions as arguments, or that returns a function as its result. Examples of higher-order functions in Python include `map`, `filter`, and `reduce`.

- `map` is a higher-order function that takes a function and an iterable as arguments, and returns a new iterable where the function has been applied to each element in the original iterable.

- `filter` is a higher-order function that takes a function and an iterable as arguments, and returns a new iterable where only the elements for which the function returns `True` are included.

- `reduce` is a higher-order function that takes a function and an iterable as arguments, and returns a single value that is the result of applying the function to the elements of the iterable in a cumulative way.

- A lambda expression is a way of defining a function without using the `def` keyword. It has the form `lambda arguments: expression`, where `arguments` is a comma-separated list of parameters, and `expression` is a single expression that is evaluated and returned whenever the lambda function is called.

- Lambda expressions are often used in conjunction with higher-order functions to create short, anonymous functions that can be passed as arguments.

### Parts of A Function

- A function in Python consists of a header and a body. The header includes the keyword `def`, followed by the function name and a set of parentheses containing the function's parameters (if any). The body of the function is indented and contains the statements that make up the function.

- Parameters are the inputs that a function takes. They are defined in the header of the function and are separated by commas. If a function takes no parameters, the parentheses are still required.

- The `return` keyword is used to return a value from a function. If a function does not contain a return statement, it returns `None` by default.

### Execution of A Function

- To execute a function in Python, you simply call it by its name followed by a set of parentheses containing any arguments that the function requires (if any).

- When a function is called, the arguments that are passed to it are assigned to the function's parameters in the order in which they are passed.

### Keyword and Default Arguments

- Keyword arguments are arguments that are passed to a function by specifying the parameter name, followed by an equals sign and the value. They are useful when a function has a large number of parameters or when the order of the arguments is not important.

- Default arguments are parameters that have a default value specified in the function header. If the argument is not passed to the function, the default value is used instead.

### Scope Rules

- The scope of a variable in Python is the region of the program where the variable is defined and can be accessed.

- The scope of a variable is determined by where it is defined in the program. Variables defined inside a function have local scope, meaning they can only be accessed within the function. Variables defined outside of a function have global scope, meaning they can be accessed anywhere in the program.

- If a variable is defined inside a function with the same name as a variable defined outside the function, the local variable takes precedence over the global variable within the function. However, the global variable can still be accessed by using the `global` keyword.