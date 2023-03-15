### Inference theory of predicate logic

- Predicate logic is a formal language in which propositions are expressed in terms of predicates, variables and quantifiers.
- Inference theory of predicate logic is a set of rules that allow us to derive valid conclusions from quantified statements .
- There are four main rules of inference in predicate logic :
  - Universal specification (US): From (x)P(x), one can conclude P(y) for any specific y.
  - Universal generalization (UG): From P(y) for any specific y, one can conclude (x)P(x).
  - Existential specification (ES): From (Ex)P(x), one can conclude P(y) for some specific y.
  - Existential generalization (EG): From P(y) for some specific y, one can conclude (Ex)P(x).
- These rules can be used to construct proofs of validity for arguments involving quantifiers and predicates.
- Here is an example of a proof using these rules:

| Step | Statement | Reason |
| --- | --- | --- |
| 1 | (x)(Fx -> Gx) | Premise |
| 2 | (Ex)Fx | Premise |
| 3 | Fa -> Ga | US from 1 |
| 4 | Fa | ES from 2 |
| 5 | Ga | Modus ponens from 3 and 4 |
| 6 | (Ex)Gx | EG from 5 |
| 7 | (Ex)Fx -> (Ex)Gx | Conditional proof from 2 to 6 |

- The proof shows that the argument is valid, i.e., the conclusion follows from the premises by the rules of logic.