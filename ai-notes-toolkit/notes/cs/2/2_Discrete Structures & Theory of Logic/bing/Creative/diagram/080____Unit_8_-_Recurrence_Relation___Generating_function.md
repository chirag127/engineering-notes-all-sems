## Unit 8 - Recurrence Relation & Generating function

A recurrence relation is an equation that defines a sequence recursively: each term of the sequence is defined as a function of the preceding terms.

A generating function is a formal power series in the form of an infinite polynomial that encodes a sequence of numbers by using the coefficients of the polynomial.

Some examples of recurrence relations and their corresponding generating functions are:

- The Fibonacci sequence: F(n) = F(n-1) + F(n-2), F(0) = 0, F(1) = 1

  The generating function for the Fibonacci sequence is:

  `F(x) = x/(1-x-x^2)`

- The factorial sequence: n! = n * (n-1)!, 0! = 1

  The generating function for the factorial sequence is:

  `F(x) = 1/(1-x)`

- The Catalan numbers: C(n) = (2n)!/(n!(n+1)!), C(0) = 1

  The generating function for the Catalan numbers is:

  `F(x) = 1/(1-sqrt(1-4x))`

Some methods to find the generating function for a given recurrence relation are:

- Using the properties of generating functions, such as linearity, differentiation, multiplication, etc.
- Using the partial fraction decomposition to split the generating function into simpler fractions
- Using the binomial theorem to expand the generating function into a power series
- Using the convolution formula to find the generating function for the product of two sequences

Some applications of recurrence relations and generating functions are:

- Solving combinatorial problems, such as counting the number of ways to arrange objects, partition sets, construct trees, etc.
- Analyzing the complexity of algorithms, such as finding the running time or the number of comparisons of recursive algorithms
- Studying the properties of sequences, such as finding the closed-form formula, the asymptotic behavior, the recurrence depth, etc.