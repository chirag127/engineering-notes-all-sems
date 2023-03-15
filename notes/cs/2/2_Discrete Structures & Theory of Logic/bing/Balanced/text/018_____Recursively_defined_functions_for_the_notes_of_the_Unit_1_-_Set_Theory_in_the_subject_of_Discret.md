### Recursively defined functions

- A recursively defined function is a function that its value at any point can be calculated from the values of the function at some previous points .
- A recursively defined function consists of two parts: a base case and a recursive step.
- The base case specifies the value of the function for some initial values of the variable, usually the smallest or simplest ones.
- The recursive step specifies how to compute the value of the function for any other value of the variable, using the values of the function for smaller or simpler values of the variable.
- For example, the factorial function n! can be defined recursively as follows:
  - Base case: 0! = 1
  - Recursive step: For any positive integer n, n! = n * (n-1)!
- A recursively defined function can also be represented by a recurrence relation, which is an equation that expresses the value of the function in terms of its previous values.
- For example, the recurrence relation for the factorial function is: a_n = n * a_(n-1), with a_0 = 1
- A recurrence relation can be solved to find an explicit formula for the function, which does not depend on its previous values.
- For example, the explicit formula for the factorial function is: n! = n * (n-1) * (n-2) * ... * 2 * 1
- Some methods to solve recurrence relations are: substitution, iteration, characteristic equation, generating functions, etc.