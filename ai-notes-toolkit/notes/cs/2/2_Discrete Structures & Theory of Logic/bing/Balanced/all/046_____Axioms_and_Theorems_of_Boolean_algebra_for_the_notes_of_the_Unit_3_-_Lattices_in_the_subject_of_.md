# Axioms and Theorems of Boolean Algebra

Boolean algebra is a branch of mathematics that deals with the manipulation of logical expressions and variables. It is used to design and analyze digital circuits and systems, such as logic gates, flip-flops, multiplexers, etc.

Boolean algebra is based on a set of axioms and theorems that define the properties and rules of the three basic logic operations: AND, OR and NOT. An axiom is a statement that is accepted as true without proof, and a theorem is a statement that can be derived from the axioms using logical reasoning.

The following are some of the most common axioms and theorems of Boolean algebra:

## Axioms of Boolean Algebra

- Axiom 1: Identity
  - A + 0 = A
  - A * 1 = A
- Axiom 2: Complement
  - A + A' = 1
  - A * A' = 0
- Axiom 3: Commutativity
  - A + B = B + A
  - A * B = B * A
- Axiom 4: Associativity
  - (A + B) + C = A + (B + C)
  - (A * B) * C = A * (B * C)
- Axiom 5: Distributivity
  - A * (B + C) = (A * B) + (A * C)
  - A + (B * C) = (A + B) * (A + C)

## Theorems of Boolean Algebra

- Theorem 1: Idempotence
  - A + A = A
  - A * A = A
- Theorem 2: Null
  - A + 1 = 1
  - A * 0 = 0
- Theorem 3: Involution
  - (A')' = A
- Theorem 4: De Morgan's Laws
  - (A + B)' = A' * B'
  - (A * B)' = A' + B'
- Theorem 5: Absorption
  - A + (A * B) = A
  - A * (A + B) = A
- Theorem 6: Consensus
  - A * B + A' * C + B * C = A * B + A' * C