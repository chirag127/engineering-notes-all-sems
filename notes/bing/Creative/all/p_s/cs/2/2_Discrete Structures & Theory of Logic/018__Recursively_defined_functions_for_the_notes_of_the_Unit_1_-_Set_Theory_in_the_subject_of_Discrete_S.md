### Recursively defined functions

- A recursively defined function is a function that its value at any point can be calculated from the values of the function at some previous points .
- A recursively defined function consists of two parts: a base case and a recursive step.
- The base case specifies the value of the function for some initial values of the variable, usually the smallest or simplest ones.
- The recursive step specifies how to obtain the value of the function for any other value of the variable, usually by using the value of the function for a smaller or simpler value of the variable.
- For example, the factorial function n! can be defined recursively as follows:

  - Base case: 0! = 1
  - Recursive step: for any positive integer n, n! = n * (n-1)!

- Another example is the Fibonacci sequence, which can be defined recursively as follows:

  - Base case: F(0) = 0, F(1) = 1
  - Recursive step: for any positive integer n, F(n) = F(n-1) + F(n-2)

- Recursively defined functions are useful for modeling phenomena that have a self-similar or iterative structure, such as fractals, trees, algorithms, etc.
- Recursively defined functions can also be converted into explicit formulas by using techniques such as generating functions, induction, or recurrence relations  .
- For example, the explicit formula for the Fibonacci sequence is:

  - F(n) = (1/sqrt(5)) * (((1 + sqrt(5))/2)^n - ((1 - sqrt(5))/2)^n)

Some possible mnemonics and learning tricks for the topic are:

- To remember the base case and the recursive step of the factorial function, you can use the acronym B.R.A.N.D: Base case is 0! = 1, Recursive step is n! = n * (n-1)!
- To remember the base case and the recursive step of the Fibonacci sequence, you can use the acronym B.R.A.F: Base case is F(0) = 0, F(1) = 1, Recursive step is F(n) = F(n-1) + F(n-2)
- To remember the explicit formula for the Fibonacci sequence, you can use the rhyme: One over root of five, times the golden ratio to the power of n, minus the negative golden ratio to the power of n.