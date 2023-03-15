# Truth tables for the notes of the Unit 4 - Propositional Logic in the subject of Discrete Structures & Theory of Logic

- A truth table is a mathematical table used in logic that shows the truth values of logical expressions for each possible combination of values of their variables.
- A truth table can be used to show the semantics of logical operators, prove logical equivalences, solve satisfiability problems, and more.
- A truth table has one column for each variable and one column for the logical expression. Each row corresponds to a possible assignment of truth values to the variables. The truth value of the expression is calculated for each row and written in the last column.
- The number of rows in a truth table is equal to 2^n, where n is the number of variables. For example, if there are two variables p and q, then the truth table has 2^2 = 4 rows.
- The order of the rows in a truth table is usually determined by the binary representation of the row number, starting from 0. For example, the first row has the binary representation 00, which means that both p and q are false. The second row has the binary representation 01, which means that p is false and q is true, and so on.
- The order of the columns in a truth table is usually determined by the order of appearance of the variables and operators in the logical expression. For example, if the expression is p ∧ q → ¬r, then the columns are p, q, r, p ∧ q, and p ∧ q → ¬r.
- The truth values of the logical operators are defined by the following rules:

  - Negation (¬): ¬p is true if and only if p is false.
  - Conjunction (∧): p ∧ q is true if and only if both p and q are true.
  - Disjunction (∨): p ∨ q is true if and only if at least one of p or q is true.
  - Implication (→): p → q is true if and only if p is false or q is true.
  - Equivalence (↔): p ↔ q is true if and only if p and q have the same truth value.

- Here is an example of a truth table for the expression p ∧ q → ¬r:

| p | q | r | p ∧ q | p ∧ q → ¬r |
|---|---|---|-------|------------|
| F | F | F | F     | T          |
| F | F | T | F     | T          |
| F | T | F | F     | T          |
| F | T | T | F     | T          |
| T | F | F | F     | T          |
| T | F | T | F     | T          |
| T | T | F | T     | T          |
| T | T | T | T     | F          |

: Truth table - Wikipedia
: Truth Tables - Propositional Logic | CodeGuage
: Propositional Logic Truth Table - Boolean Algebra - DYclassroom
: Truth Table Generator - Stanford University
: Propositional Logic | Brilliant Math & Science Wiki