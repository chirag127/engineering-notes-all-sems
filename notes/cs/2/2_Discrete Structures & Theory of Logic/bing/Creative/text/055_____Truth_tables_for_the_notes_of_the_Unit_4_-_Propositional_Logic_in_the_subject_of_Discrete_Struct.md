### Truth tables for the notes of the Unit 4 - Propositional Logic in the subject of Discrete Structures & Theory of Logic

- A truth table is a mathematical table used in logic that shows the truth values of logical expressions for each possible combination of values of their variables.
- A truth table can be used to show the semantics of logical operators, prove logical equivalences, solve satisfiability problems, and other applications in propositional logic.
- A truth table has one column for each variable and one column for the logical expression. The rows of the table correspond to all possible assignments of truth values to the variables. The truth value of the expression is calculated for each row and written in the last column.
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
| Disjunction | ∨, \|\|, or | p ∨ q | p | q | p ∨ q |
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
  - Identify all the variables and operators in the expression and assign a column for each of them.
  - Write all possible combinations of truth values for the variables in the rows of the table. A common method is to use binary counting, starting from all F's and ending with all T's.
  - Fill in the columns for the operators by applying the corresponding truth tables to the values of the variables or subexpressions. Start from the innermost parentheses and work outwards.
  - The last column will contain the truth values of the whole expression.
- For example, to construct a truth table for the expression (p ∧ q) → (p ∨ q), we can follow these steps:

| Step | Expression | Column |
|:----:|:----------:|:------:|
| 1 | (p ∧ q) → (p ∨ q) | p | q | p ∧ q | p ∨ q | (p ∧ q) → (p ∨ q) |
| 2 | (p ∧ q) → (p ∨ q) | p | q | p ∧ q | p ∨ q | (p ∧ q) → (p ∨ q) |
| | | F | F | | | |
| | | F | T | | | |
| | | T | F | | | |
| | | T | T | | | |
| 3 | (p ∧ q) → (p ∨ q) | p | q | p ∧ q | p ∨ q | (p ∧ q) → (p ∨ q) |
| | | F | F | F | F | |
| | | F | T | F | T | |
| | | T | F | F | T | |
| | | T | T | T | T | |
| 4