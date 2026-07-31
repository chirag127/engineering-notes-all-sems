## Unit 3 - Function: Parts of A Function , Execution of A Function , Keyword and Default Arguments ,Scope Rules.

- A function is a block of code that performs a specific task, such as printing a message, calculating a value, or sorting a list.
- A function can be defined using the `def` keyword, followed by the function name and a pair of parentheses that may contain some parameters.
- A function can be called by using the function name followed by a pair of parentheses that may contain some arguments.
- A function can return a value to the caller using the `return` statement, or return `None` by default if there is no `return` statement.
- A function can have four types of parameters: positional, keyword, default, and variable-length.
- Positional parameters are the ones that are specified in the function definition and must be passed in the same order by the caller.
- Keyword parameters are the ones that are specified in the function definition and can be passed by using the parameter name and an equal sign, regardless of the order.
- Default parameters are the ones that are specified in the function definition and have a default value assigned to them, which is used if the caller does not provide a value for that parameter.
- Variable-length parameters are the ones that are prefixed with an asterisk (*) or a double asterisk (**), and can accept any number of arguments from the caller. The single asterisk (*) creates a tuple of positional arguments, while the double asterisk (**) creates a dictionary of keyword arguments.
- A function can have a docstring, which is a string literal that appears as the first statement in the function body, and describes the purpose and usage of the function.
- A function can have local and global variables. Local variables are the ones that are defined inside the function body and are only accessible within the function. Global variables are the ones that are defined outside the function body and are accessible throughout the program.
- A function can modify a global variable by using the `global` keyword inside the function body, which tells the interpreter that the variable is not local but global.
- A function can also have nonlocal variables, which are the ones that are defined in the enclosing function, and are accessible by the nested function. A nested function can modify a nonlocal variable by using the `nonlocal` keyword inside the function body, which tells the interpreter that the variable is not local but nonlocal.