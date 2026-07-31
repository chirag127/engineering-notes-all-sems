### Recursive definition of functions

- A recursive definition of a function is a way of defining the value of a function for some inputs in terms of the values of the same function for other inputs, usually smaller or simpler.
- A recursive definition of a function consists of two parts: a base case and a recursive step.
- The base case specifies the value of the function for some simple or trivial inputs, such as 0 or 1.
- The recursive step specifies how to compute the value of the function for a larger or more complex input, using the values of the function for smaller or simpler inputs.
- For example, the factorial function n! is defined recursively by the rules:
  - 0! = 1 (base case)
  - (n + 1)! = (n + 1) * n! (recursive step)
- A recursive definition of a function is valid if it satisfies two conditions:
  - Every possible input is eventually reduced to a base case by applying the recursive step finitely many times.
  - The value of the function for any input is uniquely determined by the base case and the recursive step.
- A recursive function is a function that is defined by a recursive definition. Recursive functions are a class of functions on the natural numbers that are studied in computability theory, a branch of mathematical logic.
- Recursive functions can be classified into different types, such as primitive recursive functions, partial recursive functions, and total recursive functions, based on their properties and computational power.
- Recursive functions can be used to model various phenomena and processes in mathematics, logic, computer science, and other fields.