 Here are the notes for the topic -

NP-Completeness and Approximation Algorithms with Examples Such as Travelling Salesman Problem

### NP-Completeness

- NP-Completeness is a class of computational problems whose solutions can be verified in polynomial time but cannot be solved in polynomial time.
- A decision problem is in NP if a 'yes' answer can be verified in polynomial time. A problem is NP-Complete if it is in NP and every other problem in NP can be reduced to it in polynomial time.
- Examples of NP-Complete problems are Hamiltonian Path, Clique, Vertex Cover, Travelling Salesman Problem, etc.

### Approximation Algorithms

- Since NP-Complete problems cannot be solved in polynomial time, we look for algorithms that produce near-optimal solutions efficiently. These are called Approximation Algorithms.
- The performance of an approximation algorithm is measured as an approximation ratio or approximation factor. It is the worst-case ratio of the algorithm's solution to the optimal solution.
- Examples are Greedy algorithms, Local search, etc.

### Travelling Salesman Problem (TSP)

- TSP is the problem of finding the shortest route that visits each city exactly once and returns to the origin city.
- It is NP-Hard. Exact algorithms take exponential time. Approximation algorithms give near-optimal solutions.
- Nearest Neighbour heuristic starts from a random city and visits the nearest unvisited city in each step. It gives an approximation ratio of 2.
- Christofides algorithm gives an approximation ratio of 3/2. It finds a minimum weight matching in a graph and converts it into a Eulerian circuit by adding edges.