## Unit 4 - Functions

- A function is a block of code that performs a specific task and can be reused in a program.
- A function has a name, a list of parameters, and a return value.
- A function can be defined using the keyword `def` followed by the function name and the parameters in parentheses.
- A function can be called by using the function name followed by the arguments in parentheses.
- A function can return a value using the keyword `return`.

### Types of Functions

- There are two types of functions in Python: built-in functions and user-defined functions.
- Built-in functions are predefined functions that are part of the Python language, such as `print`, `len`, `max`, etc.
- User-defined functions are functions that are created by the programmer to perform a specific task, such as `square`, `factorial`, `greet`, etc.

### Functions with Array

- An array is a collection of elements of the same type that are stored in a contiguous memory location.
- An array can be passed as an argument to a function by using the array name without brackets.
- A function can access and modify the elements of an array by using the index notation.
- A function can return an array by creating a new array inside the function and returning it using the `return` keyword.

### Passing Parameters to Functions

- Parameters are variables that are used to pass information to a function.
- Arguments are the actual values that are passed to a function when it is called.
- There are two ways of passing parameters to a function: call by value and call by reference.

#### Call by Value

- Call by value is the default way of passing parameters to a function in Python.
- In call by value, a copy of the argument value is passed to the parameter variable.
- Any changes made to the parameter variable inside the function do not affect the argument variable outside the function.

#### Call by Reference

- Call by reference is the way of passing parameters to a function in Python when the argument is a mutable object, such as a list, a dictionary, or a set.
- In call by reference, the reference or the address of the argument object is passed to the parameter variable.
- Any changes made to the parameter variable inside the function affect the argument object outside the function.

### Recursive Functions

- A recursive function is a function that calls itself within its body.
- A recursive function must have a base case, which is a condition that stops the recursion, and a recursive case, which is a condition that continues the recursion.
- A recursive function can be used to solve problems that have a repetitive or a recursive structure, such as factorial, Fibonacci, binary search, etc.