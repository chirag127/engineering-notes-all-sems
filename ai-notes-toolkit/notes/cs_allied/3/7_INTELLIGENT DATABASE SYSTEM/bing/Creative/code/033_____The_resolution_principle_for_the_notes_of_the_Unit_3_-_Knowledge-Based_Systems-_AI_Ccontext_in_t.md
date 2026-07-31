### The resolution principle

- The resolution principle is a general rule of inference that can be used to derive new conclusions from a set of premises .
- It is based on the idea of resolving two clauses that contain complementary literals, i.e., literals that are the negation of each other, into a new clause that contains the remaining literals .
- For example, if we have the clauses `p v q` and `¬p v r`, we can resolve them on the literal `p` and obtain the new clause `q v r`.
- The resolution principle can be applied to propositional logic and predicate logic, as well as other forms of logic .
- In artificial intelligence, resolution is a technique for automated theorem proving, and more generally for automated deduction .
- It can be used to check the validity or satisfiability of a formula, or to prove that a formula is entailed by a knowledge base .
- The resolution algorithm is a systematic procedure that applies the resolution principle repeatedly to a set of clauses until either a contradiction is derived or no more clauses can be added .
- The resolution algorithm works as follows :
  - Convert all the sentences in the knowledge base and the negation of the desired conclusion to conjunctive normal form (CNF), i.e., a conjunction of disjunctions of literals.
  - Add all the clauses to a set S.
  - Repeat until either a contradiction is derived or no new clauses can be added:
    - Select two clauses from S that contain complementary literals.
    - Resolve them into a new clause C.
    - If C is empty, then a contradiction is derived and the algorithm terminates with success.
    - If C is not empty and not already in S, then add C to S.
    - If no new clauses can be added, then the algorithm terminates with failure.

: https://www.surfactants.net/the-resolution-process-in-artificial-intelligence/
: https://www.surfactants.net/what-is-resolution-in-predicate-logic-in-artificial-intelligence-2/
: https://www.geeksforgeeks.org/resolution-algorithm-in-artificial-intelligence/
: https://www.sciencedirect.com/topics/computer-science/resolution-principle
: http://www.ai.mit.edu/courses/6.825/fall02/pdf/6.825-lecture-07.pdf