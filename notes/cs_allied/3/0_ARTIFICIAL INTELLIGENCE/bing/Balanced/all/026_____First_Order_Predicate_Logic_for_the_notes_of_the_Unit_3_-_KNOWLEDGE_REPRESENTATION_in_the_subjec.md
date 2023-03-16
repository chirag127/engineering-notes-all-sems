# First Order Predicate Logic

- First order predicate logic (FOPL) is a formal language for representing and reasoning about the properties and relations of objects in a domain.
- FOPL extends propositional logic by introducing **predicates**, **quantifiers**, **functions**, and **constants**.
- A **predicate** is a symbol that represents a property or relation of one or more objects. For example, `Red(x)` means that x is red, and `Loves(x,y)` means that x loves y.
- A **quantifier** is a symbol that expresses how many objects in the domain satisfy a given predicate. For example, `∀x Red(x)` means that all objects are red, and `∃x Loves(x,y)` means that there exists some object that loves y.
- A **function** is a symbol that maps one or more objects to another object. For example, `Father(x)` means the father of x, and `Add(x,y)` means the sum of x and y.
- A **constant** is a symbol that represents a specific object in the domain. For example, `a` and `b` are constants that refer to particular objects.
- A **term** is either a constant, a variable, or a function applied to one or more terms. For example, `a`, `x`, `Father(x)`, and `Add(a,x)` are terms.
- An **atomic formula** is a predicate applied to one or more terms. For example, `Red(a)`, `Loves(x,y)`, and `Loves(Father(x),y)` are atomic formulas.
- A **formula** is either an atomic formula, or a complex formula formed by applying logical connectives and quantifiers to other formulas. For example, `Red(a) ∧ Loves(x,y)`, `∀x (Red(x) → Loves(x,y))`, and `∃x ∃y (Loves(x,y) ∧ Loves(y,x))` are formulas.
- The **semantics** of FOPL define how to assign truth values to formulas based on a **model** of the domain. A model consists of a **domain** (a set of objects), an **interpretation** (a mapping from symbols to objects, properties, and relations), and an **assignment** (a mapping from variables to objects).
- A formula is **satisfiable** if there exists a model and an assignment that make it true. A formula is **valid** if it is true in every model and assignment. A formula is **unsatisfiable** if it is false in every model and assignment. A formula is **contingent** if it is neither valid nor unsatisfiable.
- FOPL can be used to represent and reason about various kinds of knowledge, such as facts, rules, definitions, constraints, and preferences. For example, the following formulas express some knowledge about colors, shapes, and preferences:

  - `∀x (Red(x) ∨ Blue(x) ∨ Green(x))` (Every object is either red, blue, or green)
  - `∀x (Square(x) → Red(x))` (All squares are red)
  - `∀x ∀y ((Square(x) ∧ Circle(y)) → ¬Loves(x,y))` (No square loves any circle)
  - `∀x ∃y Loves(x,y)` (Everyone loves someone)
  - `∀x (Loves(x,a) → Loves(a,x))` (a is loved by everyone who loves a)
  - `∀x (Loves(x,b) → ¬Loves(b,x))` (b is not loved by anyone who loves b)
  - `Loves(a,b)` (a loves b)
  - `¬Loves(b,a)` (b does not love a)