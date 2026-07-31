### Truth tables for the notes of the Unit 4 - Propositional Logic in the subject of Discrete Structures & Theory of Logic

- A truth table is a mathematical table used in logic that shows the truth values of logical expressions for each possible combination of values taken by their logical variables.
- A truth table can be used to solve various problems in propositional logic, such as showing the semantics of logical operators, proving equivalences, solving satisfiability problems, etc.
- A truth table has one column for each logical variable and one column for the logical expression. Each row corresponds to a possible assignment of truth values to the variables. The truth value of the expression is calculated for each row using the rules of propositional logic.
- The following table shows the basic logical operators and their truth tables:

| Operator | Symbol | Example | Truth table |
|:--------:|:------:|:-------:|:-----------:|
| Negation | ¬, ~, ! | ¬p | p | ¬p |
| | | | T | F |
| | | | F | T |
| Conjunction | ∧, &, and | p ∧ q | p | q | p ∧ q |
| | | | T | T | T |
| | | | T | F | F |
| | | | F | T | F |
| | | | F | F | F |
| Disjunction | ∨, \, or | p ∨ q | p | q | p ∨ q |
| | | | T | T | T |
| | | | T | F | T |
| | | | F | T | T |
| | | | F | F | F |
| Conditional | →, =>, implies | p → q | p | q | p → q |
| | | | T | T | T |
| | | | T | F | F |
| | | | F | T | T |
| | | | F | F | T |
| Biconditional | ↔, <=>, iff | p ↔ q | p | q | p ↔ q |
| | | | T | T | T |
| | | | T | F | F |
| | | | F | T | F |
| | | | F | F | T |
| Exclusive or | ⊕, ^, xor | p ⊕ q | p | q | p ⊕ q |
| | | | T | T | F |
| | | | T | F | T |
| | | | F | T | T |
| | | | F | F | F |

- To construct a truth table for a complex expression, we can use the following steps:
  - Identify all the logical variables and operators in the expression.
  - Write a column for each variable and operator, and a column for the expression itself.
  - Write the possible truth values for the variables in the first rows, using T for true and F for false.
  - Calculate the truth values for each operator and the expression, following the order of precedence and the rules of logic.
  - Fill in the truth values in the corresponding columns.
- For example, to construct a truth table for the expression (p ∧ q) → (p ∨ q), we can use the following steps:
  - Identify the variables and operators: p, q, ∧, ∨, →.
  - Write a column for each variable and operator, and a column for the expression: p | q | ∧ | ∨ | → | (p ∧ q) → (p ∨ q).
  - Write the possible truth values for the variables: p | q | ∧ | ∨ | → | (p ∧ q) → (p ∨ q) T | T | | | | T | F | | | | F | T | | | | F | F | | | |
  - Calculate the truth values for each operator and the expression: p | q | ∧ | ∨ | → | (p ∧ q) → (p ∨ q) T | T | T | T | T | T T | F | F | T | T | T F | T | F | T | T | T F | F | F | F | T | T
  - Fill in the truth values in the corresponding columns: p | q | ∧ | ∨ | → | (p ∧ q) → (p ∨ q) T | T | T | T | T | T T | F | F | T |