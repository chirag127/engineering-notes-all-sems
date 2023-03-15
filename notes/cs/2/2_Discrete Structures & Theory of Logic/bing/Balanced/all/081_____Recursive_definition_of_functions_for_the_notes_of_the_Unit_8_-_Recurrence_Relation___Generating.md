# Recursive definition of functions

- A recursive definition of a function defines values of the function for some inputs in terms of the values of the same function for other (usually smaller) inputs.
- A recursive definition of a function consists of two parts: a base case and a recursive step.
- The base case specifies the value of the function for one or more simple inputs, such as 0 or 1.
- The recursive step specifies how to compute the value of the function for a given input by using the value of the function for a smaller input.
- For example, the factorial function n! is defined by the rules:
  - 0! = 1 (base case)
  - (n + 1)! = (n + 1)· n ! (recursive step)
- A recursive definition of a function is also called a recurrence relation or a recurrence equation.
- A recursive function is a function that calls itself in its definition or implementation.
- A recursive function must have a base case to terminate the recursion, otherwise it will result in an infinite loop or a stack overflow.
- A recursive function can be converted into an equivalent iterative function by using a stack or a loop.
- Recursive functions are a class of functions on the natural numbers studied in computability theory, a branch of mathematical logic.
- Recursive functions are also used to model various phenomena in computer science, such as algorithms, data structures, grammars, and languages.