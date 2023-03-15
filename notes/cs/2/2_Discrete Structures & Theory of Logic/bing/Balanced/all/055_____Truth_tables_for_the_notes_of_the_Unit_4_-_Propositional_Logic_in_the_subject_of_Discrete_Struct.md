# Truth tables for the notes of the Unit 4 - Propositional Logic in the subject of Discrete Structures & Theory of Logic

- A truth table is a tabular representation of the truth values of a propositional formula for all possible combinations of truth values of its variables.
- A propositional formula is a combination of propositional variables and logical connectives, such as negation (¬), conjunction (∧), disjunction (∨), implication (→), and equivalence (↔).
- A propositional variable is a symbol that can take either true (T) or false (F) as its value.
- A logical connective is a symbol that combines two or more propositional variables to form a new propositional formula.
- The truth value of a propositional formula depends on the truth values of its variables and the logical connectives used.
- A truth table has one column for each propositional variable and one column for the propositional formula. Each row of the table corresponds to a possible assignment of truth values to the variables. The last column shows the truth value of the formula for that assignment.
- The number of rows in a truth table is equal to 2^n, where n is the number of propositional variables in the formula.
- The order of the rows in a truth table is usually determined by the binary representation of the row number, starting from 0. For example, if there are three variables p, q, and r, the order of the rows is:

| Row | p | q | r | Binary |
| --- | --- | --- | --- | --- |
| 0 | F | F | F | 000 |
| 1 | F | F | T | 001 |
| 2 | F | T | F | 010 |
| 3 | F | T | T | 011 |
| 4 | T | F | F | 100 |
| 5 | T | F | T | 101 |
| 6 | T | T | F | 110 |
| 7 | T | T | T | 111 |

- The truth values of the logical connectives are defined by the following rules:

| p | q | ¬p | p ∧ q | p ∨ q | p → q | p ↔ q |
| --- | --- | --- | --- | --- | --- | --- |
| F | F | T | F | F | T | T |
| F | T | T | F | T | T | F |
| T | F | F | F | T | F | F |
| T | T | F | T | T | T | T |

- ¬p is true if and only if p is false.
- p ∧ q is true if and only if both p and q are true.
- p ∨ q is true if and only if at least one of p or q is true.
- p → q is true if and only if p is false or q is true.
- p ↔ q is true if and only if p and q have the same truth value.

- To construct a truth table for a propositional formula, follow these steps:

  - Identify all the propositional variables and logical connectives in the formula.
  - Create a column for each variable and a column for the formula.
  - Fill in the rows with the possible truth values of the variables, following the binary order.
  - Fill in the last column with the truth values of the formula, applying the rules of the logical connectives from left to right and using parentheses to indicate the order of operations.
  - For example, to construct a truth table for the formula (p ∧ q) → (p ∨ r), follow these steps:

    - Identify the variables and connectives: p, q, r, ∧, ∨, →.
    - Create the columns: p, q, r, (p ∧ q) → (p ∨ r).
    - Fill in the rows with the truth values of the variables:

| p | q | r | (p ∧ q) → (p ∨ r) |
| --- | --- | --- | --- |
| F | F | F |  |
| F | F | T |  |
| F | T | F |  |
| F | T | T |  |
| T | F | F |  |
| T | F | T |  |
| T | T | F |  |
| T | T | T |  |

    - Fill in the last column with the truth values of the formula, applying the rules of the logical connectives:

| p | q | r | (p ∧ q) → (p ∨ r) |
| --- | --- | --- |