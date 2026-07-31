## Unit 4 - Propositional Logic

- Propositional logic is a branch of logic that deals with propositions, which are statements that can be either true or false.
- Propositional logic uses symbols and connectives to represent propositions and their logical relations.
- The basic symbols of propositional logic are:
  - **Propositional variables**: lowercase letters (p, q, r, ...) that stand for arbitrary propositions.
  - **Logical constants**: uppercase letters (T, F) that stand for the truth values true and false.
  - **Logical connectives**: symbols that combine propositional variables or constants to form complex propositions. The main logical connectives are:
    - **Negation**: ¬p, which means "not p" or "it is not the case that p".
    - **Conjunction**: p ∧ q, which means "p and q" or "both p and q".
    - **Disjunction**: p ∨ q, which means "p or q" or "either p or q".
    - **Implication**: p → q, which means "p implies q" or "if p then q".
    - **Equivalence**: p ↔ q, which means "p is equivalent to q" or "p if and only if q".
- The meaning of a proposition is determined by its truth value, which is either true or false. The truth value of a proposition depends on the truth values of its components and the logical connectives that join them.
- A **truth table** is a table that shows the truth value of a proposition for every possible combination of truth values of its components. A truth table has one column for each component and one column for the proposition. Each row of the table corresponds to a possible assignment of truth values to the components. The truth value of the proposition in each row is calculated by applying the rules of the logical connectives.
- The rules of the logical connectives are:
  - ¬p is true if and only if p is false.
  - p ∧ q is true if and only if both p and q are true.
  - p ∨ q is true if and only if at least one of p and q is true.
  - p → q is true if and only if either p is false or q is true.
  - p ↔ q is true if and only if p and q have the same truth value.
- Here are some examples of truth tables:

| p | q | ¬p | p ∧ q | p ∨ q | p → q | p ↔ q |
|---|---|----|-------|-------|-------|-------|
| T | T | F  | T     | T     | T     | T     |
| T | F | F  | F     | T     | F     | F     |
| F | T | T  | F     | T     | T     | F     |
| F | F | T  | F     | F     | T     | T     |

- A proposition is **tautology** if it is always true, regardless of the truth values of its components. For example, p ∨ ¬p is a tautology, because it is true for both p = T and p = F.
- A proposition is **contradiction** if it is always false, regardless of the truth values of its components. For example, p ∧ ¬p is a contradiction, because it is false for both p = T and p = F.
- A proposition is **contingency** if it is neither a tautology nor a contradiction, meaning that it can be true or false depending on the truth values of its components. For example, p ∧ q is a contingency, because it is true for p = T and q = T, but false for any other combination of truth values.
- Two propositions are **logically equivalent** if they have the same truth value for every possible assignment of truth values to their components. For example, p → q and ¬p ∨ q are logically equivalent, because they have the same truth value in every row of their truth tables. Logical equivalence is denoted by ≡, so we can write p → q ≡ ¬p ∨ q.
- Two propositions are **logically consistent** if there is at least one assignment of truth values to their components that makes them both true. For example, p and q are logically consistent, because they are both true for p = T and q = T. Logical consistency is denoted by ⊨, so we can write p ⊨ q.
- Two propositions are **logically inconsistent** if there is no assignment of truth values to their components that makes them both true. For example, p and ¬p are