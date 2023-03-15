Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Artificial Intelligence KCS. Here is the content for the topic of First Order Predicate Logic for the notes of the Unit 3 - Knowledge Representation.

### First Order Predicate Logic

- First Order Predicate Logic (FOPL) is a form of logic that extends propositional logic by introducing quantifiers, predicates, functions, and variables.
- FOPL allows us to express more complex sentences and relations than propositional logic, which only deals with atomic propositions and logical connectives.
- FOPL is also called First Order Logic (FOL) or Predicate Calculus.

#### Syntax of FOPL

- The syntax of FOPL defines the rules for forming well-formed formulas (wffs) in the logic.
- The basic elements of FOPL are:

  - **Constants**: symbols that represent specific objects in the domain of discourse, such as `a`, `b`, `c`, etc.
  - **Variables**: symbols that can stand for any object in the domain of discourse, such as `x`, `y`, `z`, etc.
  - **Predicates**: symbols that represent properties or relations of objects in the domain of discourse, such as `P`, `Q`, `R`, etc. Predicates can have one or more arguments, which are constants or variables. For example, `P(x)` is a unary predicate, `Q(x,y)` is a binary predicate, and `R(x,y,z)` is a ternary predicate.
  - **Functions**: symbols that represent mappings from objects to objects in the domain of discourse, such as `f`, `g`, `h`, etc. Functions can have one or more arguments, which are constants or variables. For example, `f(x)` is a unary function, `g(x,y)` is a binary function, and `h(x,y,z)` is a ternary function.
  - **Logical connectives**: symbols that represent logical operations on wffs, such as `¬` (negation), `∧` (conjunction), `∨` (disjunction), `→` (implication), and `↔` (equivalence).
  - **Quantifiers**: symbols that represent the scope of variables in wffs, such as `∀` (universal quantifier) and `∃` (existential quantifier).

- The rules for forming wffs in FOPL are:

  - If `P` is a predicate and `t1, t2, ..., tn` are terms (constants, variables, or functions), then `P(t1, t2, ..., tn)` is a wff. This is called an **atomic formula**.
  - If `φ` is a wff, then `¬φ` is a wff. This is called a **negated formula**.
  - If `φ` and `ψ` are wffs, then `(φ ∧ ψ)`, `(φ ∨ ψ)`, `(φ → ψ)`, and `(φ ↔ ψ)` are wffs. These are called **compound formulas**.
  - If `φ` is a wff and `x` is a variable, then `∀x φ` and `∃x φ` are wffs. These are called **quantified formulas**.
  - Nothing else is a wff.

- Some examples of wffs in FOPL are:

  - `P(a)`: an atomic formula that states that `a` has the property `P`.
  - `¬Q(x,y)`: a negated formula that states that `x` and `y` do not have the relation `Q`.
  - `(P(a) ∧ Q(x,y))`: a compound formula that states that `a` has the property `P` and `x` and `y` have the relation `Q`.
  - `∀x P(x)`: a quantified formula that states that every object in the domain has the property `P`.
  - `∃x (Q(x,a) → R(f(x),b))`: a quantified formula that states that there exists an object in the domain such that if it has the relation `Q` with `a`, then it has the relation `R` with the result of applying the function `f` to it and `b`.

#### Semantics of FOPL

- The semantics of FOPL defines the rules for assigning truth values to wffs in the logic, given an interpretation of the symbols in the logic.
- An interpretation of FOPL consists of:

  - A **domain of discourse** or **universe**, which is a non