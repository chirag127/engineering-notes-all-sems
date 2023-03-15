### Inference theory of predicate logic

- Predicate logic, also known as first-order logic or quantified logic, is a formal language in which propositions are expressed in terms of predicates, variables and quantifiers.
- Predicates are functions that take one or more arguments and return a truth value. For example, P(x) is a predicate that takes x as an argument and returns true or false.
- Variables are symbols that can represent any object in the domain of discourse. For example, x, y, z are variables that can stand for any person, animal, thing, etc.
- Quantifiers are operators that specify the scope or range of the variables. There are two main types of quantifiers: universal and existential. For example, (x)P(x) is a universal quantifier that means "for all x, P(x) is true", and (x)P(x) is an existential quantifier that means "there exists some x such that P(x) is true".
- Inference theory of predicate logic is a set of rules that allow us to derive valid conclusions from quantified statements. There are four main rules of inference for predicate logic :
  - Universal specification (US): From (x)P(x), one can conclude P(y) for any specific y in the domain. For example, from (x)Human(x) -> Mortal(x), one can conclude Human(Socrates) -> Mortal(Socrates).
  - Universal generalization (UG): From P(y) for any specific y in the domain, one can conclude (x)P(x). For example, from Human(Socrates) -> Mortal(Socrates), one can conclude (x)Human(x) -> Mortal(x).
  - Existential specification (ES): From (x)P(x), one can conclude P(c) for some constant c in the domain. For example, from (x)Human(x) -> Mortal(x), one can conclude Human(c) -> Mortal(c) for some c.
  - Existential generalization (EG): From P(c) for some constant c in the domain, one can conclude (x)P(x). For example, from Human(c) -> Mortal(c) for some c, one can conclude (x)Human(x) -> Mortal(x).
- These rules of inference are sound and complete, meaning that they can derive all and only the valid conclusions from the premises. They can also be combined with the rules of inference for propositional logic, such as modus ponens, modus tollens, etc.