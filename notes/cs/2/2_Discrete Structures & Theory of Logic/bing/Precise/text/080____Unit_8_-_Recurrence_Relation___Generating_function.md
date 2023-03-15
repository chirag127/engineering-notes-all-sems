## Unit 8 - Recurrence Relation & Generating function

A **recurrence relation** is an equation that describes a sequence of values in terms of their previous values. For example, the Fibonacci sequence is defined by the recurrence relation `F(n) = F(n-1) + F(n-2)` with initial conditions `F(0) = 0` and `F(1) = 1`.

A **generating function** is a formal power series that encodes the information of a sequence. For example, the generating function for the Fibonacci sequence is `F(x) = x/(1-x-x^2)`.

Generating functions can be used to solve recurrence relations by manipulating the power series to find a closed-form expression for the sequence.

Some common techniques for solving recurrence relations using generating functions include:
1. Multiplying both sides of the recurrence relation by `x^n` and summing over all `n` to obtain an equation in terms of the generating function.
2. Using partial fraction decomposition to split the generating function into simpler terms.
3. Using the binomial theorem to expand terms in the generating function.

These techniques can be applied to a wide range of recurrence relations to find closed-form solutions for the corresponding sequences. It is important to note that not all recurrence relations have closed-form solutions, and in some cases, numerical methods may be necessary to approximate the values of the sequence.