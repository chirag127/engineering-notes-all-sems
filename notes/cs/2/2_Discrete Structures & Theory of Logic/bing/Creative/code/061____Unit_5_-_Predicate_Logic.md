## Unit 5 - Predicate Logic

Predicate logic is a branch of logic that deals with predicates, quantifiers, and variables. Predicate logic is more expressive than propositional logic, as it can capture the structure and meaning of natural language sentences more accurately.

### Predicate Logic Syntax

The syntax of predicate logic consists of the following elements:

- **Predicates**: Predicates are symbols that represent properties or relations of objects. For example, `P(x)` means that object `x` has property `P`, and `R(x,y)` means that objects `x` and `y` are related by relation `R`. Predicates can have any number of arguments, but each argument must be a term.
- **Terms**: Terms are symbols that represent objects or constants. For example, `a`, `b`, and `c` are terms that denote some specific objects, and `0`, `1`, and `2` are terms that denote numerical constants. Terms can also be formed by applying functions to other terms. For example, `f(x)` is a term that denotes the result of applying function `f` to term `x`.
- **Functions**: Functions are symbols that represent mappings from objects to objects. For example, `f(x)` means that object `x` is mapped to another object by function `f`. Functions can have any number of arguments, but each argument must be a term.
- **Variables**: Variables are symbols that represent unspecified objects. For example, `x`, `y`, and `z` are variables that can stand for any object in the domain of discourse. Variables are usually lowercase letters, and can be subscripted or primed to distinguish them from each other.
- **Quantifiers**: Quantifiers are symbols that express how many objects satisfy a given predicate. For example, `∀x P(x)` means that all objects have property `P`, and `∃x P(x)` means that there exists some object that has property `P`. Quantifiers can be nested to form complex expressions, such as `∀x ∃y R(x,y)`, which means that for every object `x`, there is some object `y` that is related to `x` by `R`. Quantifiers can also be restricted by specifying the domain of objects they range over, such as `∀x∈S P(x)`, which means that all objects in set `S` have property `P`.
- **Connectives**: Connectives are symbols that combine predicates or quantified expressions into more complex ones. For example, `P(x) ∧ Q(x)` means that object `x` has both properties `P` and `Q`, and `P(x) → Q(x)` means that if object `x` has property `P`, then it also has property `Q`. Connectives can also be applied to quantified expressions, such as `∀x P(x) → ∃x Q(x)`, which means that if all objects have property `P`, then there exists some object that has property `Q`. The connectives of predicate logic are the same as those of propositional logic, namely `¬` (negation), `∧` (conjunction), `∨` (disjunction), `→` (implication), and `↔` (equivalence).
- **Parentheses**: Parentheses are symbols that group expressions together and indicate the order of evaluation. For example, `(P(x) ∧ Q(x)) → R(x)` means that if object `x` has both properties `P` and `Q`, then it also has property `R`, and `P(x) ∧ (Q(x) → R(x))` means that object `x` has property `P`, and if it also has property `Q`, then it also has property `R`. Parentheses can also be used to group quantified expressions, such as `(∀x P(x)) ∧ (∃x Q(x))`, which means that all objects have property `P`, and there exists some object that has property `Q`.

### Predicate Logic Semantics

The semantics of predicate logic defines how to assign truth values to predicate logic expressions, given a domain of discourse and an interpretation. The domain of discourse is the set of objects that the variables and terms can refer to, and the interpretation is a function that assigns meanings to the predicates, functions, and constants.

- **Truth values**: Truth values are the possible outcomes of evaluating a predicate logic expression. There are two truth values, `true` and `false`, denoted by `T` and `F`, respectively.
- **Satisfiability**: A predicate logic expression is satisfiable if there is some domain of discourse and interpretation that makes it true. For example, `