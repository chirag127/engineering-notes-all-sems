# Dynamic Programming with Examples Such as All Pair Shortest Paths – Warshal’s and Floyd’s Algorithms

Dynamic programming is a method for solving complex problems by breaking them down into smaller subproblems. It is applicable to problems that exhibit the properties of overlapping subproblems and optimal substructure. When a problem can be divided into subproblems that are smaller instances of the same problem, and the solution to the problem can be constructed from the solutions to the subproblems, dynamic programming can be used to find the optimal solution.

One example of a problem that can be solved using dynamic programming is the all-pair shortest paths problem. This problem involves finding the shortest path between all pairs of vertices in a weighted graph. Two algorithms that can be used to solve this problem are Warshal’s algorithm and Floyd’s algorithm.

Warshal’s algorithm is an iterative algorithm that computes the transitive closure of a graph. It uses a matrix to represent the graph, with the element at the ith row and jth column representing the presence or absence of an edge between the ith and jth vertices. The algorithm iteratively updates the matrix to include paths of increasing length, until the matrix represents the transitive closure of the graph.

Floyd’s algorithm is another iterative algorithm that computes the shortest paths between all pairs of vertices in a weighted graph. It uses a matrix to represent the graph, with the element at the ith row and jth column representing the weight of the edge between the ith and jth vertices. The algorithm iteratively updates the matrix to include paths of increasing length, until the matrix represents the shortest paths between all pairs of vertices.

Both Warshal’s and Floyd’s algorithms have a time complexity of O(n^3), where n is the number of vertices in the graph.

Other examples of problems that can be solved using dynamic programming include the knapsack problem, the resource allocation problem, and the traveling salesman problem. These problems can be solved by breaking them down into smaller subproblems and using dynamic programming to find the optimal solution.

Backtracking and branch and bound are two other techniques that can be used to solve complex problems. Backtracking involves exploring all possible solutions to a problem and discarding solutions that do not meet certain criteria. Branch and bound involves systematically searching for the optimal solution to a problem by maintaining an upper and lower bound on the solution and pruning branches of the search tree that cannot lead to an optimal solution.

Examples of problems that can be solved using backtracking and branch and bound include the graph coloring problem, the n-queen problem, the Hamiltonian cycles problem, and the sum of subsets problem. These problems can be solved by systematically exploring the solution space and using backtracking or branch and bound to find the optimal solution.