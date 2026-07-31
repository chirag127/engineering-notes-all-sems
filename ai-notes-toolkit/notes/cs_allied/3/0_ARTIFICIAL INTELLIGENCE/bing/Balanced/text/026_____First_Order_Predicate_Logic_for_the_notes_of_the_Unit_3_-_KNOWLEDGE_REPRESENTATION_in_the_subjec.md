### First Order Predicate Logic

- First order predicate logic (FOPL) is a formal language for representing and reasoning about the properties and relations of objects in a domain.
- FOPL extends propositional logic by introducing **predicates**, **quantifiers**, **functions**, and **constants**.
- A **predicate** is a symbol that represents a property or relation of one or more objects. For example, `P(x)` means that object `x` has property `P`, and `Q(x,y)` means that objects `x` and `y` are related by `Q`.
- A **quantifier** is a symbol that expresses how many objects in the domain satisfy a given predicate. For example, `∀x P(x)` means that all objects have property `P`, and `∃x Q(x,y)` means that there exists some object that is related to `y` by `Q`.
- A **function** is a symbol that represents a mapping from one or more objects to another object. For example, `f(x)` means the object that is mapped from `x` by `f`, and `g(x,y)` means the object that is mapped from `x` and `y` by `g`.
- A **constant** is a symbol that represents a specific object in the domain. For example, `a` means the object `a`, and `b` means the object `b`.
- A **term** is either a constant, a variable, or a function applied to one or more terms. For example, `a`, `x`, `f(x)`, and `g(a,b)` are terms.
- An **atomic formula** is a predicate applied to one or more terms. For example, `P(a)`, `Q(x,y)`, and `R(f(x),g(a,b))` are atomic formulas.
- A **formula** is either an atomic formula, or a complex formula formed by applying logical connectives and quantifiers to formulas. For example, `P(a) ∧ Q(x,y)`, `∀x (P(x) → Q(x,f(x)))`, and `∃y (R(y,y) ∨ ¬Q(a,y))` are formulas.
- A **model** is an interpretation of the symbols in FOPL that assigns a domain of objects, a denotation for each constant, a function for each function symbol, and a truth value for each atomic formula. For example, a model for the formula `P(a) ∧ Q(x,y)` could assign the domain `{1,2,3}`, the denotation `1` for `a`, the function `+1` for `f`, the truth value `true` for `P(1)` and `Q(2,3)`, and the truth value `false` for all other atomic formulas.
- A formula is **satisfiable** if there exists some model that makes it true, and **unsatisfiable** otherwise. For example, the formula `P(a) ∧ ¬P(a)` is unsatisfiable, since no model can make it true.
- A formula is **valid** if it is true in all models, and **invalid** otherwise. For example, the formula `∀x P(x) → ∃x P(x)` is valid, since it is true in any model.
- A formula is **entailed** by a set of formulas if it is true in all models that make the set true, and **not entailed** otherwise. For example, the formula `P(a)` is entailed by the set `{P(a), Q(a,b)}`, since any model that makes the set true must also make `P(a)` true.