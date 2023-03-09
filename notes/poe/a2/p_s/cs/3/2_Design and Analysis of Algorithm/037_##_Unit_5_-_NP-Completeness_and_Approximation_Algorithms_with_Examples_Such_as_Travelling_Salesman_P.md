 Here is the content in markdown format:

## Unit 5 - NP-Completeness and Approximation Algorithms with Examples

NP-Completeness:
- A problem is NP-complete if it is in NP and every other problem in NP can be reduced to it in polynomial time.
- NP-complete problems are the hardest problems in NP. If any NP-complete problem has a polynomial time solution, then all problems in NP have polynomial time solutions.
- Examples: Travelling Salesman Problem, Hamiltonian Cycle, Graph Coloring, Boolean Satisfiability Problem.

Approximation Algorithms:
- For NP-hard problems, exact optimal solutions cannot be found in polynomial time.
- Approximation algorithms provide feasible solutions in polynomial time which are close to the optimal solution.
- Performance of an approximation algorithm is measured using approximation ratio (ratio of its solution to the optimal solution).
- Examples:
    - Travelling Salesman Problem: Nearest Neighbour algorithm (approximation ratio ~2)
    - Graph Coloring: Greedy coloring algorithm (approximation ratio depends on graph structure)
    - Facility Location Problem: Greedy algorithm (approximation ratio 2)

Examples in Detail:

Travelling Salesman Problem (TSP):
- Find the shortest route visiting each city exactly once and returning to the starting city.
- NP-complete problem. Exact solutions require evaluating all permutations which is not feasible for large number of cities.
- Approximation algorithms: Nearest Neighbour (ratio ~2), 2-Approximation algorithm (ratio 2).
- Applications: Logistics, chip design, genome sequence assembly.

[Detailed explanations and diagrams for other examples can be added here]

Advantages of approximation algorithms:
- Provide feasible solutions in polynomial time for NP-hard problems.
- Solution quality can be adjusted by varying approximation ratio (higher ratio means less runtime but lower quality).
- For some problems, approximation ratios close to 1 can be achieved.

Disadvantages:
- No guarantees on obtaining optimal solutions.
- For some problems, best known approximation ratios can be quite high (e.g. travelling salesman has no approximation better than ~2 unless P=NP).