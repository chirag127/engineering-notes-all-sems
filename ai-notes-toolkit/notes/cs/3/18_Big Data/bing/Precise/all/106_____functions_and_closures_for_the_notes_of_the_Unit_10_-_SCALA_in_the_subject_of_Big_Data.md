# Unit 10 - SCALA: Functions and Closures

## Functions
- In SCALA, functions are objects.
- Functions can be assigned to variables, passed as arguments to other functions, and returned as values from other functions.
- A function literal is compiled into a class that when instantiated at runtime is a function value.
- A function value is an object that can be invoked in the same way as any other function.

## Closures
- A closure is a function that references variables from outside its body.
- The function can access and modify the value of these variables even if the variables are defined in a different scope.
- Closures capture the variables that are in scope when the function is defined, not when it is invoked.
- This allows the function to access and modify the values of these variables even if they are no longer in scope when the function is invoked.
