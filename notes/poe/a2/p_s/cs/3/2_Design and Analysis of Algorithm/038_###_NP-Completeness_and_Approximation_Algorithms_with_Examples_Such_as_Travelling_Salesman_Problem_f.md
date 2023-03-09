 Here are the notes for the topic ### NP-Completeness and Approximation Algorithms with Examples Such as Travelling Salesman Problem:

NP-Completeness:
- A decision problem is NP-complete if it is in NP and every other problem in NP can be reduced to it in polynomial time.
- NP-complete problems are the hardest problems in NP. If any NP-complete problem has a polynomial time algorithm, then all problems in NP have polynomial time algorithms.
- Examples: Boolean Satisfiability (SAT), Hamiltonian Path, Travelling Salesman Problem (TSP), Graph Coloring, n-Queens Problem, etc.

Travelling Salesman Problem (TSP):
- Given a list of cities and distances between each pair of cities, find the shortest possible route that visits each city exactly once and returns to the origin city.
- It is NP-hard as the number of possible routes increases exponentially with number of cities.
- Approximate solutions can be found in polynomial time. The challenge is to get close to the optimal solution.
- Applications: Vehicle routing, circuit design, logistics, etc.

Approximation Algorithms:
- For NP-hard problems, algorithms that find feasible solutions with guaranteed worst-case performance ratio (approximation ratio) with respect to optimal solution.
- Examples:
-- For TSP, a 2-approximation algorithm: Pick the pair of cities at minimum distance and include the edge. Repeat until all cities are included.
-- For vertex cover, a 2-approximation algorithm: Include all vertices with degree ???2.
-- For graph coloring, a 2-approximation algorithm: Assign colors greedily.

Advantages:
- Provides fast solutions for hard problems.
- Useful when finding exact optimal solutions takes too long.
- Can provide guaranteed level of sub-optimality.

Disadvantages:
- Does not find optimal solutions.
- Hard to achieve good approximation ratios for some problems.