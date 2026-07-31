## Unit 8 - Recurrence Relation & Generating function

- A recurrence relation is an equation that defines a sequence recursively, that is, each term of the sequence is expressed as a function of the preceding terms.
- A generating function is a formal power series that encodes the information of a sequence in its coefficients.
- Recurrence relations and generating functions are useful tools for analyzing and solving many problems in discrete mathematics, such as counting, combinatorics, recurrence, and algorithms.

### Examples of recurrence relations

- The Fibonacci sequence is defined by the recurrence relation F(n) = F(n-1) + F(n-2), with initial conditions F(0) = 0 and F(1) = 1.
- The factorial function is defined by the recurrence relation n! = n * (n-1)!, with initial condition 0! = 1.
- The binomial coefficients are defined by the recurrence relation C(n,k) = C(n-1,k-1) + C(n-1,k), with initial conditions C(n,0) = C(n,n) = 1.

### Examples of generating functions

- The generating function of the Fibonacci sequence is F(x) = x / (1 - x - x^2), which can be obtained by multiplying both sides of the recurrence relation by x^n and summing over n.
- The generating function of the factorial function is F(x) = e^x, which can be obtained by using the Taylor series expansion of e^x.
- The generating function of the binomial coefficients is F(x) = (1 + x)^n, which can be obtained by using the binomial theorem.