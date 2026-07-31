### First-Order Logic

- First-order logic (FOL) is a formal language for representing and reasoning about the properties and relations of objects and events in the world.
- FOL consists of symbols for constants, variables, predicates, functions, logical connectives, quantifiers, and parentheses.
- Constants represent specific objects or individuals, such as John, Mary, 2, or red.
- Variables range over a domain of possible objects or individuals, such as x, y, z, or n.
- Predicates represent properties or relations of objects or individuals, such as Animal(x), Larger(x, y), or Loves(x, y).
- Functions represent mappings from objects or individuals to other objects or individuals, such as Father(x), SquareRoot(x), or Add(x, y).
- Logical connectives represent the logical operations of negation, conjunction, disjunction, implication, and equivalence, such as ¬, ∧, ∨, →, and ↔.
- Quantifiers represent the scope of variables over a domain, such as ∀ (for all) and ∃ (there exists).
- Parentheses are used to group symbols and indicate the order of evaluation, such as (x ∧ y) ∨ z.

- A term is either a constant, a variable, or a function applied to one or more terms, such as x, 2, Father(John), or Add(x, y).
- An atomic formula is a predicate applied to one or more terms, such as Animal(x), Larger(2, x), or Loves(Father(John), Mary).
- A formula is either an atomic formula, a negated formula, a formula connected to another formula by a logical connective, or a quantified formula, such as Animal(x), ¬Larger(2, x), (Animal(x) ∧ Larger(2, x)), ∀x(Animal(x) → Larger(2, x)), or ∃x(Loves(Father(John), x)).
- A sentence is a formula that contains no free variables, such as ∀x(Animal(x) → Larger(2, x)) or ∃x(Loves(Father(John), x)).

- The syntax of FOL defines the rules for forming well-formed formulas (wffs) from the symbols of the language.
- The semantics of FOL defines the rules for assigning truth values to formulas based on a model of the domain and an interpretation of the symbols.
- A model of a domain is a set of objects or individuals that constitute the domain, and a set of relations and functions that hold among them.
- An interpretation of the symbols is a mapping from constants to objects, from variables to objects or sets of objects, from predicates to relations, and from functions to functions.
- A formula is true in a model and an interpretation if it corresponds to a fact that holds in the model according to the interpretation, and false otherwise.
- A sentence is true in a model if it is true in every interpretation of the symbols in that model, and false otherwise.
- A sentence is valid if it is true in every model, and unsatisfiable if it is false in every model.
- A sentence is satisfiable if it is true in some model, and contingent if it is true in some model and false in some other model.
- A sentence α entails a sentence β if β is true in every model in which α is true, and α is logically equivalent to β if α and β are true in the same models.

- FOL is a powerful and expressive language for natural language processing (NLP) because it can capture many aspects of natural language semantics, such as quantification, negation, implication, and equivalence.
- FOL can also be used as an intermediate representation for natural language understanding and generation, where natural language sentences are parsed into FOL formulas, and FOL formulas are verbalized into natural language sentences.
- FOL can also be used as a basis for automated reasoning, where FOL sentences are given to an automated theorem prover or a satisfiability solver to infer new sentences or check the consistency of a knowledge base.