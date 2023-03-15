## Unit 5 - Predicate Logic

Predicate logic is a branch of logic that deals with predicates, quantifiers, and variables. Predicate logic is more expressive than propositional logic, as it can represent the structure and relations of objects and properties in a domain of discourse.

### 5.1 Predicates and Quantifiers

- A predicate is a sentence that contains a subject and a verb, and expresses a statement about the subject. For example, "x is red" is a predicate, where x is the subject and "is red" is the verb.
- A quantifier is a word or symbol that specifies how many or how much of something is being referred to. For example, "all", "some", "none", "there exists", and "for all" are quantifiers.
- A variable is a symbol that can stand for any object or value in a domain of discourse. For example, x, y, z, and n are variables.
- A predicate logic formula is a combination of predicates, quantifiers, variables, logical connectives, and parentheses. For example, ∀x (P(x) → Q(x)) is a predicate logic formula, where ∀ is the universal quantifier, P and Q are predicates, and x is a variable.

### 5.2 Interpretations and Models

- An interpretation of a predicate logic formula is a way of assigning meanings to the predicates, variables, and quantifiers in the formula. For example, an interpretation of ∀x (P(x) → Q(x)) could be: the domain of discourse is the set of natural numbers, P(x) means "x is even", Q(x) means "x is divisible by 4", and ∀ means "for all".
- A model of a predicate logic formula is an interpretation that makes the formula true. For example, the interpretation above is a model of ∀x (P(x) → Q(x)), since it is true that for all natural numbers x, if x is even, then x is divisible by 4.
- A predicate logic formula is valid if it is true in every interpretation, and satisfiable if it is true in at least one interpretation. For example, ∀x (P(x) → Q(x)) is valid if P(x) implies Q(x) for any possible meaning of P and Q, and satisfiable if there is at least one interpretation where P(x) implies Q(x).

### 5.3 Rules of Inference

- A rule of inference is a logical principle that allows us to derive a new formula from one or more existing formulas. For example, modus ponens is a rule of inference that says: if P and P → Q are true, then Q is true.
- A proof is a sequence of formulas, each of which is either an assumption or derived from previous formulas by a rule of inference. For example, a proof of Q from P and P → Q is:

1. P (assumption)
2. P → Q (assumption)
3. Q (modus ponens from 1 and 2)

- A formula is provable from a set of assumptions if there is a proof of the formula from the assumptions. For example, Q is provable from {P, P → Q}.
- A formula is a logical consequence of a set of formulas if it is true in every interpretation that makes the set of formulas true. For example, Q is a logical consequence of {P, P → Q}.
- A sound rule of inference is one that preserves logical consequence, i.e., if the premises are true, then the conclusion is true. For example, modus ponens is a sound rule of inference.
- A complete set of rules of inference is one that can prove any logical consequence from any set of formulas. For example, the following rules of inference are a complete set for predicate logic:

- Universal instantiation: from ∀x P(x), infer P(t), where t is any term
- Existential generalization: from P(t), infer ∃x P(x), where t is any term
- Universal generalization: from P(x), infer ∀x P(x), where x is not free in any assumption
- Existential instantiation: from ∃x P(x), infer P(c), where c is a new constant not occurring in any formula
- Modus ponens: from P and P → Q, infer Q
- Modus tollens: from ¬Q and P → Q, infer ¬P
- Hypothetical syllogism: from P → Q and Q → R, infer P → R
- Disjunctive syllogism: from P ∨ Q and ¬P, infer Q
- Addition: from P, infer P ∨ Q, where Q is