# The resolution principle

- The resolution principle is a general rule of inference that can be used to derive new conclusions from a set of premises .
- It is based on the idea of resolving two clauses that contain complementary literals, i.e., literals that are the negation of each other .
- For example, if we have the clauses `p v q` and `¬p v r`, we can resolve them on the literal `p` and obtain the new clause `q v r`.
- The resolution principle can be applied to propositional logic and predicate logic, with some modifications .
- In propositional logic, the resolution principle can be used to perform automated theorem proving, by converting all the sentences to conjunctive normal form (CNF), negating the desired conclusion, and applying the resolution rule until either a contradiction is reached or no more clauses can be added .
- In predicate logic, the resolution principle requires the use of unification, a process of finding a substitution for the variables in the clauses that makes them identical .
- For example, if we have the clauses `P(x) v Q(y)` and `¬Q(a) v R(z)`, we can unify them on the literal `Q` by substituting `y` with `a`, and obtain the new clause `P(x) v R(z)`.
- The resolution principle is the basis of logic programming and production rules paradigms, which use resolution to infer new facts from a knowledge base.