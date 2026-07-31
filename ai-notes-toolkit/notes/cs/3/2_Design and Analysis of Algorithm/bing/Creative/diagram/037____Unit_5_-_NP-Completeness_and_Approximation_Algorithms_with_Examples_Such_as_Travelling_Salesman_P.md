Hello, I am Sydney, your AI assistant. I can help you with your query. Here is the content I have generated for you in markdown format:

## Unit 5 - NP-Completeness and Approximation Algorithms with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

### NP-Completeness

- NP-Completeness is a concept that deals with the complexity of decision problems, which are problems that have a yes or no answer.
- A problem is in the class P if there is a polynomial time algorithm that can solve it, i.e., an algorithm that runs in time O(n^k) for some constant k, where n is the size of the input.
- A problem is in the class NP if there is a polynomial time algorithm that can verify a given solution, i.e., an algorithm that can check in time O(n^k) whether a given candidate answer is correct or not.
- A problem is NP-complete if it is in NP and every other problem in NP can be reduced to it in polynomial time, i.e., there is a polynomial time algorithm that can transform any instance of any NP problem into an equivalent instance of the NP-complete problem.
- NP-complete problems are the hardest problems in NP, and they are believed to be not solvable in polynomial time, unless P = NP, which is a major open question in computer science.
- Some examples of NP-complete problems are:

  - Travelling Salesman Problem (TSP): Given a set of cities and the distances between them, find the shortest tour that visits each city exactly once and returns to the starting point.
  - Graph Coloring: Given a graph and a number k, determine whether the vertices of the graph can be colored with k colors such that no two adjacent vertices have the same color.
  - n-Queen Problem: Given a chessboard of size n x n, place n queens on the board such that no two queens attack each other, i.e., no two queens share the same row, column, or diagonal.
  - Hamiltonian Cycle: Given a graph, determine whether there is a cycle that visits each vertex exactly once and returns to the starting point.
  - Sum of Subsets: Given a set of positive integers and a target sum, determine whether there is a subset of the set that adds up to the target sum.

### Approximation Algorithms

- Approximation Algorithms are a way of dealing with NP-completeness for optimization problems, which are problems that seek to find the best solution among many possible solutions, according to some objective function.
- Approximation Algorithms do not guarantee the optimal solution, but they aim to find a solution that is close to the optimal one in polynomial time, and provide a measure of how close the solution is.
- The measure of closeness is usually given by the approximation ratio, which is the ratio between the value of the solution found by the algorithm and the value of the optimal solution. The smaller the ratio, the better the approximation.
- For minimization problems, the approximation ratio is defined as:

  - `ratio = (value of algorithm solution) / (value of optimal solution)`

- For maximization problems, the approximation ratio is defined as:

  - `ratio = (value of optimal solution) / (value of algorithm solution)`

- Some examples of approximation algorithms are:

  - TSP: There is a 2-approximation algorithm that uses a minimum spanning tree to construct a tour, i.e., the length of the tour is at most twice the length of the optimal tour.
  - Graph Coloring: There is a (Δ + 1)-approximation algorithm that uses a greedy strategy to color the vertices, where Δ is the maximum degree of the graph, i.e., the number of colors used is at most Δ + 1, which is the worst case scenario.
  - n-Queen Problem: There is no known polynomial time approximation algorithm for this problem, as it is an NP-complete decision problem, not an optimization problem.
  - Hamiltonian Cycle: There is no known polynomial time approximation algorithm for this problem, unless P = NP, as it is an NP-complete decision problem, not an optimization problem.
  - Sum of Subsets: There is a (1/2)-approximation algorithm that uses a greedy strategy to select the elements of the subset, i.e., the sum of the subset is at least half of the target sum.