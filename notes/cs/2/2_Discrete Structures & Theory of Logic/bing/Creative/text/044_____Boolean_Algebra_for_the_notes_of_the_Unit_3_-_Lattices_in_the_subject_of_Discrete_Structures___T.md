### Boolean Algebra

- Boolean algebra is a branch of mathematics that deals with operations on logical values with binary variables  .
- The Boolean variables are represented as binary numbers to represent truths: 1 = true and 0 = false .
- The basic operations in Boolean algebra are the logical operations AND, OR and NOT .
- AND is denoted by ∧, OR by ∨ and NOT by ¬.
- AND returns 1 if both operands are 1, otherwise 0.
- OR returns 1 if either operand is 1, otherwise 0.
- NOT returns 1 if the operand is 0, and 0 if the operand is 1.
- For example, 1 ∧ 0 = 0, 1 ∨ 0 = 1, ¬1 = 0, ¬0 = 1.
- Boolean algebra can be used to manipulate and simplify logical expressions, such as those used in digital circuits .
- Boolean algebra can also be defined abstractly as any set with binary operations ∧ and ∨ and a unary operation ¬ satisfying the Boolean laws.
- The Boolean laws are a set of axioms and rules that govern the behavior of Boolean operations.
- Some of the Boolean laws are:

  - Commutative laws: A ∧ B = B ∧ A, A ∨ B = B ∨ A.
  - Associative laws: (A ∧ B) ∧ C = A ∧ (B ∧ C), (A ∨ B) ∨ C = A ∨ (B ∨ C).
  - Distributive laws: A ∧ (B ∨ C) = (A ∧ B) ∨ (A ∧ C), A ∨ (B ∧ C) = (A ∨ B) ∧ (A ∨ C).
  - Identity laws: A ∧ 1 = A, A ∨ 0 = A.
  - Complement laws: A ∧ ¬A = 0, A ∨ ¬A = 1.
  - Idempotent laws: A ∧ A = A, A ∨ A = A.
  - De Morgan's laws: ¬(A ∧ B) = ¬A ∨ ¬B, ¬(A ∨ B) = ¬A ∧ ¬B.
  - Absorption laws: A ∧ (A ∨ B) = A, A ∨ (A ∧ B) = A.
  - Involution law: ¬(¬A) = A.

- A Boolean function is a function that takes one or more Boolean variables as inputs and returns a Boolean value as output.
- A Boolean function can be represented in various ways, such as a truth table, an algebraic expression, a logic diagram or a Boolean circuit.
- A truth table is a table that lists all possible combinations of inputs and their corresponding outputs.
- An algebraic expression is a formula that uses Boolean variables and operations to describe the output.
- A logic diagram is a graphical representation that uses symbols for Boolean variables and operations to show the logic of the function.
- A Boolean circuit is a physical implementation of a logic diagram using electronic components such as switches, gates and wires.
- For example, the Boolean function F(A, B) = A ∧ ¬B can be represented as:

  - Truth table:

    | A | B | F(A, B) |
    |---|---|---------|
    | 0 | 0 | 0       |
    | 0 | 1 | 0       |
    | 1 | 0 | 1       |
    | 1 | 1 | 0       |

  - Algebraic expression: F(A, B) = A ∧ ¬B
  - Logic diagram:

    ![Logic diagram of F(A, B) = A ∧ ¬B](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/AND_NOT.svg/1200px-AND_NOT.svg.png)

  - Boolean circuit:

    ![Boolean circuit of F(A, B) = A ∧ ¬B](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/AND_NOT_c