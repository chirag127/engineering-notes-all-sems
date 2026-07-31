# First-Order Logic

- First-order logic (FOL) is a formal language for representing and reasoning about the properties and relations of objects and events in the world.
- FOL is widely used in natural language processing (NLP) to capture the meaning and inference of natural language sentences.
- FOL has a simple syntax that consists of symbols for constants, variables, predicates, functions, logical connectives, and quantifiers.
- FOL has a well-defined semantics that assigns truth values to sentences based on a model of the domain of discourse.
- FOL can express many aspects of natural language semantics, such as quantification, negation, implication, and equality, but it cannot express some phenomena, such as modality, tense, and intensionality.

## Syntax of FOL

- The basic elements of FOL are terms and formulas.
- A term is an expression that denotes an object in the domain of discourse. A term can be a constant symbol, a variable symbol, or a function symbol applied to one or more terms.
- A formula is an expression that denotes a truth value. A formula can be an atomic formula, a negated formula, a conjunction, a disjunction, an implication, an equivalence, a universal quantification, or an existential quantification.
- An atomic formula is a predicate symbol applied to one or more terms. A predicate symbol denotes a property or a relation of objects in the domain of discourse.
- A negated formula is a formula prefixed by the negation symbol (:). It denotes the opposite truth value of the original formula.
- A conjunction is a formula composed of two formulas joined by the conjunction symbol (^). It denotes the truth value of the logical and of the two formulas.
- A disjunction is a formula composed of two formulas joined by the disjunction symbol (_). It denotes the truth value of the logical or of the two formulas.
- An implication is a formula composed of two formulas joined by the implication symbol (!). It denotes the truth value of the logical if-then of the two formulas.
- An equivalence is a formula composed of two formulas joined by the equivalence symbol (\u0011). It denotes the truth value of the logical if-and-only-if of the two formulas.
- A universal quantification is a formula prefixed by the universal quantifier symbol (8) and a variable symbol. It denotes the truth value of the logical for-all of the formula with respect to the variable.
- An existential quantification is a formula prefixed by the existential quantifier symbol (9) and a variable symbol. It denotes the truth value of the logical there-exists of the formula with respect to the variable.

## Semantics of FOL

- The semantics of FOL defines how to assign truth values to formulas based on a model of the domain of discourse.
- A model of the domain of discourse consists of a set of objects (the domain), a function that assigns an object to each constant symbol (the interpretation), and a function that assigns a set of tuples of objects to each predicate symbol and a function from tuples of objects to objects to each function symbol (the extension).
- The truth value of a formula is determined by the following rules:
  - An atomic formula is true if and only if the tuple of objects denoted by the terms in the formula belongs to the extension of the predicate symbol in the formula.
  - A negated formula is true if and only if the original formula is false.
  - A conjunction is true if and only if both formulas in the conjunction are true.
  - A disjunction is true if and only if at least one formula in the disjunction is true.
  - An implication is true if and only if the first formula in the implication is false or the second formula in the implication is true.
  - An equivalence is true if and only if both formulas in the equivalence have the same truth value.
  - A universal quantification is true if and only if the formula with respect to the variable is true for every object in the domain.
  - An existential quantification is true if and only if the formula with respect to the variable is true for some object in the domain.