### Well Formed Formula of Predicate Logic

- A well formed formula (WFF) of predicate logic is a string of symbols that can be interpreted as a meaningful expression in predicate logic .
- A WFF can be either a **closed formula** or an **open formula**.
  - A closed formula (also called a sentence or a proposition) is a WFF that does not contain any free variables. It can be evaluated as true or false in a given interpretation. For example: ∀x(Px ∨ Qx)
  - An open formula (also called a sentential or propositional function) is a WFF that contains at least one free variable. It cannot be evaluated as true or false by itself, but only when the free variables are assigned values. For example: Px, ∃yQxy
- The rules for constructing WFFs of predicate logic are as follows :
  - Any predicate letter followed by any constant or variable is a WFF. For example: Pq, Qx
  - The result of prefixing any WFF with ‘~’ is a WFF. For example: ~Pq, ~∃yQxy
  - The result of joining any two WFFs with ‘•’, ‘∨’, ‘⊃’, or ‘≡’ and enclosing the result in parentheses is a WFF. For example: (Pq ∨ Qx), (Px ⊃ ~Qx)
  - The result of prefixing any WFF with a quantifier ‘∀’ or ‘∃’ and a variable is a WFF. For example: ∀xPx, ∃yQxy
  - Nothing else is a WFF. For example: P, Qxy, (Px ∨) are not WFFs.