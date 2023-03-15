### Inference theory of predicate logic

- Predicate logic, also known as first-order logic or quantified logic, is a formal language in which propositions are expressed in terms of predicates, variables and quantifiers.
- Predicates are functions that take one or more arguments and return a truth value. For example, P(x) is a predicate that takes x as an argument and returns true or false.
- Variables are symbols that can represent any object in the domain of discourse. For example, x, y, z are variables that can stand for any person, animal, thing, etc.
- Quantifiers are operators that specify the scope or range of variables. There are two main types of quantifiers: universal and existential. For example, (x)P(x) is a universal quantifier that means "for all x, P(x) is true", and (Ex)P(x) is an existential quantifier that means "there exists some x such that P(x) is true".
- Inference theory of predicate logic is a set of rules that allow us to derive valid conclusions from quantified statements. There are four main rules of inference for predicate logic :
  - Universal specification (US): From (x)P(x), one can conclude P(y) for any y in the domain. For example, from (x)Human(x) -> Mortal(x), one can conclude Human(Socrates) -> Mortal(Socrates).
  - Universal generalization (UG): From P(y) for any y in the domain, one can conclude (x)P(x). For example, from Even(2) and Even(4), one can conclude (x)Even(x) -> x mod 2 = 0.
  - Existential specification (ES): From (Ex)P(x), one can conclude P(c) for some constant c in the domain. For example, from (Ex)Prime(x), one can conclude Prime(2) or Prime(3) or Prime(5), etc.
  - Existential generalization (EG): From P(c) for some constant c in the domain, one can conclude (Ex)P(x). For example, from Odd(3), one can conclude (Ex)Odd(x).

- These rules of inference can be used to construct valid arguments in predicate logic. For example, consider the following argument:

  Premise 1: (x)Human(x) -> Mortal(x)
  Premise 2: Human(Socrates)
  Conclusion: Mortal(Socrates)

  This argument is valid by applying the rule of US to premise 1 and then using modus ponens. Alternatively, one can use a proof tree to show the validity of the argument:

  ```
  (x)Human(x) -> Mortal(x)    Premise
  Human(Socrates)             Premise
  |---------------------------US
  Human(Socrates) -> Mortal(Socrates)
  |---------------------------MP
  Mortal(Socrates)            Conclusion
  ```