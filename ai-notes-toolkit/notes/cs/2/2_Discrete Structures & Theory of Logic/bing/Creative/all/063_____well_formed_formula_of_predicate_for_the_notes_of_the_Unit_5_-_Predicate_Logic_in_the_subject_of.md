# Well Formed Formula of Predicate Logic

- A well formed formula (WFF) of predicate logic is a string of symbols that can be interpreted as a meaningful expression in predicate logic.
- A WFF can be either a **closed formula** or an **open formula**.
- A closed formula (also called a **sentence** or a **proposition**) is a WFF that does not contain any free variables. It can be evaluated as true or false in a given interpretation.
- An open formula (also called a **sentential function** or a **propositional function**) is a WFF that contains at least one free variable. It cannot be evaluated as true or false by itself, but only when the free variables are assigned values from a domain.
- The rules for constructing WFFs of predicate logic are as follows :
  - Any predicate letter followed by any constant or variable is a WFF. For example: `Pq`, `Qx`, `Rab`.
  - The result of prefixing any WFF with `~` (negation) is a WFF. For example: `~Pq`, `~(Qx ∨ Ry)`.
  - The result of joining any two WFFs with `•` (conjunction), `∨` (disjunction), `⊃` (implication), or `≡` (equivalence) and enclosing the result in parentheses is a WFF. For example: `(Pq • Qx)`, `(Qx ⊃ Ry)`, `(Pq ≡ ~Qx)`.
  - The result of prefixing any WFF with `∀x` (universal quantification) or `∃x` (existential quantification), where `x` is any variable, is a WFF. For example: `∀xPx`, `∃yQy`, `∀x(Qx ⊃ ∃yRxy)`.
  - Nothing else is a WFF. For example: `P`, `QxRy`, `∀Pq`, `(Pq ∨)`.
- The order of precedence of the logical operators is as follows: `~`, `∀`, `∃`, `•`, `∨`, `⊃`, `≡`. Parentheses can be used to override the order of precedence. For example: `~∀xPx` means `~(∀xPx)`, not `(~∀x)Px`.
- The scope of a quantifier is the part of the WFF that it affects. The scope of a quantifier is the WFF that immediately follows it, unless parentheses indicate otherwise. For example: in `∀x(Px ∨ Qx)`, the scope of `∀x` is `(Px ∨ Qx)`; in `∀xPx ∨ Qx`, the scope of `∀x` is `Px`.
- A variable is **bound** in a WFF if it occurs within the scope of a quantifier that uses the same variable. A variable is **free** in a WFF if it is not bound. For example: in `∀xPx ∨ Qx`, `x` is bound and `y` is free; in `Px ∨ Qy`, both `x` and `y` are free.
- A WFF is **valid** if it is true in every possible interpretation. A WFF is **satisfiable** if it is true in at least one possible interpretation. A WFF is **unsatisfiable** if it is false in every possible interpretation. For example: `∀xPx ⊃ ∃xPx` is valid; `∀xPx ∨ ∃x~Px` is satisfiable but not valid; `∀xPx • ∃x~Px` is unsatisfiable.