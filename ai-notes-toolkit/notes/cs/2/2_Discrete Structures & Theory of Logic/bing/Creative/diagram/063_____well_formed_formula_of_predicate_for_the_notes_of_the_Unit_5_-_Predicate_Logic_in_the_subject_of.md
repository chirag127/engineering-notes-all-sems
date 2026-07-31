### Well Formed Formula of Predicate Logic

- A well formed formula (WFF) of predicate logic is a string of symbols that can be interpreted as a meaningful expression in predicate logic.
- A WFF can be either a **closed formula** or an **open formula**.
- A closed formula (also called a **sentence** or a **proposition**) is a WFF that does not contain any free variables. It can be evaluated as true or false in a given interpretation.
- An open formula (also called a **sentential function** or a **propositional function**) is a WFF that contains at least one free variable. It cannot be evaluated as true or false by itself, but only when the free variables are assigned values from a domain.
- The rules for constructing WFFs of predicate logic are as follows :
  - Any predicate letter followed by any constant or variable is a WFF. For example: `Pq`, `Qx`, `Rab`.
  - The result of prefixing any WFF with `~` (negation) is a WFF. For example: `~Pq`, `~(Qx ∨ Ry)`.
  - The result of joining any two WFFs with `•` (conjunction), `∨` (disjunction), `⊃` (implication), or `≡` (equivalence) and enclosing the result in parentheses is a WFF. For example: `(Pq • Qx)`, `(Qx ⊃ Ry)`, `(Pq ≡ ~Qx)`.
  - The result of prefixing any WFF with `∀` (universal quantifier) or `∃` (existential quantifier) and a variable is a WFF. For example: `∀x Pq`, `∃y Qx`, `∀x (Qx ⊃ Ry)`.
  - Nothing else is a WFF of predicate logic.

- Here are some examples of WFFs and non-WFFs of predicate logic:
  - `Pq` is a WFF. It is an open formula with `q` as a free variable.
  - `~(Pq ∨ Qx)` is a WFF. It is an open formula with `q` and `x` as free variables.
  - `∀x (Qx ⊃ Ry)` is a WFF. It is a closed formula, since the only variable `x` is bound by the universal quantifier.
  - `∀x Pq ∨ Qx` is not a WFF. It violates the rule of enclosing the result of joining two WFFs with a connective in parentheses.
  - `P` is not a WFF. It violates the rule of having a predicate letter followed by a constant or a variable.
  - `P(x)` is not a WFF. It violates the rule of using parentheses only for enclosing the result of joining two WFFs with a connective.