# Inference Theory of Predicate Logic

- Predicate logic, also known as first-order logic or quantified logic, is a formal language in which propositions are expressed in terms of predicates, variables and quantifiers.
- Predicates are functions that take one or more arguments and return a truth value. For example, P(x) means "x is prime".
- Variables are symbols that can represent any object in the domain of discourse. For example, x, y, z, etc.
- Quantifiers are operators that specify how many objects in the domain satisfy a predicate. For example, (x) means "for all x" and (x) means "there exists an x".
- To reach a conclusion on quantified statements, there are four rules of inference which are collectively called as Inference Theory of the Predicate Calculus . They are:

  - **Universal Specification (US)**: From (x) P(x), one can conclude P(y) for any y in the domain. For example, from (x) (x is even -> x + 1 is odd), one can conclude 2 is even -> 2 + 1 is odd.
  - **Universal Generalization (UG)**: If P(y) is true for any y in the domain, then (x) P(x) is true. For example, if x + 1 is odd for any even x, then (x) (x is even -> x + 1 is odd) is true.
  - **Existential Specification (ES)**: From (x) P(x), one can conclude P(c) for some constant c in the domain. For example, from (x) (x is odd -> x - 1 is even), one can conclude 3 is odd -> 3 - 1 is even.
  - **Existential Generalization (EG)**: If P(c) is true for some constant c in the domain, then (x) P(x) is true. For example, if 3 is odd -> 3 - 1 is even, then (x) (x is odd -> x - 1 is even) is true.

- These rules of inference can be used to construct valid arguments in predicate logic. For example, given the premises:

  - (x) (x is a bird -> x can fly)
  - Tweety is a bird

  One can use US to infer:

  - Tweety can fly

  This is a valid argument, since the conclusion follows from the premises by the rules of inference.

- However, not all arguments in predicate logic are valid. For example, given the premises:

  - (x) (x is a bird -> x can fly)
  - Tweety can fly

  One cannot use EG to infer:

  - Tweety is a bird

  This is an invalid argument, since the conclusion does not follow from the premises by the rules of inference. This is an example of a fallacy of affirming the consequent.