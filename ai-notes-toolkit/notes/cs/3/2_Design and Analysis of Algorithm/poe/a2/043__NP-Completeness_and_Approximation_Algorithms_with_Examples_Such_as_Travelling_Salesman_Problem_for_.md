 Here are the notes on NP-Completeness and Approximation Algorithms with Examples Such as Travelling Salesman Problem:

### NP-Completeness

- A decision problem is NP-complete if it is in NP and every other problem in NP can be reduced to it in polynomial time.
- NP-complete problems are the hardest problems in NP. If any NP-complete problem has a polynomial time algorithm, then all problems in NP have polynomial time algorithms.
- Examples of NP-complete problems: Boolean Satisfiability Problem, Hamiltonian Path Problem, Travelling Salesman Problem, etc.

### Approximation Algorithms

- For NP-hard problems, we cannot hope for efficient exact algorithms. We look for efficient algorithms that find approximate solutions.
- An approximation algorithm is a polynomial time algorithm that finds a solution that is within a constant factor of the optimal solution.
- The approximation ratio/factor is the maximum ratio of the approximate solution to the optimal solution over all instances.
- A PTAS is a polynomial time approximation scheme which can get an (1+??)-approximate solution for any ??.
- Examples: Travelling salesman problem, vertex cover problem, etc.

### Travelling Salesman Problem (TSP)

- Given a set of cities and distances between each pair of cities, the problem is to find the shortest possible tour that visits each city exactly once and returns to the starting city.
- It is NP-hard. Some approximation algorithms for TSP:
    - Nearest neighbour: Pick the nearest unvisited city at each step. Approximation ratio: 2.
    - Christofides algorithm: Greedy algorithm followed by minimum weight perfect matching. Approximation ratio: 3/2
- Other approximation algorithms exist with approximation ratios slightly better than the above algorithms.
