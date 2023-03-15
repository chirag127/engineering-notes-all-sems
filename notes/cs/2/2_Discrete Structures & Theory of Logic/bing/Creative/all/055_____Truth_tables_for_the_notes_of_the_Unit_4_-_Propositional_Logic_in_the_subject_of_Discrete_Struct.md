# Truth tables for the notes of the Unit 4 - Propositional Logic in the subject of Discrete Structures & Theory of Logic

- A truth table is a mathematical table used in logic that shows the truth values of logical expressions for each possible combination of values taken by their logical variables.
- A truth table can be used to solve various problems in propositional logic, such as showing the semantics of logical operators, proving equivalences, solving satisfiability problems, etc.
- A truth table has one column for each logical variable and one column for the logical expression. The rows of the table correspond to all possible assignments of truth values to the variables. The truth value of the expression for each row is calculated using the rules of propositional logic.
- The following table shows the basic logical operators and their truth tables:

| Operator | Symbol | Example | Truth table |
|:--------:|:------:|:-------:|:-----------:|
| Negation | ¬, ~, ! | ¬p | p | ¬p |
| | | | T | F |
| | | | F | T |
| Conjunction | ∧, /\\, & | p ∧ q | p | q | p ∧ q |
| | | | T | T | T |
| | | | T | F | F |
| | | | F | T | F |
| | | | F | F | F |
| Disjunction | ∨, \\/, \| | p ∨ q | p | q | p ∨ q |
| | | | T | T | T |
| | | | T | F | T |
| | | | F | T | T |
| | | | F | F | F |
| Implication | →, ->, => | p → q | p | q | p → q |
| | | | T | T | T |
| | | | T | F | F |
| | | | F | T | T |
| | | | F | F | T |
| Equivalence | ↔, <->, <=> | p ↔ q | p | q | p ↔ q |
| | | | T | T | T |
| | | | T | F | F |
| | | | F | T | F |
| | | | F | F | T |

- To construct a truth table for a complex expression, we can use the following steps:
  - Identify all the logical variables and operators in the expression and assign a column for each of them.
  - Write down all possible combinations of truth values for the variables in the rows of the table. A common method is to use binary counting, starting from all F's and ending with all T's.
  - Fill in the truth values for the operators, starting from the innermost parentheses and working outwards. Use the rules of propositional logic to calculate the truth values for each row.
  - The final column of the table will show the truth values of the whole expression.

- For example, to construct a truth table for the expression (p ∧ q) → (p ∨ q), we can follow these steps:

| Step | Expression | Truth table |
|:----:|:----------:|:-----------:|
| 1 | (p ∧ q) → (p ∨ q) | p | q | (p ∧ q) | (p ∨ q) | (p ∧ q) → (p ∨ q) |
| 2 | (p ∧ q) → (p ∨ q) | p | q | (p ∧ q) | (p ∨ q) | (p ∧ q) → (p ∨ q) |
| | | F | F | | | |
| | | F | T | | | |
| | | T | F | | | |
| | | T | T | | | |
| 3 | (p ∧ q) → (p ∨ q) | p | q | (p ∧ q) | (p ∨ q) | (p ∧ q) → (p ∨ q) |
| | | F | F | F | F | |
| | | F | T | F | T | |
| | | T | F | F | T | |
| | | T | T | T | T | |
| 4 | (p ∧ q) → (p ∨ q) | p | q | (p ∧ q) | (p ∨ q) | (p ∧ q) → (p