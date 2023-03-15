## Unit 5 - Predicate Logic

Predicate logic is a branch of logic that deals with predicates, quantifiers, and variables. Predicate logic is more expressive than propositional logic, as it can capture the structure and relations of objects and properties in a domain of discourse.

Some key concepts and terms in predicate logic are:

- A **predicate** is a symbol that represents a property or relation of one or more objects. For example, P(x) could mean "x is prime" or "x is purple".
- A **quantifier** is a symbol that expresses how many objects in a domain satisfy a predicate. The two most common quantifiers are the universal quantifier (∀), which means "for all", and the existential quantifier (∃), which means "there exists".
- A **variable** is a symbol that can stand for any object in a domain. Variables are usually lowercase letters, such as x, y, z. Variables can be bound by quantifiers or free, meaning they are not bound by any quantifier.
- A **constant** is a symbol that stands for a specific object in a domain. Constants are usually uppercase letters, such as A, B, C. Constants are always free variables.
- A **term** is either a variable or a constant. Terms can be used as arguments for predicates. For example, P(x) and P(A) are terms.
- A **formula** is a well-formed expression that can be true or false in a domain. Formulas can be atomic, meaning they consist of a single predicate and one or more terms, or complex, meaning they are formed by combining atomic formulas with logical connectives and quantifiers. For example, P(x) and Q(x) are atomic formulas, and P(x) ∧ Q(x) and ∃x P(x) are complex formulas.
- A **model** is a pair (D, I), where D is a non-empty set called the domain, and I is an interpretation function that assigns meanings to the symbols in the language. I maps each constant to an element of D, each predicate to a subset of D^n (where n is the arity of the predicate), and each logical connective and quantifier to their usual truth functions. A model determines the truth value of a formula in a domain.
- A **valuation** is a function that assigns values to the free variables in a formula. A valuation can be extended to a model by using the interpretation function I. A valuation satisfies a formula if the formula is true under that valuation and model. A formula is **satisfiable** if there exists a valuation and a model that satisfy it, and **unsatisfiable** otherwise.
- A formula is **valid** if it is true under every valuation and model, and **invalid** otherwise. A formula is **contingent** if it is neither valid nor invalid, meaning it is true under some valuations and models, and false under others.
- A formula α **entails** another formula β, written as α |= β, if every valuation and model that satisfy α also satisfy β. A formula α is **equivalent** to another formula β, written as α ≡ β, if α and β have the same truth value under every valuation and model.