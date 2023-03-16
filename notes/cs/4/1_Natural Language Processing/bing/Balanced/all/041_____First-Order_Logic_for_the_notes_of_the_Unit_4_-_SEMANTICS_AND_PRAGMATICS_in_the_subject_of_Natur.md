# First-Order Logic

- First-order logic (FOL) is a formal language for representing and reasoning about the properties and relations of objects and events in the world.
- FOL is more expressive than propositional logic, which can only represent the truth values of atomic sentences.
- FOL can represent complex sentences that involve quantifiers, variables, predicates, and functions.
- FOL can also capture the meaning of natural language sentences more precisely and systematically than informal methods.

## Syntax of FOL

- The syntax of FOL defines the rules for constructing well-formed formulas (WFFs) from a set of symbols.
- The symbols of FOL include:
  - Logical constants: `true`, `false`
  - Logical connectives: `and`, `or`, `not`, `implies`, `iff`
  - Quantifiers: `forall`, `exists`
  - Variables: `x`, `y`, `z`, ...
  - Predicates: `P`, `Q`, `R`, ...
  - Functions: `f`, `g`, `h`, ...
  - Constants: `a`, `b`, `c`, ...
- The grammar of FOL is as follows:

  - A term is either a variable, a constant, or a function applied to one or more terms.
  - An atomic formula is a predicate applied to one or more terms.
  - A formula is either an atomic formula, a logical constant, or a complex formula formed by applying a logical connective to one or more formulas, or by applying a quantifier to a formula with a variable.
  - A sentence is a formula that contains no free variables (i.e., variables that are not bound by a quantifier).

- Examples of terms: `x`, `a`, `f(x)`, `g(a, b)`
- Examples of atomic formulas: `P(x)`, `Q(a, b)`, `R(f(x), g(a, b))`
- Examples of formulas: `P(x)`, `not Q(a, b)`, `P(x) and Q(a, b)`, `forall x P(x)`, `exists x (P(x) and Q(x))`
- Examples of sentences: `P(a)`, `not Q(a, b)`, `forall x P(x)`, `exists x (P(x) and Q(x))`, `forall x (P(x) implies Q(x))`

## Semantics of FOL

- The semantics of FOL defines the rules for assigning truth values to formulas based on a model of the domain of discourse.
- A model consists of:
  - A domain: a non-empty set of objects that the terms can refer to.
  - An interpretation: a mapping from the symbols of FOL to the domain or to truth values.
- The interpretation assigns:
  - A unique object in the domain to each constant symbol.
  - A truth value (`true` or `false`) to each logical constant symbol.
  - A function from the domain to the domain to each function symbol of arity n (i.e., a function that takes n arguments).
  - A relation on the domain to each predicate symbol of arity n (i.e., a relation that holds for n objects).
- The truth value of a formula in a model is determined by:
  - The truth value of an atomic formula is the truth value of the corresponding relation applied to the corresponding objects in the domain.
  - The truth value of a logical constant is the truth value assigned by the interpretation.
  - The truth value of a complex formula is the truth value of the corresponding logical connective applied to the truth values of the subformulas.
  - The truth value of a quantified formula is the truth value of the corresponding quantifier applied to the truth values of the formula with different assignments of objects to the variable.
- A formula is satisfiable if there exists a model in which it is true.
- A formula is valid if it is true in every model.
- A formula entails another formula if the latter is true in every model in which the former is true.
- Examples of models:

  - Domain: `{1, 2, 3}`
  - Interpretation:
    - `a` -> `1`
    - `b` -> `2`
    - `c` -> `3`
    - `true` -> `true`
    - `false` -> `false`
    - `f` -> `+1` (i.e., a function that adds one to its argument)
    - `g` -> `*` (i.e.,