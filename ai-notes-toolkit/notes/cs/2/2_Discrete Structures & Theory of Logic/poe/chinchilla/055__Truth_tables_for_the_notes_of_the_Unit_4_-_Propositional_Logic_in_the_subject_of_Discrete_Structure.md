### Truth tables for the notes of the Unit 4 - Propositional Logic in the subject of Discrete Structures & Theory of Logic

Truth tables are an essential tool in propositional logic that allows us to determine the truth value of complex logical expressions. In this unit, we will learn how to construct truth tables for various logical connectives and how to use them to evaluate logical expressions.

Here are some key points to keep in mind when working with truth tables:

- A truth table is a table that lists all possible combinations of truth values for the propositional variables in a logical expression and the resulting truth value of the expression.

- The number of rows in a truth table is determined by the number of propositional variables in the expression. If we have n propositional variables, then we will have 2^n rows in the truth table.

- The columns in a truth table represent the propositional variables and the logical connectives used in the expression. Each column corresponds to a unique combination of truth values for the propositional variables.

- The truth values in the last column of the truth table represent the truth value of the entire logical expression for each combination of truth values for the propositional variables.

- To construct a truth table, we start by listing the propositional variables in the first column and then add additional columns for each logical connective used in the expression.

- We then fill in the remaining columns of the truth table by applying the truth table rules for each logical connective. The truth table rules specify the truth value of the expression for each combination of truth values for the propositional variables.

- Once the truth table is complete, we can use it to evaluate the truth value of any logical expression. To do this, we simply find the row in the truth table that corresponds to the truth values of the propositional variables in the expression and read off the truth value of the expression from the last column of the table.

Here are some examples of how to construct truth tables for some common logical connectives:

- Conjunction (AND): The truth value of a conjunction is true if and only if both of its operands are true. The truth table for conjunction is as follows:

| P | Q | P AND Q |
|---|---|--------|
| T | T | T      |
| T | F | F      |
| F | T | F      |
| F | F | F      |

- Disjunction (OR): The truth value of a disjunction is true if at least one of its operands is true. The truth table for disjunction is as follows:

| P | Q | P OR Q |
|---|---|-------|
| T | T | T     |
| T | F | T     |
| F | T | T     |
| F | F | F     |

- Negation (NOT): The truth value of a negation is the opposite of the truth value of its operand. The truth table for negation is as follows:

| P | NOT P |
|---|-------|
| T | F     |
| F | T     |

- Conditional (IF-THEN): The truth value of a conditional is false only when its antecedent (the "if" part) is true and its consequent (the "then" part) is false. The truth table for conditional is as follows:

| P | Q | P -> Q |
|---|---|--------|
| T | T | T      |
| T | F | F      |
| F | T | T      |
| F | F | T      |

- Biconditional (IF AND ONLY IF): The truth value of a biconditional is true if and only if both operands have the same truth value. The truth table for biconditional is as follows:

| P | Q | P <-> Q |
|---|---|---------|
| T | T | T       |
| T | F | F       |
| F | T | F       |
| F | F | T       |

By understanding how truth tables work and how to construct them, we can better understand the logical structure of complex expressions and evaluate them more accurately.