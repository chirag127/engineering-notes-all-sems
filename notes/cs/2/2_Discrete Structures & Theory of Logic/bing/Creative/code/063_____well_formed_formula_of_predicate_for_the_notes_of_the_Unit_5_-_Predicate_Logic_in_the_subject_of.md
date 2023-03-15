Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn or discuss. You have asked me to write the content on the topic of well formed formula of predicate for the notes of the Unit 5 - Predicate Logic in the subject of Discrete Structures & Theory of Logic. Here is the content I have written in markdown format:

### Well formed formula of predicate

- A well formed formula (wff) of predicate is a string of symbols that follows the rules of syntax of predicate logic.
- A wff of predicate can be either an atomic formula or a complex formula.
- An atomic formula is a wff that consists of a predicate symbol followed by a sequence of terms, where each term is either a constant symbol, a variable symbol, or a function symbol applied to a sequence of terms.
- A complex formula is a wff that is formed by applying logical connectives and quantifiers to other wffs.
- The logical connectives are: negation (~), conjunction (∧), disjunction (∨), implication (→), and equivalence (↔).
- The quantifiers are: universal (∀) and existential (∃).
- The rules of syntax for forming wffs of predicate are:

  - If P is a predicate symbol of arity n, and t1, t2, ..., tn are terms, then P(t1, t2, ..., tn) is a wff. This is an atomic formula.
  - If α is a wff, then ~α is a wff. This is a complex formula.
  - If α and β are wffs, then (α ∧ β), (α ∨ β), (α → β), and (α ↔ β) are wffs. These are complex formulas.
  - If α is a wff, and x is a variable symbol, then (∀x)α and (∃x)α are wffs. These are complex formulas.
  - Nothing else is a wff.

- Examples of wffs of predicate are:

  - P(a, b, c) (an atomic formula)
  - ~Q(x, f(x)) (a complex formula)
  - (P(a, b, c) ∧ Q(x, f(x))) → R(g(a), h(b, c)) (a complex formula)
  - (∀x)(P(x) → Q(x)) (a complex formula)
  - (∃y)(~P(y) ∧ R(g(y), h(a, b))) (a complex formula)

- Examples of strings that are not wffs of predicate are:

  - P(a, b) (not a wff because P is a predicate symbol of arity 3, not 2)
  - Q(x, f) (not a wff because f is a function symbol, not a term)
  - P(a, b, c) ∧ Q(x, f(x)) (not a wff because it is missing parentheses)
  - (∀x)P(x) → Q(x) (not a wff because the scope of the quantifier is ambiguous)
  - (∃x)(P(x) ∧ (∀y)Q(y)) (not a wff because the variable x is free in the subformula (∀y)Q(y))