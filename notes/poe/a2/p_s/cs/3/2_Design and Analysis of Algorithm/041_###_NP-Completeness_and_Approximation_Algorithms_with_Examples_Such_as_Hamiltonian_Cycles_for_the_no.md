 Here are the notes for the topic ### NP-Completeness and Approximation Algorithms with Examples Such as Hamiltonian Cycles:

NP-Completeness:
- NP-Completeness is a class of computational problems whose solutions can be verified in polynomial time but cannot be solved in polynomial time.
- These problems are the hardest problems in NP and are intractable in the worst case.
- Examples: Traveling Salesman Problem, Hamiltonian Cycle, Graph Coloring, Subset Sum problem, etc.

Approximation Algorithms:
- For NP-hard problems, we cannot find exact optimal solutions efficiently. Hence, we look for approximation algorithms that can find near-optimal solutions efficiently.
- The performance of an approximation algorithm is measured using an approximation ratio which is the worst-case ratio of the cost of the solution found by the algorithm to the cost of the optimal solution.
- For example, a 2-approximate algorithm for the TSP finds a tour of length at most 2 times the length of the optimal tour.

Hamiltonian Cycles:
- A Hamiltonian cycle in a graph is a cycle that visits each vertex exactly once.
- Hamiltonian cycle is an NP-complete problem. There is no known polynomial time algorithm to detect whether a given graph contains a Hamiltonian cycle or not unless P=NP.
- However, for some graph classes like planar graphs and graphs with degrees bounded by a constant, Hamiltonian cycle can be solved in polynomial time.
- Approximation algorithms with approximation ratios 2 and 3/2 are known for the Hamiltonian cycle problem.

[Diagrams and examples can be added here for better understanding]

Advantages: Approximation algorithms can find reasonably good solutions for NP-hard problems in polynomial time.
Disadvantages: The solutions found may not be optimal. The approximation ratio depends on the problem and the algorithm.
Applications: Used in scheduling, routing, clustering problems where finding exact optimal solutions is not feasible.