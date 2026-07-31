### The resolution principle

- The resolution principle is a general rule of inference that can be used to derive new conclusions from a set of premises .
- It is based on the idea of resolving two clauses that contain complementary literals, i.e., a literal and its negation, into a new clause that contains the remaining literals .
- For example, if we have the clauses `p v q` and `¬p v r`, we can resolve them into `q v r` by eliminating the complementary literals `p` and `¬p`.
- The resolution principle can be applied to propositional logic, predicate logic, and other forms of logic .
- The resolution principle can be used for automated theorem proving, and more generally for automated deduction .
- The resolution principle can also be used for checking the consistency and entailment of a knowledge base .
- The resolution principle can be implemented as an algorithm that takes a set of clauses as input and tries to derive the empty clause, which represents a contradiction .
- The algorithm works as follows :
  - Convert all the sentences in the knowledge base and the negation of the desired conclusion to conjunctive normal form (CNF), i.e., a conjunction of disjunctions of literals.
  - Add all the clauses to a set S.
  - Repeat until either the empty clause is derived or no more clauses can be added:
    - Select two clauses from S that contain complementary literals.
    - Apply the resolution rule to them and obtain a new clause.
    - If the new clause is the empty clause, then stop and report that the knowledge base entails the conclusion.
    - Otherwise, if the new clause is not already in S, then add it to S.
  - If the loop terminates without deriving the empty clause, then stop and report that the knowledge base does not entail the conclusion.