# Inference Theory of Predicate Logic

- Predicate logic is a formal language in which propositions are expressed in terms of predicates, variables and quantifiers.
- Inference is the process of deriving new statements from given statements using logical rules.
- Inference theory of predicate logic is a set of rules that allow us to infer valid conclusions from quantified statements .
- There are four main rules of inference for predicate logic :
  - Universal Specification (US): From ∀x P(x), one can conclude P(y) for any specific y.
  - Universal Generalization (UG): From P(y) for any specific y, one can conclude ∀x P(x), provided that y does not occur in any premise or assumption.
  - Existential Specification (ES): From ∃x P(x), one can conclude P(y) for some specific y, provided that y is a new variable that does not occur in any premise or assumption.
  - Existential Generalization (EG): From P(y) for some specific y, one can conclude ∃x P(x), provided that y does not occur in any premise or assumption.
- These rules can be used to construct proofs of validity for arguments involving quantifiers.
- For example, consider the following argument:

Premise 1: ∀x (P(x) → Q(x))
Premise 2: ∃x P(x)
Conclusion: ∃x Q(x)

- To prove the validity of this argument, we can use the following steps:

Step 1: ∃x P(x) (Premise 2)
Step 2: P(a) (ES, Step 1)
Step 3: ∀x (P(x) → Q(x)) (Premise 1)
Step 4: P(a) → Q(a) (US, Step 3)
Step 5: Q(a) (Modus Ponens, Step 2 and Step 4)
Step 6: ∃x Q(x) (EG, Step 5)

- Therefore, the argument is valid by the inference theory of predicate logic.