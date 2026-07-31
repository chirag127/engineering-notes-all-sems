 Here are the notes on NP-Completeness and Approximation Algorithms with Examples Such as Hamiltonian Cycles:

## NP-Completeness

- A decision problem is in NP if a `yes` answer can be verified in polynomial time.
- A problem is NP-complete if it is in NP and every other problem in NP can be reduced to it in polynomial time.
- NP-complete problems are the hardest problems in NP. If any NP-complete problem has a polynomial time algorithm, then P = NP.
- Examples of NP-complete problems: Hamiltonian cycle, travelling salesman problem, vertex cover, clique, subset sum, etc.

## Approximation Algorithms

- For NP-hard problems, it may not be possible to find an exact optimal solution efficiently.
- Approximation algorithms provide guaranteed near-optimal solutions in polynomial time.
- The approximation ratio is the maximum ratio of the cost of the approximate solution to the cost of the optimal solution.
- For example, a 2-approximation algorithm for TSP finds a tour no more than 2 times the length of the shortest tour.

## Hamiltonian Cycles

- A Hamiltonian cycle in a graph is a cycle that visits each vertex exactly once.
- Checking if a graph has a Hamiltonian cycle is NP-complete.
- Some graphs, such as complete graphs (cliques) and cycles, have Hamiltonian cycles.
- Approximation algorithms for Hamiltonian cycle find near-optimal solutions. A 2-approximation algorithm is to find a maximum cardinality matching and use the endpoints of matching edges as a cycle.