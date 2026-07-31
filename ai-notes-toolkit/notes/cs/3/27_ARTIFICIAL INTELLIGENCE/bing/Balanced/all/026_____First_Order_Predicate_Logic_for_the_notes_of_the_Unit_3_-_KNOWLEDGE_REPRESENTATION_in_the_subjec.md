# First Order Predicate Logic

- First order predicate logic (FOPL) is a formal language for representing and reasoning about the properties and relations of objects in a domain.
- FOPL extends propositional logic by allowing the use of variables, constants, predicates, functions, and quantifiers.
- Variables are symbols that can stand for any object in the domain, such as x, y, z, etc.
- Constants are symbols that stand for a specific object in the domain, such as Alice, Bob, 1, 2, etc.
- Predicates are symbols that represent properties or relations of objects, such as Happy, Loves, Larger, etc.
- Functions are symbols that map objects to other objects, such as Mother, Successor, etc.
- Quantifiers are symbols that express how many objects satisfy a given formula, such as ∀ (for all) and ∃ (there exists).

- A term is either a variable, a constant, or a function applied to one or more terms, such as x, Alice, Successor(1), Mother(Alice), etc.
- An atomic formula is a predicate applied to one or more terms, such as Happy(x), Loves(Alice, Bob), Larger(2, 1), etc.
- A formula is either an atomic formula, or a formula formed by applying logical connectives (such as ¬, ∧, ∨, →, ↔) or quantifiers to other formulas, such as ¬Happy(x), ∀x Happy(x), ∃x Loves(x, Alice), etc.

- The semantics of FOPL are defined by specifying a domain of discourse (a set of objects) and an interpretation (a mapping from symbols to objects, properties, and relations).
- A term is said to denote an object in the domain, and an atomic formula is said to be true or false in the domain, depending on the interpretation.
- A formula is said to be true or false in the domain, depending on the truth values of its subformulas and the logical rules for connectives and quantifiers.
- A formula is said to be valid if it is true in every domain and interpretation, and satisfiable if it is true in some domain and interpretation.
- A formula is said to be a logical consequence of a set of formulas if it is true in every domain and interpretation where the set of formulas is true.

- FOPL can be used to represent and reason about various kinds of knowledge, such as facts, rules, definitions, constraints, etc.
- FOPL can also be used to perform various kinds of inference, such as deduction, induction, abduction, etc.
- FOPL has some limitations, such as the inability to express higher-order concepts, modalities, uncertainty, vagueness, etc.