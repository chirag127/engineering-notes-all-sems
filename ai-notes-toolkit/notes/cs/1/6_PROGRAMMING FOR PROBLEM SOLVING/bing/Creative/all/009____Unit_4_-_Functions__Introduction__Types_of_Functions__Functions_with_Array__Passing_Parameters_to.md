## Unit 4 - Functions

- A function is a block of code that performs a specific task and can be reused in a program.
- A function has a name, a list of parameters, and a return value.
- A function can be defined using the keyword `function` followed by the name, the parameters in parentheses, and the body in curly braces.
- A function can be called by using the name followed by the arguments in parentheses.
- A function can be declared before or after the main code, but it must be defined before it is used.

### Types of Functions

- There are two types of functions in programming: built-in functions and user-defined functions.
- Built-in functions are predefined functions that are provided by the programming language or the environment. For example, `print()`, `len()`, `sqrt()`, etc.
- User-defined functions are functions that are created by the programmer to perform a specific task. For example, `factorial()`, `isPrime()`, `reverse()`, etc.

### Functions with Array

- An array is a collection of data elements of the same type, stored in contiguous memory locations.
- An array can be passed as a parameter to a function by using the array name without brackets.
- The function can access the array elements by using the parameter name with brackets and an index.
- The function can modify the array elements by assigning new values to them.
- The function can return an array by using the keyword `return` followed by the array name.

### Passing Parameters to Functions

- Parameters are variables that are used to pass data to a function.
- There are two ways of passing parameters to a function: call by value and call by reference.
- Call by value means that the function receives a copy of the actual parameter value. Any changes made to the parameter inside the function do not affect the original value.
- Call by reference means that the function receives the address of the actual parameter. Any changes made to the parameter inside the function affect the original value.
- In most programming languages, primitive data types (such as int, float, char, etc.) are passed by value, while complex data types (such as arrays, structures, objects, etc.) are passed by reference.

### Recursive Functions

- A recursive function is a function that calls itself within its body.
- A recursive function must have a base case, which is a condition that stops the recursion.
- A recursive function must have a recursive case, which is a condition that reduces the problem to a smaller subproblem and calls the function again.
- A recursive function can be used to solve problems that have a recursive structure, such as factorial, Fibonacci, binary search, etc.