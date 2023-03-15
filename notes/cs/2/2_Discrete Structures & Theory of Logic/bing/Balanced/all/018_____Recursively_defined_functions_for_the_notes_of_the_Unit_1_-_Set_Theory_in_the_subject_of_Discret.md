# Recursively defined functions

- A recursively defined function is a function that its value at any point can be calculated from the values of the function at some previous points.
- A recursive definition of a function consists of two steps:
  - Basis step: Specify the value of the function at zero or some other initial value.
  - Recursive step: Give a rule for finding its value at an integer from its values at smaller integers.
- For example, suppose a function f(k) = f(k-2) + f(k-3) which is defined over non-negative integers. If we have the value of the function at k = 0 and k = 2, we can also find its value at any other non-negative integer.
- Another example is the factorial function, which is defined as n! = n * (n-1)!, with the basis step of 0! = 1.
- Recursively defined functions can be used to model various phenomena, such as sequences, trees, algorithms, and grammars.
- Recursively defined functions can also be converted to explicit formulas using techniques such as generating functions. A generating function is a formal power series that encodes the values of a sequence as coefficients of the series. By manipulating the generating function, we can find an explicit formula for the sequence.