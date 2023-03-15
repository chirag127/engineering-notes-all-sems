# Algebraic manipulation of Boolean expressions

- Boolean expressions are algebraic expressions that involve variables and operators that take only two values: true (1) or false (0).
- Boolean expressions can be used to represent logic circuits, truth tables, and sets.
- Boolean expressions can be manipulated using the laws, rules, and theorems of Boolean algebra, which is a branch of mathematics that deals with the properties and operations of binary logic.
- Some of the basic laws and rules of Boolean algebra are:

  - Commutative laws: A + B = B + A and A * B = B * A
  - Associative laws: (A + B) + C = A + (B + C) and (A * B) * C = A * (B * C)
  - Distributive laws: A * (B + C) = (A * B) + (A * C) and A + (B * C) = (A + B) * (A + C)
  - Identity laws: A + 0 = A and A * 1 = A
  - Complement laws: A + A' = 1 and A * A' = 0
  - Idempotent laws: A + A = A and A * A = A
  - Involution law: (A')' = A
  - De Morgan's laws: (A + B)' = A' * B' and (A * B)' = A' + B'
  - Absorption laws: A + (A * B) = A and A * (A + B) = A
  - Consensus law: (A + B) * (A' + C) * (B + C) = (A + B) * (A' + C)

- Algebraic manipulation of Boolean expressions is the process of transforming one expression into another equivalent expression by applying the laws and rules of Boolean algebra.
- Algebraic manipulation can be used to simplify, standardize, or optimize Boolean expressions for various purposes, such as minimizing the number of literals, terms, or gates in a logic circuit, or converting an expression into a canonical form, such as sum-of-products (SOP) or product-of-sums (POS).
- An example of algebraic manipulation is:

  - Given the expression: F = A * B + A' * C + B * C
  - Simplify it using Boolean algebra.
  - Solution:

    - F = A * B + A' * C + B * C
    - Apply the distributive law: F = A * B + (A' + B) * C
    - Apply the consensus law: F = A * B + A' * C
    - The expression is simplified.