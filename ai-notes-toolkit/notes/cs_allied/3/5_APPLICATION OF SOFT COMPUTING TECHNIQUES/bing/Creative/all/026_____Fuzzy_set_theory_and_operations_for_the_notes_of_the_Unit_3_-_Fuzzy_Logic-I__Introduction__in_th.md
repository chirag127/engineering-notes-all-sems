# Fuzzy set theory and operations

Fuzzy set theory is a branch of mathematics that deals with sets whose elements have degrees of membership. Unlike classical sets, where an element either belongs or does not belong to a set, fuzzy sets allow for partial or graded membership. Fuzzy sets were introduced by Lotfi A. Zadeh in 1965 as an extension of the classical notion of set.

Fuzzy sets can be used to model uncertainty, vagueness, ambiguity, and imprecision in various domains, such as logic, control, game, topology, pattern recognition, linguistics, taxonomy, system, decision making, information retrieval and so on.

Some basic concepts and definitions of fuzzy set theory are:

- A fuzzy set ~A is a set of ordered pairs of the form (\uD835\uDC66, \uD835\uDC6F(\uD835\uDC66)), where \uD835\uDC66 is an element of the universe of discourse U and \uD835\uDC6F(\uD835\uDC66) is the degree of membership of \uD835\uDC66 in ~A, ranging from 0 to 1. The function \uD835\uDC6F is called the membership function of ~A.
- A fuzzy set ~A is said to be normal if there exists at least one element \uD835\uDC66 in U such that \uD835\uDC6F(\uD835\uDC66) = 1. Otherwise, ~A is said to be subnormal.
- A fuzzy set ~A is said to be convex if for any two elements \uD835\uDC66 and \uD835\uDC67 in U and any \uD835\uDC68 in [0, 1], \uD835\uDC6F(\uD835\uDC68\uD835\uDC66 + (1 - \uD835\uDC68)\uD835\uDC67) ≥ min(\uD835\uDC6F(\uD835\uDC66), \uD835\uDC6F(\uD835\uDC67)). Otherwise, ~A is said to be non-convex.
- A fuzzy set ~A is said to be singleton if there exists only one element \uD835\uDC66 in U such that \uD835\uDC6F(\uD835\uDC66) > 0. Otherwise, ~A is said to be non-singleton.

Some common operations that can be performed on fuzzy sets are:

- Fuzzy complement: The complement of a fuzzy set ~A is a fuzzy set ~A^c defined by \uD835\uDC6F^c(\uD835\uDC66) = 1 - \uD835\uDC6F(\uD835\uDC66) for all \uD835\uDC66 in U.
- Fuzzy union: The union of two fuzzy sets ~A and ~B is a fuzzy set ~A ∪ ~B defined by \uD835\uDC6F∪(\uD835\uDC66) = max(\uD835\uDC6F(\uD835\uDC66), \uD835\uDC70(\uD835\uDC66)) for all \uD835\uDC66 in U.
- Fuzzy intersection: The intersection of two fuzzy sets ~A and ~B is a fuzzy set ~A ∩ ~B defined by \uD835\uDC6F∩(\uD835\uDC66) = min(\uD835\uDC6F(\uD835\uDC66), \uD835\uDC70(\uD835\uDC66)) for all \uD835\uDC66 in U.
- Fuzzy algebraic product: The algebraic product of two fuzzy sets ~A and ~B is a fuzzy set ~A ⊗ ~B defined by \uD835\uDC6F⊗(\uD835\uDC66) = \uD835\uDC6F(\uD835\uDC66) × \uD835\uDC70(\uD835\uDC66) for all \uD835\uDC66 in U.
- Fuzzy algebraic sum: The algebraic sum of two fuzzy sets ~A and ~B is a fuzzy set ~A ⊕ ~B defined by \uD835\uDC6F⊕(\uD835\uDC66) = \uD835\uDC6F(\uD835\uDC66) + \uD835\uDC70(\uD835\uDC66) - \uD835\uDC6F(\uD835