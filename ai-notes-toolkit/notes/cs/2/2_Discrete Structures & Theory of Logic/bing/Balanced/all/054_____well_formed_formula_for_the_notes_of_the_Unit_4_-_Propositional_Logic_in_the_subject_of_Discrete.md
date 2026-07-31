Hello, I am Sydney, your AI assistant. I can help you with your study material for Discrete Structures & Theory of Logic. Here is the content for well formed formula for the notes of Unit 4 - Propositional Logic.

# Well Formed Formula

- A well formed formula (WFF) is a string of symbols that follows the rules of syntax of propositional logic.
- A WFF can be either an atomic formula or a compound formula.
- An atomic formula is a single propositional variable (such as p, q, r, ...) or a constant (such as T for true or F for false).
- A compound formula is formed by applying logical connectives (such as ¬ for negation, ∧ for conjunction, ∨ for disjunction, → for implication, ↔ for equivalence) to one or more WFFs.
- The rules of syntax for WFFs are:

  - Any atomic formula is a WFF.
  - If α is a WFF, then ¬α is a WFF.
  - If α and β are WFFs, then (α ∧ β), (α ∨ β), (α → β), and (α ↔ β) are WFFs.
  - Nothing else is a WFF.

- Examples of WFFs are:

  - p
  - ¬q
  - (p ∧ q)
  - (¬p ∨ q)
  - (p → (q ↔ r))

- Examples of strings that are not WFFs are:

  - p ∧
  - ¬(p q)
  - (p →) ∨ q
  - p ↔ ¬
  - (p ∧ (q ∨ r)