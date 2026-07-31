# Axioms and Theorems of Boolean Algebra

Boolean algebra is a branch of mathematics that deals with the manipulation of logical expressions and variables. It is used to design and analyze digital circuits and systems. Boolean algebra is based on a set of axioms and theorems that define the properties and rules of logic operations.

## Axioms of Boolean Algebra

An axiom is a statement that is accepted as true without proof. It is also called a postulate. Axioms are used to define the basic logic operations of AND, OR and NOT. The following are the axioms of Boolean algebra:

- Commutative laws: These laws state that the order of operands does not affect the result of the logic operations.

  - A + B = B + A
  - A * B = B * A

- Associative laws: These laws state that the grouping of operands does not affect the result of the logic operations.

  - (A + B) + C = A + (B + C)
  - (A * B) * C = A * (B * C)

- Distributive laws: These laws state that the logic operations can be distributed over each other.

  - A * (B + C) = (A * B) + (A * C)
  - A + (B * C) = (A + B) * (A + C)

- Identity laws: These laws state that there are two special values, 0 and 1, that act as identities for the logic operations.

  - A + 0 = A
  - A * 1 = A

- Complement laws: These laws state that there is a unary operation, called complement or NOT, that reverses the value of a variable.

  - A + A' = 1
  - A * A' = 0

- Idempotent laws: These laws state that repeating a variable in a logic operation does not change the result.

  - A + A = A
  - A * A = A

- Absorption laws: These laws state that a variable can be absorbed by another variable in a logic operation.

  - A + (A * B) = A
  - A * (A + B) = A

- De Morgan's laws: These laws state that the complement of a logic operation is equal to the logic operation of the complements with the opposite operator.

  - (A + B)' = A' * B'
  - (A * B)' = A' + B'

## Theorems of Boolean Algebra

A theorem is a statement that can be derived or proved from the axioms or other theorems. Theorems are used to simplify and manipulate logic expressions and variables. The following are some of the theorems of Boolean algebra:

- Zero and one laws: These laws state that there are two special values, 0 and 1, that have unique effects on the logic operations.

  - A + 1 = 1
  - A * 0 = 0

- Involution law: This law states that the complement of a complement is equal to the original variable.

  - (A')' = A

- Redundancy laws: These laws state that some variables or terms can be eliminated from a logic expression without changing the result.

  - A + (A * B) = A
  - A * (A + B) = A

- Consensus law: This law states that a term can be removed from a logic expression if it is implied by another term.

  - A * B + A' * C + B * C = A * B + A' * C

- Adjacency law: This law states that two adjacent terms with the same variable can be combined into one term.

  - A * B + A * B' = A

- Simplification laws: These laws state that some logic expressions can be simplified by applying the axioms and theorems of Boolean algebra.

  - A + A * B = A
  - A * (A + B) = A

- Duality principle: This principle states that every axiom and theorem of Boolean algebra has a dual form that can be obtained by interchanging the operators and the identities.

  - A + B = B + A (dual of A * B = B * A)
  - A + 0 = A (dual of A * 1 = A)
  - A + A' = 1 (dual of A * A' = 0)