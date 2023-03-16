### First-Order Logic

- First-order logic (FOL) is a formal language for representing and reasoning about the properties and relations of objects and events in the world.
- FOL consists of symbols for constants, variables, predicates, functions, logical connectives, quantifiers, and parentheses.
- Constants represent specific objects or individuals, such as `John`, `Mary`, `2`, or `red`.
- Variables range over a domain of possible objects or individuals, such as `x`, `y`, or `z`.
- Predicates represent properties or relations of objects or individuals, such as `Animal(x)`, `Color(x, red)`, or `Loves(x, y)`.
- Functions represent mappings from objects or individuals to other objects or individuals, such as `Father(x)`, `Age(x)`, or `Plus(x, y)`.
- Logical connectives represent the truth-functional operations of negation (`¬`), conjunction (`∧`), disjunction (`∨`), implication (`→`), and equivalence (`↔`).
- Quantifiers represent the scope of variables over a domain of possible objects or individuals, such as universal quantifier (`∀`) and existential quantifier (`∃`).
- Parentheses are used to group symbols and indicate the order of evaluation.

- A term is either a constant, a variable, or a function applied to one or more terms, such as `x`, `2`, `Father(John)`, or `Plus(x, y)`.
- An atomic formula is a predicate applied to one or more terms, such as `Animal(x)`, `Color(red, x)`, or `Loves(John, Mary)`.
- A formula is either an atomic formula, a negated formula, a formula connected to another formula by a logical connective, or a quantified formula, such as `¬Animal(x)`, `Animal(x) ∧ Color(x, red)`, `∀x (Animal(x) → Color(x, red))`, or `∃x (Loves(x, John))`.
- A sentence is a formula that contains no free variables, that is, all variables are bound by quantifiers, such as `∀x (Animal(x) → Color(x, red))` or `∃x ∃y (Loves(x, y))`.

- The semantics of FOL defines how to assign truth values to sentences based on a model, which consists of a domain of possible objects or individuals, and an interpretation, which assigns meanings to constants, predicates, and functions.
- A model satisfies a sentence if the sentence is true under the model, and falsifies a sentence if the sentence is false under the model.
- A sentence is valid if it is satisfied by every model, and unsatisfiable if it is falsified by every model.
- A sentence is satisfiable if it is satisfied by some model, and contingent if it is satisfied by some model and falsified by some other model.
- A sentence entails another sentence if every model that satisfies the first sentence also satisfies the second sentence, and is entailed by another sentence if every model that satisfies the second sentence also satisfies the first sentence.
- A set of sentences is consistent if there is a model that satisfies all of them, and inconsistent if there is no such model.

- FOL can be used to represent and reason about natural language semantics, by mapping natural language expressions to FOL symbols and structures, and applying logical inference rules to derive new sentences from existing ones.
- FOL can capture many aspects of natural language semantics, such as quantification, negation, implication, and equivalence, but not all of them, such as modality, tense, aspect, and intensionality.