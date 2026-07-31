# Inference Theory of Predicate Logic

- Predicate logic, also known as first-order logic or quantified logic, is a formal language in which propositions are expressed in terms of predicates, variables and quantifiers.
- Predicates are functions that take one or more arguments and return a truth value. For example, P(x) means "x is prime".
- Variables are symbols that can represent any object in the domain of discourse. For example, x, y, z, etc.
- Quantifiers are operators that specify the scope of a variable. For example, ∀x means "for all x" and ∃x means "there exists x".
- Inference theory of predicate logic is a set of rules that allow us to derive valid conclusions from quantified statements .
- There are four main rules of inference for predicate logic :
  - Universal specification (US): From ∀x P(x), one can conclude P(y) for any y in the domain.
  - Universal generalization (UG): From P(y) for any y in the domain, one can conclude ∀x P(x).
  - Existential specification (ES): From ∃x P(x), one can conclude P(y) for some y in the domain.
  - Existential generalization (EG): From P(y) for some y in the domain, one can conclude ∃x P(x).
- These rules can be used to construct valid arguments in predicate logic. For example, given the premises:
  - ∀x (P(x) → Q(x))
  - ∃x P(x)
  - We can use US to infer P(a) for some a in the domain.
  - We can use modus ponens (a rule of propositional logic) to infer Q(a) from P(a) and ∀x (P(x) → Q(x)).
  - We can use EG to infer ∃x Q(x) from Q(a).
  - Therefore, the conclusion ∃x Q(x) follows from the premises by the rules of inference.