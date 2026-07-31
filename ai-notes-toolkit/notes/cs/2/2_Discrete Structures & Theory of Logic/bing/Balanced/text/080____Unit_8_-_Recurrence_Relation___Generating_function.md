## Unit 8 - Recurrence Relation & Generating function

- A **recurrence relation** is an equation that defines a sequence recursively: each term of the sequence is defined as a function of the preceding terms.
- A **generating function** is a formal power series that encodes the information of a sequence in its coefficients.
- Recurrence relations and generating functions are useful tools for analyzing and solving problems involving discrete structures, such as combinatorics, algorithms, and cryptography.
- Some examples of recurrence relations are:

  - The Fibonacci sequence: F(n) = F(n-1) + F(n-2), with F(0) = 0 and F(1) = 1.
  - The factorial function: n! = n * (n-1)!, with 0! = 1.
  - The binomial coefficients: C(n, k) = C(n-1, k-1) + C(n-1, k), with C(n, 0) = C(n, n) = 1.

- Some examples of generating functions are:

  - The geometric series: G(x) = 1 + x + x^2 + x^3 + ... = 1 / (1 - x).
  - The exponential function: E(x) = 1 + x + x^2 / 2! + x^3 / 3! + ... = e^x.
  - The binomial theorem: B(x) = (1 + x)^n = C(n, 0) + C(n, 1) x + C(n, 2) x^2 + ... + C(n, n) x^n.

- To find the generating function of a given sequence, we can use various methods, such as:

  - The method of coefficients: equate the coefficients of the same powers of x in the generating function and the sequence, and solve for the unknowns.
  - The method of substitution: substitute a known generating function into another generating function, and simplify the result.
  - The method of partial fractions: decompose a rational generating function into simpler fractions, and use known formulas to find the corresponding sequences.

- To find the sequence of a given generating function, we can use various methods, such as:

  - The method of differentiation: differentiate the generating function with respect to x, and multiply by x^n to find the coefficient of x^n.
  - The method of integration: integrate the generating function with respect to x, and divide by x^n+1 to find the coefficient of x^n.
  - The method of expansion: expand the generating function using binomial theorem, Taylor series, or other techniques, and read off the coefficients of x^n.