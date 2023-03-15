### Inference theory of predicate logic

- Predicate logic is a formal language in which propositions are expressed in terms of predicates, variables and quantifiers.
- Inference theory of predicate logic is a set of rules that allow us to derive valid conclusions from quantified statements .
- There are four main rules of inference for predicate logic :
  - Universal specification (US): From `(x) P(x)`, one can conclude `P(y)` for any specific `y`.
  - Universal generalization (UG): From `P(y)` for any specific `y`, one can conclude `(x) P(x)`.
  - Existential specification (ES): From `(∃x) P(x)`, one can conclude `P(y)` for some specific `y`.
  - Existential generalization (EG): From `P(y)` for some specific `y`, one can conclude `(∃x) P(x)`.
- These rules are based on the principle of substitution, which states that if two terms have the same meaning, they can be replaced by each other without changing the truth value of a statement.
- These rules can be used to construct proofs of validity for arguments involving quantifiers, predicates and logical connectives.
- An example of a proof using these rules is:

  - Premise 1: `(x) (P(x) → Q(x))`
  - Premise 2: `(∃x) P(x)`
  - Conclusion: `(∃x) Q(x)`
  - Proof:
    - By ES, from premise 2, we can conclude `P(a)` for some specific `a`.
    - By US, from premise 1, we can conclude `P(a) → Q(a)`.
    - By modus ponens, from `P(a)` and `P(a) → Q(a)`, we can conclude `Q(a)`.
    - By EG, from `Q(a)`, we can conclude `(∃x) Q(x)`.
    - Therefore, the conclusion follows from the premises by the rules of inference.