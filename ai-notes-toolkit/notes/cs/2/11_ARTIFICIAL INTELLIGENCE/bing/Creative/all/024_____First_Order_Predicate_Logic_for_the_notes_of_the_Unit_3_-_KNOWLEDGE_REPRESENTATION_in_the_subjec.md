# First Order Predicate Logic

First order predicate logic (FOL) is a method of knowledge representation in artificial intelligence that extends propositional logic. FOL can express natural language statements in a concise and precise way, using objects, relations, functions, and quantifiers. FOL is also called predicate logic or first-order logic.

## Syntax of FOL

The syntax of FOL defines the rules for forming well-formed formulas (wffs) in the logic. A wff is a string of symbols that has a meaning in the logic. The basic symbols of FOL are:

- **Constants**: These are symbols that represent specific objects in the domain of discourse, such as `a`, `b`, `c`, `John`, `Mary`, etc.
- **Variables**: These are symbols that can stand for any object in the domain of discourse, such as `x`, `y`, `z`, etc.
- **Predicates**: These are symbols that represent properties or relations of objects, such as `P`, `Q`, `R`, `Red`, `House`, `Friend`, etc. Predicates can take one or more arguments, which are constants or variables, and are written as `P(x)`, `Q(x,y)`, `R(a,b,c)`, etc.
- **Functions**: These are symbols that represent mappings from objects to objects, such as `f`, `g`, `h`, `Father`, `Mother`, `Successor`, etc. Functions can take one or more arguments, which are constants or variables, and are written as `f(x)`, `g(x,y)`, `h(a,b,c)`, etc.
- **Connectives**: These are symbols that represent logical operations, such as `¬` (negation), `∧` (conjunction), `∨` (disjunction), `→` (implication), and `↔` (equivalence).
- **Quantifiers**: These are symbols that express the scope of variables, such as `∀` (universal quantifier) and `∃` (existential quantifier).
- **Parentheses**: These are symbols that group subformulas, such as `(` and `)`.

The rules for forming wffs in FOL are:

- If `c` is a constant, then `c` is a term.
- If `x` is a variable, then `x` is a term.
- If `f` is a function of arity `n` (meaning it takes `n` arguments), and `t1`, `t2`, ..., `tn` are terms, then `f(t1, t2, ..., tn)` is a term.
- If `P` is a predicate of arity `n`, and `t1`, `t2`, ..., `tn` are terms, then `P(t1, t2, ..., tn)` is an atomic formula.
- If `α` and `β` are wffs, then `¬α`, `(α ∧ β)`, `(α ∨ β)`, `(α → β)`, and `(α ↔ β)` are wffs.
- If `x` is a variable, and `α` is a wff, then `∀x α` and `∃x α` are wffs.
- Nothing else is a wff.

## Semantics of FOL

The semantics of FOL defines the rules for assigning truth values to wffs in the logic. A truth value is either true or false. The semantics of FOL depends on an interpretation, which is a mapping from the symbols of the logic to the objects and relations in the domain of discourse. An interpretation consists of:

- A non-empty set `D`, called the domain, which contains the objects of interest.
- A function `I`, called the interpretation function, which assigns a value to each symbol in the logic, such that:
  - If `c` is a constant, then `I(c)` is an element of `D`.
  - If `x` is a variable, then `I(x)` is an element of `D`.
  - If `P` is a predicate of arity `n`, then `I(P)` is a relation of arity `n` over `D`, meaning a set of `n`-tuples of elements of `D`.
  - If `f` is a function of arity `n`, then `I(f)` is a function of arity `n` over `D`, meaning a mapping from `n`-tuples of elements of `D` to