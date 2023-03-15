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
- These rules of inference can be used to construct valid arguments in predicate logic. For example, given the premises (x)Human(x) -> Mortal(x) and Human(Socrates), we can use US to derive Human(Socrates) -> Mortal(Socrates), and then use modus ponens to derive Mortal(Socrates).
- Inference theory of predicate logic is also useful for proving the validity or invalidity of arguments in predicate logic. For example, to prove that the argument (x)P(x) -> Q(x), (Ex)P(x) |- (Ex)Q(x) is valid, we can use the following steps:
  - Assume the premises (x)P(x) -> Q(x) and (Ex)P(x).
  - Use ES to derive P(c) for some constant c.
  - Use US to derive P(c) -> Q(c).
  - Use modus ponens to derive Q(c).
  - Use EG to derive (Ex)Q(x).
  - Therefore, the conclusion (Ex)Q(x) follows from the premises by the rules of inference.
- Inference theory of predicate logic is based on the assumption that the domain of discourse is non-empty, meaning that there is at least one object in the domain. If the domain is empty, then some of the rules of inference may not hold. For example, if the domain is empty, then (x)P(x) is vacuously true for any predicate P, but P(y) may not be true for any y. Therefore, US may not be valid in an empty domain. Similarly, if the domain is empty, then (Ex)P(x) is vacuously false for any predicate P, but P(c) may be true for some constant c. Therefore, EG may not be valid in an empty domain. To avoid these problems, we usually assume that the domain is non-empty when using inference theory of predicate logic.