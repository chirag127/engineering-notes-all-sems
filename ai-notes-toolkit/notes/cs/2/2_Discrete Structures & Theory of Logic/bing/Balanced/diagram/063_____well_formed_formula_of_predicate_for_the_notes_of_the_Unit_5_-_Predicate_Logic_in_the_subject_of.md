### Well Formed Formula of Predicate Logic

- A well formed formula (WFF) of predicate logic is a string of symbols that can be interpreted as a meaningful expression in predicate logic .
- A WFF can be either a **closed formula** or an **open formula**.
  - A closed formula (also called a sentence or a proposition) is a WFF that does not contain any free variables. It can be evaluated as true or false in a given interpretation.
  - An open formula (also called a sentential or propositional function) is a WFF that contains at least one free variable. It cannot be evaluated as true or false by itself, but only when the free variables are assigned some values.
- The rules for constructing WFFs of predicate logic are as follows :
  - Any predicate letter followed by any constant or variable is a WFF. For example: Pq, Qx, Rxy.
  - The result of prefixing any WFF with ‘~’ (negation) is a WFF. For example: ~Pq, ~Qx, ~Rxy.
  - The result of joining any two WFFs with ‘•’ (conjunction), ‘∨’ (disjunction), ‘⊃’ (implication), or ‘≡’ (equivalence) and enclosing the result in parentheses is a WFF. For example: (Pq • Qx), (Qx ∨ Rxy), (Rxy ⊃ Pq), (Pq ≡ Qx).
  - The result of prefixing any WFF with ‘∀’ (universal quantifier) or ‘∃’ (existential quantifier) and a variable is a WFF. For example: ∀x Pq, ∃y Qx, ∀x (Qx ⊃ Rxy), ∃y (Rxy • Pq).
  - Nothing else is a WFF.