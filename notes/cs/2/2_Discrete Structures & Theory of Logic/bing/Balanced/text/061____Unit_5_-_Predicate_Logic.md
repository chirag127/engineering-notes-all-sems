## Unit 5 - Predicate Logic

- Predicate logic is a branch of logic that deals with predicates, quantifiers, and variables.
- A predicate is a statement that can be true or false depending on the values of its arguments. For example, `P(x)` is a predicate that says `x` is a prime number.
- A quantifier is a symbol that expresses how many or how much of something satisfies a predicate. For example, `∀x P(x)` is a quantified statement that says `for all x, x is a prime number`.
- A variable is a symbol that can represent any value in a given domain. For example, `x` is a variable that can represent any natural number.
- Predicate logic allows us to express more complex and general statements than propositional logic, which only deals with propositions that are true or false by themselves.
- Predicate logic has two main types of formulas: atomic formulas and complex formulas.
- An atomic formula is a formula that consists of a predicate and its arguments. For example, `P(x)` and `Q(a,b)` are atomic formulas.
- A complex formula is a formula that is formed by combining atomic formulas using logical connectives and/or quantifiers. For example, `∀x (P(x) → Q(x,a))` and `∃y (R(y) ∧ ¬S(y,b))` are complex formulas.
- The syntax and semantics of predicate logic are defined by a set of rules that specify how to construct and interpret formulas.
- The syntax rules specify how to form well-formed formulas (wffs) using symbols, parentheses, and variables.
- The semantics rules specify how to assign truth values to formulas using a structure, which consists of a domain and an interpretation.
- A domain is a set of values that the variables can take. For example, the domain of natural numbers is `{0, 1, 2, 3, ...}`.
- An interpretation is a function that assigns meanings to the predicates and constants in a formula. For example, an interpretation can define `P(x)` to mean `x is even` and `a` to mean `2`.
- A formula is true in a structure if it is true for all possible assignments of values to the variables in the formula. For example, `∀x P(x)` is true in a structure if `P(x)` is true for every value in the domain.
- A formula is valid if it is true in every possible structure. For example, `∀x (P(x) → P(x))` is valid because it is a tautology.
- A formula is satisfiable if it is true in some possible structure. For example, `∃x P(x)` is satisfiable if there is at least one value in the domain that makes `P(x)` true.
- A formula is unsatisfiable if it is false in every possible structure. For example, `∀x ¬P(x) ∧ ∃x P(x)` is unsatisfiable because it is a contradiction.