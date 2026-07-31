Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is some content in markdown format that you can use for your study material.

## Unit 3 - Function: Parts of A Function , Execution of A Function , Keyword and Default Arguments ,Scope Rules.

- A function is a block of code that performs a specific task, such as printing a message, calculating a value, or sorting a list.
- A function can be defined using the `def` keyword, followed by the function name and a pair of parentheses that may contain some parameters.
- A function can be called by using the function name and a pair of parentheses that may contain some arguments that match the parameters.
- A function can return a value to the caller using the `return` statement, or return `None` by default if there is no `return` statement.
- A function can have four types of parameters: positional, keyword, default, and variable-length.
  - Positional parameters are the ones that must be passed in the same order as they are defined in the function header.
  - Keyword parameters are the ones that can be passed by using the parameter name and an equal sign, regardless of their order in the function header.
  - Default parameters are the ones that have a default value assigned to them in the function header, and can be omitted when calling the function.
  - Variable-length parameters are the ones that can accept an arbitrary number of arguments, and are prefixed with an asterisk (*) for positional arguments or a double asterisk (**) for keyword arguments.
- A function can have four types of arguments: positional, keyword, default, and variable-length.
  - Positional arguments are the ones that match the positional parameters in the function header, and are passed in the same order as they are defined.
  - Keyword arguments are the ones that match the keyword parameters in the function header, and are passed by using the parameter name and an equal sign, regardless of their order in the function header.
  - Default arguments are the ones that match the default parameters in the function header, and are omitted when calling the function, or can be overridden by passing a different value.
  - Variable-length arguments are the ones that match the variable-length parameters in the function header, and are passed as a tuple for positional arguments or a dictionary for keyword arguments.
- A function can have two types of scope: local and global.
  - Local scope is the scope within a function, where the local variables are defined and accessed.
  - Global scope is the scope outside of any function, where the global variables are defined and accessed.
  - A local variable can only be accessed within the function where it is defined, and is not visible to other functions or the global scope.
  - A global variable can be accessed anywhere in the program, including within functions, unless there is a local variable with the same name that shadows it.
  - A local variable can be made global by using the `global` keyword before its name, which allows it to be accessed and modified in the global scope.
  - A global variable can be accessed within a function by using the `global` keyword before its name, which allows it to be modified in the global scope.