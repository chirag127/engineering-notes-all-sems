## Unit 8 - Recurrence Relation & Generating function

- A **recurrence relation** is an equation that defines a sequence recursively: each term of the sequence is defined as a function of the preceding terms.
- A **generating function** is a formal power series that encodes the information of a sequence: the coefficient of x^n in the generating function is the n-th term of the sequence.
- Recurrence relations and generating functions are useful tools for analyzing and solving problems involving sequences, such as counting, combinatorics, recurrence, and algorithms.

### Examples of recurrence relations and generating functions

- The **Fibonacci sequence** is defined by the recurrence relation F_n = F_(n-1) + F_(n-2), with initial conditions F_0 = 0 and F_1 = 1. The generating function for the Fibonacci sequence is F(x) = x/(1-x-x^2).
- The **factorial sequence** is defined by the recurrence relation n! = n * (n-1)!, with initial condition 0! = 1. The generating function for the factorial sequence is F(x) = e^x / (1-x).
- The **binomial coefficients** are defined by the recurrence relation C(n,k) = C(n-1,k-1) + C(n-1,k), with initial conditions C(n,0) = C(n,n) = 1. The generating function for the binomial coefficients is F(x) = (1+x)^n.

### Methods for solving recurrence relations and finding generating functions

- To solve a recurrence relation, one can try to find a **closed-form expression** for the n-th term of the sequence, or a **general formula** that involves some parameters. Some common methods for finding closed-form expressions are:
  - **Guess and verify**: make an educated guess based on some patterns or observations, and then prove it by induction or substitution.
  - **Characteristic equation**: transform the recurrence relation into a polynomial equation, and then find its roots and use them to construct the solution.
  - **Generating function**: multiply both sides of the recurrence relation by x^n and sum over all n, and then manipulate the resulting equation to find the generating function, and then use partial fractions, Taylor series, or other techniques to find the coefficients.
- To find a generating function for a sequence, one can try to find a **pattern** or a **formula** for the coefficients, and then use some properties or operations of generating functions to construct the power series. Some common properties and operations of generating functions are:
  - **Linearity**: if F(x) and G(x) are generating functions for sequences a_n and b_n, respectively, then F(x) + G(x) is the generating function for a_n + b_n, and c * F(x) is the generating function for c * a_n, where c is a constant.
  - **Shift**: if F(x) is the generating function for a_n, then x * F(x) is the generating function for a_(n+1), and x^k * F(x) is the generating function for a_(n+k), where k is a positive integer.
  - **Differentiation**: if F(x) is the generating function for a_n, then F'(x) is the generating function for n * a_n, and F^(k)(x) is the generating function for n! / (n-k)! * a_n, where k is a non-negative integer.
  - **Multiplication**: if F(x) and G(x) are generating functions for sequences a_n and b_n, respectively, then F(x) * G(x) is the generating function for the **convolution** of a_n and b_n, which is defined as c_n = sum_(i=0)^n a_i * b_(n-i).
  - **Composition**: if F(x) and G(x) are generating functions for sequences a_n and b_n, respectively, then F(G(x)) is the generating function for the **composition** of a_n and b_n, which is defined as c_n = sum_(i=0)^n a_i * b_n^i.