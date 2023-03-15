Hello, I am Sydney, your AI assistant. I can help you with writing notes on First Order Predicate Logic for the Unit 3 - Knowledge Representation in the subject of Artificial Intelligence KCS. Here is the content in markdown format:

### First Order Predicate Logic

- First Order Predicate Logic (FOPL) is a formal language for representing and reasoning about knowledge in a logical and precise way.
- FOPL extends propositional logic by introducing **predicates**, **quantifiers**, **functions**, and **constants**.
- A **predicate** is a symbol that represents a property or relation of one or more objects. For example, `Likes(x, y)` is a predicate that means "x likes y".
- A **quantifier** is a symbol that expresses how many objects satisfy a given predicate. There are two main types of quantifiers: **universal** and **existential**.
  - A **universal quantifier** (∀) means "for all" or "every". For example, `∀x Likes(x, x)` means "everyone likes themselves".
  - An **existential quantifier** (∃) means "there exists" or "some". For example, `∃x Likes(x, y)` means "someone likes y".
- A **function** is a symbol that maps one or more objects to another object. For example, `Father(x)` is a function that returns the father of x.
- A **constant** is a symbol that represents a specific object. For example, `Alice` is a constant that refers to a person named Alice.
- A **term** is either a constant, a variable, or a function applied to one or more terms. For example, `Father(Alice)` and `x` are terms.
- An **atomic formula** is a predicate applied to one or more terms. For example, `Likes(Father(Alice), x)` is an atomic formula.
- A **formula** is either an atomic formula, or a complex formula formed by applying logical connectives (¬, ∧, ∨, →, ↔) and quantifiers to other formulas. For example, `∀x Likes(x, x) → Likes(Father(x), x)` is a formula.
- A **model** is a structure that assigns a meaning to the symbols of FOPL. A model consists of a **domain** (a set of objects), an **interpretation** (a mapping from constants and functions to objects, and from predicates to relations), and a **valuation** (a mapping from variables to objects).
- A formula is **satisfiable** if there exists a model and a valuation that make it true. A formula is **valid** if it is true in every model and valuation. A formula is **unsatisfiable** if it is false in every model and valuation. A formula is **contingent** if it is neither valid nor unsatisfiable.
- A formula **entails** another formula if the truth of the first formula implies the truth of the second formula in every model and valuation. For example, `∀x Likes(x, x)` entails `Likes(Alice, Alice)`.
- A set of formulas is **consistent** if there exists a model and a valuation that make all of them true. A set of formulas is **inconsistent** if there is no such model and valuation. A set of formulas is **complete** if for any formula, either the set entails the formula or the set entails its negation.