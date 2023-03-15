Hello, I am Sydney, your AI assistant. I can help you with your notes on First Order Predicate Logic for the Unit 3 - Knowledge Representation in the subject of Artificial Intelligence KCS. Here is the content in markdown format:

# First Order Predicate Logic

## Introduction

- First Order Predicate Logic (FOPL) is a formal language for representing and reasoning about knowledge in a domain.
- FOPL extends propositional logic by allowing the use of variables, constants, predicates, functions, and quantifiers.
- FOPL can express more complex and general statements than propositional logic, such as "All humans are mortal" or "There is a red car in the parking lot".
- FOPL can also handle relations between objects, such as "John is the father of Mary" or "Paris is the capital of France".

## Syntax

- The basic elements of FOPL are **terms** and **formulas**.
- A **term** is an expression that denotes an object in the domain. Terms can be:
  - **Constants**: symbols that represent specific objects, such as `John`, `Paris`, or `3`.
  - **Variables**: symbols that can stand for any object, such as `x`, `y`, or `z`.
  - **Functions**: symbols that map terms to terms, such as `father(x)`, `square(2)`, or `plus(x,y)`.
- A **formula** is an expression that denotes a truth value (true or false). Formulas can be:
  - **Atomic formulas**: symbols that represent properties or relations of terms, such as `human(John)`, `father(John,Mary)`, or `equal(plus(x,y),z)`.
  - **Complex formulas**: formulas that are composed of other formulas using logical connectives, such as `not`, `and`, `or`, `implies`, or `iff`.
  - **Quantified formulas**: formulas that are prefixed by a quantifier, such as `forall` or `exists`, and a variable, such as `forall x human(x) implies mortal(x)` or `exists x red(car(x))`.

## Semantics

- The meaning of a FOPL expression depends on the **interpretation** of the symbols in the expression.
- An **interpretation** consists of a **domain** and an **assignment**.
- A **domain** is a set of objects that the terms can refer to, such as the set of all humans, all cars, or all numbers.
- An **assignment** is a function that maps symbols to objects or truth values, such as `John -> John Smith`, `Paris -> Paris, France`, `human -> {John, Mary, ...}`, `father -> {(John, Mary), (Bob, Alice), ...}`, `plus -> +`, `true -> true`, `false -> false`.
- The **truth value** of a formula under an interpretation is determined by the following rules:
  - An atomic formula is true if and only if the assignment maps the predicate to a set that contains the tuple of objects denoted by the terms, such as `human(John)` is true if and only if `John Smith` is in the set assigned to `human`.
  - A complex formula is true if and only if the truth value of the subformulas and the logical connectives match, such as `not human(John)` is true if and only if `human(John)` is false, `human(John) and mortal(John)` is true if and only if both `human(John)` and `mortal(John)` are true, etc.
  - A quantified formula is true if and only if the quantifier and the variable range over the domain and the truth value of the subformula match, such as `forall x human(x) implies mortal(x)` is true if and only if for every object in the domain, if it is in the set assigned to `human`, then it is also in the set assigned to `mortal`, `exists x red(car(x))` is true if and only if there is an object in the domain that is in the set assigned to `car` and also in the set assigned to `red`, etc.