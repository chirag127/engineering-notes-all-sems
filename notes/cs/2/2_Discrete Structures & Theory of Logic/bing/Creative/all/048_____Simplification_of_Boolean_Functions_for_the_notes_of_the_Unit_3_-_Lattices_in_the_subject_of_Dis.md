# Simplification of Boolean Functions

- A boolean function is a function that takes one or more boolean variables as inputs and produces a single boolean output.
- The output of a boolean function depends on the logical operations performed on the inputs, such as AND, OR, NOT, etc.
- The algebraic expression of a boolean function can be written using boolean variables, constants (0 or 1), and operators (+, ., ', etc.).
- The process of simplifying the algebraic expression of a boolean function is called minimization.
- Minimization is important since it reduces the cost and complexity of the associated circuit .
- For example, the function F = A.B + A.B + B.C can be minimized to F = A + B.C using the theorems of boolean algebra.
- There are different methods for minimizing boolean functions, such as algebraic method, Karnaugh map method, Quine-McCluskey method, etc.
- In this unit, we will focus on the algebraic method of minimization, which uses the following boolean identities:

  - Identity law: A + 0 = A, A . 1 = A
  - Idempotent law: A + A = A, A . A = A
  - Commutative law: A + B = B + A, A . B = B . A
  - Associative law: (A + B) + C = A + (B + C), (A . B) . C = A . (B . C)
  - Distributive law: A . (B + C) = A . B + A . C, A + (B . C) = (A + B) . (A + C)
  - Complement law: A + A' = 1, A . A' = 0
  - De Morgan's law: (A + B)' = A' . B', (A . B)' = A' + B'
  - Absorption law: A + A . B = A, A . (A + B) = A
  - Involution law: (A')' = A
  - Consensus law: A . B + A' . C + B . C = A . B + A' . C

- To simplify a boolean function using the algebraic method, we apply the above identities in a systematic way until we obtain the simplest expression possible.
- The order of applying the identities is not fixed, but we can follow some general guidelines, such as:

  - Eliminate the redundant terms or literals using the idempotent law, the complement law, or the absorption law.
  - Apply the distributive law to expand the expression and create more opportunities for simplification.
  - Apply the De Morgan's law to simplify the complements of sums or products.
  - Apply the consensus law to eliminate the common terms in a sum of products or a product of sums.
  - Apply the identity law, the commutative law, or the associative law to rearrange the terms or literals as needed.

- For example, to simplify the function F ( A, B, C) = A' . B + B . C' + B . C + A . B' . C', we can follow these steps:

  - Step 1: Eliminate the redundant term B . C' + B . C using the idempotent law: F = A' . B + B + A . B' . C'
  - Step 2: Apply the distributive law to expand the expression: F = A' . B + B . 1 + A . B' . C' = A' . B + B . (A + A') + A . B' . C'
  - Step 3: Apply the complement law to simplify the term A + A': F = A' . B + B . 1 + A . B' . C' = A' . B + B + A . B' . C'
  - Step 4: Apply the consensus law to eliminate the common term A' . B: F = A' . B + B + A . B' . C' = B + A . B' . C'
  - Step 5: Rearrange the terms using the commutative law: F = B + A . B' . C' = A . B' . C' + B

- The final expression F = A .