### Definition and elementary properties of Rings and Fields

A **ring** is a set R with two binary operations, usually called **addition** and **multiplication**, that satisfy the following properties  :

- (R, +) is an **abelian group**, meaning that:
  - **Closure**: For all a, b in R, a + b is also in R.
  - **Associativity**: For all a, b, c in R, (a + b) + c = a + (b + c).
  - **Identity**: There exists an element 0 in R such that for all a in R, a + 0 = 0 + a = a.
  - **Inverse**: For every a in R, there exists an element -a in R such that a + (-a) = (-a) + a = 0.
  - **Commutativity**: For all a, b in R, a + b = b + a.
- (R, *) is a **semigroup**, meaning that:
  - **Closure**: For all a, b in R, a * b is also in R.
  - **Associativity**: For all a, b, c in R, (a * b) * c = a * (b * c).
- **Distributivity**: For all a, b, c in R, a * (b + c) = (a * b) + (a * c) and (a + b) * c = (a * c) + (b * c).

Some examples of rings are:

- The set of integers Z with the usual addition and multiplication.
- The set of polynomials with coefficients in a ring R, denoted by R[x], with the usual addition and multiplication of polynomials.
- The set of 2x2 matrices with entries in a ring R, denoted by M_2(R), with the usual matrix addition and multiplication.

A ring is called **commutative** if its multiplication is also commutative, that is, for all a, b in R, a * b = b * a. A ring is called **unital** or **unitary** if it has a **multiplicative identity**, that is, there exists an element 1 in R such that for all a in R, a * 1 = 1 * a = a. A ring is called an **integral domain** if it is commutative, unital, and has no **zero divisors**, that is, for all a, b in R, if a * b = 0, then either a = 0 or b = 0.

A **field** is a ring that is commutative, unital, and has **multiplicative inverses**, meaning that for every nonzero a in R, there exists an element a^-1 in R such that a * a^-1 = a^-1 * a = 1. In other words, a field is a ring where every nonzero element is a **unit**   .

Some examples of fields are:

- The set of rational numbers Q with the usual addition and multiplication.
- The set of real numbers R with the usual addition and multiplication.
- The set of complex numbers C with the usual addition and multiplication.
- The set of integers modulo a prime p, denoted by Z_p, with the addition and multiplication defined by the remainder after dividing by p.