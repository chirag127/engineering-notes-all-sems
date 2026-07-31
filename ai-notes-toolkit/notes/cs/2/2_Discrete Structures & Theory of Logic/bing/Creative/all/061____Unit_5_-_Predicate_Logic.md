## Unit 5 - Predicate Logic

Predicate logic is a branch of logic that deals with predicates, quantifiers, and variables. Predicate logic is more expressive than propositional logic, as it can capture the structure and meaning of natural language sentences more accurately.

### Predicate Logic Syntax

The syntax of predicate logic consists of the following elements:

- **Predicates**: Predicates are symbols that represent properties or relations of objects. For example, `P(x)` means that object `x` has property `P`, and `Q(x,y)` means that objects `x` and `y` are related by relation `Q`.
- **Constants**: Constants are symbols that represent specific objects in the domain of discourse. For example, `a`, `b`, and `c` can be constants that denote Alice, Bob, and Charlie, respectively.
- **Variables**: Variables are symbols that can stand for any object in the domain of discourse. For example, `x`, `y`, and `z` can be variables that range over all possible objects.
- **Quantifiers**: Quantifiers are symbols that indicate how many objects satisfy a given predicate. There are two main types of quantifiers: universal (`∀`) and existential (`∃`). For example, `∀x P(x)` means that all objects have property `P`, and `∃x Q(x,a)` means that there exists some object that is related to `a` by relation `Q`.
- **Connectives**: Connectives are symbols that combine predicates or quantified formulas into more complex formulas. The connectives of predicate logic are the same as those of propositional logic: negation (`¬`), conjunction (`∧`), disjunction (`∨`), implication (`→`), and equivalence (`↔`).
- **Parentheses**: Parentheses are symbols that group formulas together and indicate the scope of quantifiers and connectives. For example, `(∀x P(x)) → Q(a)` means that if all objects have property `P`, then `a` has property `Q`.

### Predicate Logic Semantics

The semantics of predicate logic defines how to assign truth values to predicate logic formulas based on a given interpretation. An interpretation consists of the following components:

- **Domain**: The domain is the set of all possible objects that the constants, variables, and predicates refer to. For example, the domain can be the set of all people, or the set of all natural numbers, or the set of all animals, etc.
- **Assignment**: The assignment is a function that maps each constant to a specific object in the domain, and each variable to an arbitrary object in the domain. For example, the assignment can map `a` to Alice, `b` to Bob, `c` to Charlie, `x` to Alice, `y` to Bob, and `z` to Charlie.
- **Interpretation**: The interpretation is a function that maps each predicate to a set of tuples of objects in the domain that satisfy the predicate. For example, the interpretation can map `P` to the set of all people who are happy, and `Q` to the set of all pairs of people who are friends.

The truth value of a predicate logic formula is determined by the following rules:

- A predicate formula `P(t1,...,tn)` is true if and only if the tuple of objects denoted by the terms `t1,...,tn` belongs to the set mapped by the predicate `P` in the interpretation. A term can be either a constant or a variable. For example, `P(a)` is true if and only if Alice is happy, and `Q(x,y)` is true if and only if `x` and `y` are friends.
- A negated formula `¬φ` is true if and only if `φ` is false.
- A conjunctive formula `φ ∧ ψ` is true if and only if both `φ` and `ψ` are true.
- A disjunctive formula `φ ∨ ψ` is true if and only if either `φ` or `ψ` is true.
- An implication formula `φ → ψ` is true if and only if either `φ` is false or `ψ` is true.
- An equivalence formula `φ ↔ ψ` is true if and only if `φ` and `ψ` have the same truth value.
- A universally quantified formula `∀x φ` is true if and only if `φ` is true for every possible value of `x` in the domain. For example, `∀x P(x)` is true if and only if everyone is happy.
- An existentially quantified formula `∃x φ`