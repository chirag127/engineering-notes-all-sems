### First-Order Logic

- First-order logic (FOL) is a formal language for representing and reasoning about the properties and relations of objects and events in the world.
- FOL consists of symbols for constants, variables, predicates, functions, logical connectives, quantifiers, and parentheses.
- Constants represent specific objects or individuals, such as `John`, `Mary`, `2`, or `red`.
- Variables range over a domain of possible objects or individuals, such as `x`, `y`, or `z`.
- Predicates represent properties or relations of objects or individuals, such as `Animal(x)`, `Color(x, red)`, or `Loves(x, y)`.
- Functions represent mappings from objects or individuals to other objects or individuals, such as `Mother(x)`, `Age(x)`, or `Plus(x, y)`.
- Logical connectives represent the truth-functional operations of negation, conjunction, disjunction, implication, and equivalence, such as `¬`, `∧`, `∨`, `→`, and `↔`.
- Quantifiers represent the scope of variables over a domain of possible objects or individuals, such as `∀` (for all) and `∃` (there exists).
- Parentheses are used to group symbols and indicate the order of evaluation, such as `(Animal(x) ∧ Color(x, red))`.

- A term is either a constant or a variable, or a function applied to one or more terms, such as `x`, `2`, `Mother(John)`, or `Plus(x, y)`.
- An atomic formula is a predicate applied to one or more terms, such as `Animal(x)`, `Color(x, red)`, or `Loves(John, Mary)`.
- A formula is either an atomic formula, or a formula formed by applying a logical connective to one or more formulas, or a formula formed by applying a quantifier to a variable and a formula, such as `Animal(x)`, `¬Color(x, red)`, `(Animal(x) ∧ Color(x, red))`, `∀x (Animal(x) → Color(x, red))`, or `∃x (Animal(x) ∧ Loves(x, John))`.

- The syntax of FOL defines the rules for forming well-formed formulas (wffs) from the symbols of the language.
- The semantics of FOL defines the rules for assigning truth values to formulas with respect to a model, which consists of a domain of possible objects or individuals, and an interpretation, which assigns meanings to the constants, predicates, and functions of the language.
- The pragmatics of FOL defines the rules for using the language to communicate and reason about the world, such as how to translate natural language sentences to FOL, how to perform logical inference on FOL formulas, and how to evaluate the validity and soundness of arguments in FOL.