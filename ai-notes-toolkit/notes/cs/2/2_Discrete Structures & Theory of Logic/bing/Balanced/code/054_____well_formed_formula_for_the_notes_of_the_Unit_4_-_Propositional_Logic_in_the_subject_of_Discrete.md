Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn or discuss. You have asked me to write the content on well formed formula for the notes of the Unit 4 - Propositional Logic in the subject of Discrete Structures & Theory of Logic. Here is the content in markdown format:

# Well Formed Formula

- A well formed formula (WFF) is a finite sequence of symbols from a given alphabet that is grammatically correct according to some rules of syntax.
- In propositional logic, the alphabet consists of the following symbols:
  - Propositional variables: p, q, r, ...
  - Logical connectives: ¬ (negation), ∧ (conjunction), ∨ (disjunction), → (implication), ↔ (equivalence)
  - Parentheses: (, )
- The rules of syntax for propositional logic are as follows:
  - Every propositional variable is a WFF.
  - If α is a WFF, then ¬α is a WFF.
  - If α and β are WFFs, then (α ∧ β), (α ∨ β), (α → β), and (α ↔ β) are WFFs.
  - Nothing else is a WFF.
- Examples of WFFs in propositional logic are:
  - p
  - ¬q
  - (p ∧ q)
  - (¬p ∨ q)
  - (p → (q ↔ r))
- Examples of non-WFFs in propositional logic are:
  - p ∧ q (missing parentheses)
  - ¬(p ∨ q) ∧ r (missing parentheses)
  - p → ¬ (missing right operand)
  - (p ↔ q) ↔ (missing right operand)
  - p ∧ ¬ ∧ q (extra connective)
  - (p ∨ q) ∨ r (extra parentheses)