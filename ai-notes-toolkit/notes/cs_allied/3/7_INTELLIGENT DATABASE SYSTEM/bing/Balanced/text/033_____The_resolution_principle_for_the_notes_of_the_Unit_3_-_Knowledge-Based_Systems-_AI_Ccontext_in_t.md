### The resolution principle

- The resolution principle is a general rule of inference that can be used to derive new conclusions from a set of premises .
- It is based on the idea of resolving two clauses that contain complementary literals, i.e., a literal and its negation, into a new clause that contains the remaining literals .
- For example, if we have the clauses `p v q` and `¬p v r`, we can resolve them on `p` and obtain the new clause `q v r`.
- The resolution principle can be applied to propositional logic and predicate logic, with some modifications .
- In propositional logic, the resolution principle can be used to perform automated theorem proving by converting all the sentences and the negated conclusion to conjunctive normal form (CNF) and then applying the resolution rule repeatedly until either a contradiction (the empty clause) is derived or no more clauses can be added .
- In predicate logic, the resolution principle requires the use of unification, a process of finding a substitution for the variables in the clauses that makes them identical .
- For example, if we have the clauses `P(x) v Q(y)` and `¬Q(a) v R(z)`, we can unify them on `Q` by substituting `y` with `a` and obtain the new clause `P(x) v R(z)`.
- The resolution principle is the basis of logic programming and production rules paradigms in artificial intelligence.