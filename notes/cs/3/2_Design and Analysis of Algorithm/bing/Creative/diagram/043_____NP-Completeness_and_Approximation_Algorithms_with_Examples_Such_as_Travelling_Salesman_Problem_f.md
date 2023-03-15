# NP-Completeness and Approximation Algorithms

## NP-Completeness

- NP-Completeness is a concept that deals with the complexity of decision problems, which are problems that have a yes or no answer.
- A problem is in NP if it can be verified in polynomial time, given a certificate or a witness for the yes answer. For example, the problem of checking whether a graph has a Hamiltonian cycle is in NP, because given a cycle, we can verify that it visits every vertex exactly once in polynomial time.
- A problem is NP-hard if every problem in NP can be reduced to it in polynomial time. This means that solving the NP-hard problem would also solve any NP problem. For example, the problem of finding a Hamiltonian cycle in a graph is NP-hard, because we can reduce any NP problem to it using a polynomial time transformation.
- A problem is NP-complete if it is both in NP and NP-hard. This means that it is among the hardest problems in NP, and no polynomial time algorithm is known for solving it. For example, the problem of deciding whether a graph has a 3-coloring is NP-complete, because it is in NP and we can reduce any NP problem to it using a polynomial time transformation.
- NP-completeness is important because it shows the limits of efficient computation. If P ≠ NP, then there is no polynomial time algorithm for any NP-complete problem, unless we can find a polynomial time algorithm for all NP problems. Therefore, finding a polynomial time algorithm for any NP-complete problem would be a major breakthrough in computer science.

## Approximation Algorithms

- Approximation Algorithms are a way of dealing with NP-completeness for optimization problems, which are problems that seek to find the best solution among many possible solutions. For example, the problem of finding the shortest tour that visits every city in a given set is an optimization problem, known as the Traveling Salesman Problem (TSP).
- Approximation Algorithms do not guarantee the best solution, but they aim to find a solution that is close to the optimal solution in polynomial time. For example, an approximation algorithm for TSP might find a tour that is at most twice as long as the shortest tour, in polynomial time.
- Approximation Algorithms are measured by their approximation ratio, which is the ratio between the cost of the solution found by the algorithm and the cost of the optimal solution. For example, an approximation algorithm for TSP that has an approximation ratio of 2 means that the tour found by the algorithm is at most twice as long as the shortest tour. The lower the approximation ratio, the better the algorithm.
- Approximation Algorithms are useful because they provide a trade-off between quality and efficiency. They can find good solutions in reasonable time, when finding the optimal solution is intractable. For example, an approximation algorithm for TSP that has an approximation ratio of 2 might be preferable to an exact algorithm that takes exponential time, especially when the number of cities is large.

## Examples of NP-Complete Problems and Approximation Algorithms

- Traveling Salesman Problem (TSP): Given a set of cities and the distances between them, find the shortest tour that visits every city exactly once and returns to the starting city.
  - NP-Complete: It is in NP, because given a tour, we can verify that it visits every city exactly once and returns to the starting city in polynomial time. It is NP-hard, because we can reduce any NP problem to it using a polynomial time transformation.
  - Approximation Algorithm: One possible approximation algorithm for TSP is the following:
    - Start from any city and choose the nearest unvisited city as the next city to visit. Repeat this until all cities are visited, and then return to the starting city. This is called the nearest neighbor heuristic.
    - The approximation ratio of this algorithm is at most 2, meaning that the tour found by the algorithm is at most twice as long as the shortest tour. This can be proved using the triangle inequality, which states that for any three cities A, B, and C, the distance from A to B plus the distance from B to C is greater than or equal to the distance from A to C.
- Graph Coloring: Given a graph and a number k, decide whether the graph can be colored with k colors, such that no two adjacent vertices have the same color.
  - NP-Complete: It is in NP, because given a coloring, we can verify that it uses k colors and no two adjacent vertices have the same color in polynomial time. It is NP-hard, because we can reduce any NP problem to it using a polynomial time transformation