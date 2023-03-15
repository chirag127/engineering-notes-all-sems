## Unit 8 - Recurrence Relation & Generating Function

A recurrence relation is an equation that defines a sequence of numbers in terms of previous terms. For example, the Fibonacci sequence is defined by the recurrence relation F_n = F_n-1 + F_n-2, with initial values F_0 = 0 and F_1 = 1.

A generating function is a function that encodes the terms of a sequence as coefficients of a power series. For example, the generating function for the Fibonacci sequence is G(x) = x/(1-x-x^2), which can be verified by expanding the series and comparing the coefficients with the Fibonacci numbers.

Generating functions are useful for solving recurrence relations, because they allow us to manipulate the series algebraically and find a closed-form expression for the nth term. Some of the techniques that can be used are:

- Polynomial multiplication: If a sequence is defined by a linear combination of previous terms, we can multiply the generating function by a polynomial to eliminate the recurrence. For example, if a_n = 2a_n-1 + 3a_n-2, we can multiply G(x) by (1-2x-3x^2) and equate the coefficients to zero to find a closed-form expression for G(x).
- Partial fractions: If a generating function is a rational function, we can decompose it into simpler fractions using partial fraction decomposition. This can help us find a closed-form expression for the nth term by using the binomial theorem or other identities. For example, if G(x) = x/(1-x-x^2), we can write it as G(x) = 1/(1-phi*x) - 1/(1-psi*x), where phi and psi are the roots of 1-x-x^2. Then we can use the binomial theorem to find a closed-form expression for the nth term as a_n = phi^n - psi^n.
- Derivatives: If a sequence is defined by a summation of previous terms, we can use the derivative of the generating function to eliminate the summation. For example, if a_n = sum_{i=0}^n b_i, we can differentiate G(x) and use the relation G'(x) = sum_{n=0}^infty n*a_n*x^n-1 to find a closed-form expression for G(x) and a_n.