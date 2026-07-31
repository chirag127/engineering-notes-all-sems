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
- The rules of syntax are:
  - If `P` is a predicate and `t1`, `t2`, ..., `tn` are terms, then `P(t1, t2, ..., tn)` is an atomic formula.
  - A term is either a variable, a constant, or a function applied to terms, such as `f(t1, t2, ..., tn)`.
  - If `p` and `q` are WFFs, then so are `not p`, `p and q`, `p or q`, `p implies q`, and `p iff q`.
  - If `p` is a WFF and `x` is a variable, then `forall x p` and `exists x p` are WFFs.
  - Nothing else is a WFF.

## Semantics of FOL

- The semantics of FOL defines the rules for assigning truth values to WFFs in a given model.
- A model consists of a domain of discourse (a set of objects) and an interpretation (a mapping from symbols to objects, relations, and functions).
- The truth value of a WFF depends on the model and a variable assignment (a mapping from variables to objects).
- The rules of semantics are:
  - An atomic formula `P(t1, t2, ..., tn)` is true if and only if the interpretation of `P` is a relation that holds for the objects denoted by the terms `t1`, `t2`, ..., `tn`.
  - A term `t` denotes an object in the domain, which is either the interpretation of `t` if `t` is a constant, the value of `t` under the variable assignment if `t` is a variable, or the result of applying the interpretation of `f` to the objects denoted by `t1`, `t2`, ..., `tn` if `t` is `f(t1, t2, ..., tn)`.
  - The logical connectives have their usual truth tables, such as `p and q` is true if and only if both `p` and `q` are true.
  - A quantified formula `forall x p` is true if and only if `p` is true for every possible value of `x` in the domain, and `exists x p` is true if and only if `p` is true for some value of `x` in the domain.