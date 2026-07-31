### NP-Completeness and Approximation Algorithms with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

- NP-Completeness is a concept that relates to the complexity of decision problems, which are problems that have a yes or no answer. A problem is NP if it can be verified in polynomial time, meaning that given a solution, we can check if it is correct in a number of steps that is proportional to some power of the input size. A problem is NP-complete if it is NP and also every other NP problem can be reduced to it in polynomial time, meaning that we can transform any instance of any NP problem into an instance of the NP-complete problem such that the answer is the same. NP-complete problems are believed to be the hardest problems in NP, and no polynomial time algorithm is known for any of them. Examples of NP-complete problems are Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets .

- Approximation Algorithms are a way of dealing with NP-completeness for optimization problems, which are problems that seek to find the best solution among many possible ones according to some objective function. An approximation algorithm does not guarantee the best solution, but rather a solution that is close to the optimal one in some sense. The goal of an approximation algorithm is to come as close as possible to the optimal solution in polynomial time, which is at most proportional to some power of the input size. The quality of an approximation algorithm is measured by its approximation ratio, which is the ratio between the value of the solution found by the algorithm and the value of the optimal solution. The smaller the approximation ratio, the better the algorithm. Examples of approximation algorithms are the 2-approximation algorithm for Vertex Cover, the 7/8-approximation algorithm for Max 3-SAT, and the Christofides algorithm for Travelling Salesman Problem   .

- Travelling Salesman Problem (TSP) is an optimization problem that asks to find the shortest tour that visits a given set of cities and returns to the starting point. The tour must visit each city exactly once. TSP is NP-complete, meaning that no polynomial time algorithm is known to solve it exactly. However, there are approximation algorithms that can find near-optimal tours in polynomial time. One such algorithm is the Christofides algorithm, which works as follows:

  - Find a minimum spanning tree of the given graph, which is a tree that connects all the vertices with the minimum total edge weight.
  - Find a minimum weight perfect matching of the odd-degree vertices in the tree, which is a set of edges that pairs up the vertices with odd degree such that the total edge weight is minimized.
  - Combine the tree and the matching to form an Eulerian graph, which is a graph that has an Eulerian circuit, which is a cycle that visits every edge exactly once.
  - Find an Eulerian circuit of the Eulerian graph, and shortcut it to obtain a Hamiltonian cycle, which is a cycle that visits every vertex exactly once.
  - Return the Hamiltonian cycle as the tour.

  The Christofides algorithm has an approximation ratio of 3/2, meaning that the tour found by the algorithm is at most 3/2 times longer than the optimal tour.

- Graph Coloring is an optimization problem that asks to assign colors to the vertices of a given graph such that no two adjacent vertices have the same color, and the number of colors used is minimized. Graph Coloring is NP-complete, meaning that no polynomial time algorithm is known to find the minimum number of colors needed for any graph. However, there are approximation algorithms that can find near-optimal colorings in polynomial time. One such algorithm is the greedy algorithm, which works as follows:

  - Order the vertices of the graph in some arbitrary way.
  - For each vertex in the order, assign it the smallest available color that does not conflict with any of its neighbors.
  - Return the coloring obtained.

  The greedy algorithm has an approximation ratio of O(log n), meaning that the number of colors used by the algorithm is at most proportional to the logarithm of the number of vertices in the graph.

- n-Queen Problem is a decision problem that asks if it is possible to place n queens on an n x n chessboard such that no two queens attack each other, meaning that no two queens share the same row, column, or diagonal.