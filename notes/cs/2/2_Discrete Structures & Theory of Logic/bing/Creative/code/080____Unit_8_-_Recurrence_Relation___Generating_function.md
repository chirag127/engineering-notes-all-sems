## Unit 8 - Recurrence Relation & Generating function

A recurrence relation is an equation that defines a sequence recursively: each term of the sequence is defined as a function of the preceding terms.

A generating function is a formal power series that encodes the information of a sequence of numbers.

Some applications of recurrence relations and generating functions are:

- Solving combinatorial problems, such as counting the number of ways to arrange objects or to partition a set.
- Analyzing the complexity of algorithms, such as divide-and-conquer or dynamic programming.
- Modeling the behavior of systems, such as population growth or recurrence networks.

Some examples of recurrence relations and generating functions are:

- The Fibonacci sequence: F(n) = F(n-1) + F(n-2), F(0) = 0, F(1) = 1. The generating function for this sequence is G(x) = x/(1-x-x^2).
- The factorial function: n! = n * (n-1)!, 0! = 1. The generating function for this sequence is G(x) = e^x.
- The binomial coefficients: C(n,k) = C(n-1,k-1) + C(n-1,k), C(n,0) = C(n,n) = 1. The generating function for this sequence is G(x) = (1+x)^n.