# NP-Completeness and Approximation Algorithms

- NP-Completeness is a concept that deals with the complexity of decision problems, which are problems that have a yes or no answer.
- A decision problem is NP if it can be verified in polynomial time, given a certificate or a witness for a yes answer.
- A decision problem is NP-Complete if it is NP and every other NP problem can be reduced to it in polynomial time, using a transformation that preserves the yes or no answer.
- NP-Complete problems are believed to be intractable, meaning that there is no polynomial time algorithm that can solve them, unless P=NP, which is a major open question in computer science.
- Examples of NP-Complete problems are: 
  - Travelling Salesman Problem (TSP): Given a set of cities and distances between them, find the shortest tour that visits each city exactly once and returns to the starting point.
  - Graph Coloring: Given a graph and a number k, determine if the graph can be colored with k colors such that no two adjacent vertices have the same color.
  - n-Queen Problem: Given a chessboard of size n x n, place n queens on the board such that no two queens attack each other.
  - Hamiltonian Cycle: Given a graph, find a cycle that visits each vertex exactly once and returns to the starting point.
  - Sum of Subsets: Given a set of positive integers and a target value, determine if there is a subset of the set that sums up to the target value.

- Approximation Algorithms are a way of dealing with NP-Completeness for optimization problems, which are problems that seek to find the best solution among many possible solutions, according to some objective function.
- Approximation Algorithms do not guarantee the optimal solution, but they aim to find a solution that is close to the optimal solution in polynomial time, with some provable bound on the quality of the solution.
- The quality of an approximation algorithm is measured by the approximation ratio, which is the ratio between the value of the solution found by the algorithm and the value of the optimal solution, for the worst-case input.
- The approximation ratio depends on whether the optimization problem is a minimization problem or a maximization problem. For minimization problems, the ratio is always greater than or equal to 1, and for maximization problems, the ratio is always less than or equal to 1.
- Examples of Approximation Algorithms are:
  - TSP: A 2-approximation algorithm is to find a minimum spanning tree of the graph, and then traverse the tree in a preorder fashion, skipping any visited vertices. The length of the tour is at most twice the length of the optimal tour .
  - Graph Coloring: A simple approximation algorithm is to assign colors to the vertices in any order, using the smallest available color for each vertex. The number of colors used is at most one more than the maximum degree of the graph, which is a lower bound for the optimal number of colors .
  - n-Queen Problem: A heuristic algorithm is to place the queens one by one, starting from the first row, and choosing the column that has the least number of conflicts with the previous queens. If there is no such column, backtrack and try a different column for the previous queen. The algorithm may or may not find a solution, depending on the size of the board and the initial choices.
  - Hamiltonian Cycle: A 2-approximation algorithm is to find a minimum spanning tree of the graph, and then double each edge of the tree. The resulting graph is Eulerian, meaning that it has a cycle that visits each edge exactly once. By skipping any visited vertices, the cycle becomes a Hamiltonian cycle. The length of the cycle is at most twice the length of the optimal cycle .
  - Sum of Subsets: A greedy algorithm is to sort the set in decreasing order, and then add the elements to the subset one by one, as long as the sum does not exceed the target value. The algorithm may or may not find a solution, depending on the set and the target value. The sum of the subset is at least half of the optimal sum .