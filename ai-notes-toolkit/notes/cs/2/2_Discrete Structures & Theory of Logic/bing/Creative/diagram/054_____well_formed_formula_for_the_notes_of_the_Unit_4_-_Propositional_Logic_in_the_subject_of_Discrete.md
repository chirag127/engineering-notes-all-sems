Hello, I am Sydney, your AI assistant. I can help you with your study material for Discrete Structures & Theory of Logic. Here is the content for well formed formula for the notes of Unit 4 - Propositional Logic.

### Well formed formula

- A well formed formula (wff) is a finite sequence of symbols from a given alphabet that is grammatically correct according to some rules of syntax.
- The alphabet for propositional logic consists of the following symbols:
  - Propositional variables: p, q, r, ...
  - Logical connectives: ¬ (negation), ∧ (conjunction), ∨ (disjunction), → (implication), ↔ (equivalence)
  - Parentheses: (, )
- The rules of syntax for propositional logic are as follows:
  - Every propositional variable is a wff.
  - If α is a wff, then ¬α is a wff.
  - If α and β are wffs, then (α ∧ β), (α ∨ β), (α → β), and (α ↔ β) are wffs.
  - Nothing else is a wff.
- Examples of wffs are:
  - p
  - ¬q
  - (p ∧ q)
  - (¬p ∨ q)
  - ((p → q) ↔ (¬q → ¬p))
- Examples of non-wffs are:
  - p ∧ q (missing parentheses)
  - ¬(p ∨ q) ∧ (missing right parenthesis)
  - p → (missing right operand)
  - ¬¬p (double negation is not allowed)