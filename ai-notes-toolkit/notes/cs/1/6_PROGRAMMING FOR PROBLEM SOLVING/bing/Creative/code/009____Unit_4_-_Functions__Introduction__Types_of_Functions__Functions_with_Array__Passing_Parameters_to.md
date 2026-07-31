```
## Unit 4 - Functions

- A function is a block of code that performs a specific task and can be reused in a program.
- A function has a name, a list of parameters, and a return value.
- A function can be defined using the `def` keyword, followed by the function name and the parameters in parentheses.
- A function can be called by using the function name and passing the arguments in parentheses.
- A function can return a value using the `return` statement.

### Types of Functions

- There are two types of functions in Python: built-in functions and user-defined functions.
- Built-in functions are predefined functions that are part of the Python language, such as `print`, `len`, `sum`, etc.
- User-defined functions are functions that are created by the programmer to perform a specific task.
- User-defined functions can be stored in a separate file and imported using the `import` statement.

### Functions with Array

- An array is a collection of elements of the same data type, stored in a contiguous memory location.
- An array can be passed as an argument to a function by using the array name without brackets.
- A function can access and modify the elements of an array by using the index notation.
- A function can return an array by creating a new array inside the function and returning it using the `return` statement.

### Passing Parameters to Functions

- Parameters are variables that are used to receive the values passed to a function when it is called.
- Arguments are the actual values that are passed to a function when it is called.
- There are two ways of passing parameters to functions: call by value and call by reference.

#### Call by Value

- Call by value is the default way of passing parameters to functions in Python.
- In call by value, a copy of the argument value is passed to the parameter, and any changes made to the parameter inside the function do not affect the original argument.
- Call by value is suitable for passing immutable data types, such as numbers, strings, tuples, etc.

#### Call by Reference

- Call by reference is the way of passing parameters to functions in Python that allows the function to modify the original argument.
- In call by reference, the argument and the parameter refer to the same object in memory, and any changes made to the parameter inside the function affect the original argument.
- Call by reference is suitable for passing mutable data types, such as lists, dictionaries, sets, etc.

### Recursive Functions

- A recursive function is a function that calls itself within its own definition.
- A recursive function must have a base case, which is a condition that stops the recursion, and a recursive case, which is a condition that continues the recursion.
- A recursive function can be used to solve problems that have a repetitive or recursive structure, such as factorial, Fibonacci, binary search, etc.
- A recursive function can be more elegant and concise than an iterative function, but it can also be less efficient and more prone to errors.
```