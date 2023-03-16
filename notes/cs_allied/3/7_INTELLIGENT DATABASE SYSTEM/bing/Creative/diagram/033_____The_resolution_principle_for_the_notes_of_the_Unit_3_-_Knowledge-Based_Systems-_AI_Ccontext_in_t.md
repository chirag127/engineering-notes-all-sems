### The resolution principle

- The resolution principle is a general rule of inference that can be used to derive new conclusions from a set of premises .
- It is based on the idea of resolving two clauses that contain complementary literals, i.e., a literal and its negation, into a new clause that contains the remaining literals .
- For example, if we have the clauses `p v q` and `¬p v r`, we can resolve them into `q v r` by eliminating the complementary literals `p` and `¬p`.
- The resolution principle can be applied to propositional logic and predicate logic, as well as other forms of logic .
- The resolution principle can be used for automated theorem proving, and more generally for automated deduction, by transforming a given problem into another problem that is easier to solve .
- For example, if we want to prove that a theorem `t` can be derived from a set of axioms `A`, we can use the resolution principle as follows :
  - Convert all sentences in `A` and `t` to conjunctive normal form (CNF), i.e., a conjunction of disjunctions of literals.
  - Negate the desired conclusion `t` and add it to the set of premises `A`.
  - Apply the resolution rule repeatedly to the clauses in the set until either:
    - A contradiction (an empty clause) is derived, in which case, `A` entails `t`.
    - No more clauses can be added, in which case, `A` does not entail `t`.
- The resolution principle is sound and complete, i.e., it can derive all and only the valid conclusions from a given set of premises .