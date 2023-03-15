### Dynamic Programming with Examples Such as All Pair Shortest Paths – Warshal’s and Floyd’s Algorithms

- Dynamic programming is a technique for solving optimization problems by breaking them down into smaller subproblems, and storing the solutions of the subproblems in a table to avoid recomputation.
- Dynamic programming can be applied to problems that have two properties: optimal substructure and overlapping subproblems.
- Optimal substructure means that the optimal solution of a problem can be obtained by using the optimal solutions of its subproblems.
- Overlapping subproblems means that the same subproblems are encountered and solved many times during the computation.
- One example of a problem that can be solved by dynamic programming is the all pair shortest path problem, which is to find the shortest distance between every pair of vertices in a weighted graph.
- There are two algorithms that can solve the all pair shortest path problem using dynamic programming: Warshal's algorithm and Floyd's algorithm.
- Warshal's algorithm is based on the idea of transitive closure, which is the set of all pairs of vertices that are reachable from each other in a graph.
- Warshal's algorithm works by initializing a matrix that contains the adjacency matrix of the graph, and then updating the matrix by adding intermediate vertices one by one, until all vertices are considered.
- Warshal's algorithm can be used to find the shortest paths in a graph that has only binary weights (0 or 1), or to find the reachability matrix of a graph.
- Floyd's algorithm is based on the idea of relaxation, which is the process of improving an estimate of the shortest distance between two vertices by using a third vertex as a intermediate point.
- Floyd's algorithm works by initializing a matrix that contains the weight matrix of the graph, and then updating the matrix by relaxing the edges one by one, until all edges are considered.
- Floyd's algorithm can be used to find the shortest paths in a graph that has any weights, positive or negative, as long as there are no negative cycles in the graph.
- Both Warshal's and Floyd's algorithms have a time complexity of O(n^3), where n is the number of vertices in the graph, and a space complexity of O(n^2), where n is the number of vertices in the graph.