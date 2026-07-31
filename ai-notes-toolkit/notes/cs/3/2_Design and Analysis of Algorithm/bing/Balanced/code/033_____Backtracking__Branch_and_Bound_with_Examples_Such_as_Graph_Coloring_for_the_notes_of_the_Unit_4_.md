### Backtracking, Branch and Bound with Examples Such as Graph Coloring

Backtracking and branch and bound are two techniques for solving optimization problems that involve searching a large space of possible solutions. Both techniques use a state-space tree to represent the solution space and explore it in a systematic way. However, they differ in how they prune the tree and select the next node to visit.

#### Backtracking

Backtracking is a technique that tries to find a feasible solution by incrementally building a partial solution and then backtracking (undoing) the last decision if it leads to a dead end. Backtracking uses a depth-first search strategy to explore the state-space tree. It applies a bounding function to check whether the current partial solution can be extended to a complete solution or not. If not, it backtracks to the previous node and tries a different option. Backtracking can be used to solve problems that have a yes/no answer, such as whether a given graph can be colored with m colors or not.

An example of backtracking is the graph coloring problem. Given a graph and a number of colors m, the problem is to assign a color to each vertex of the graph such that no two adjacent vertices have the same color. A possible algorithm using backtracking is:

- Start with an empty color assignment (an array of size n, where n is the number of vertices).
- Pick the first vertex and assign it the first color.
- Recursively assign colors to the remaining vertices, starting from the second vertex.
- For each vertex, check if the current color assignment is safe, i.e., no two adjacent vertices have the same color. If yes, proceed to the next vertex. If no, backtrack and try a different color.
- If all vertices are colored, print the color assignment and return true. If no color assignment is possible, return false.

#### Branch and Bound

Branch and bound is a technique that tries to find an optimal solution by exploring only the promising branches of the state-space tree. Branch and bound uses a breadth-first search strategy to explore the state-space tree. It applies a bounding function to estimate the lower and upper bounds of the optimal solution for each node. It then uses these bounds to prune the nodes that cannot lead to a better solution than the current best solution. Branch and bound can be used to solve problems that have a numerical answer, such as finding the minimum cost of traveling through a set of cities.

An example of branch and bound is the traveling salesman problem. Given a set of n cities and the distances between them, the problem is to find the shortest tour that visits each city exactly once and returns to the starting city. A possible algorithm using branch and bound is:

- Start with an empty tour (a list of size n+1, where n is the number of cities).
- Pick the first city as the starting and ending point of the tour.
- Recursively add cities to the tour, starting from the second city.
- For each city, calculate the cost of the current tour and the lower bound of the remaining tour using a heuristic function (such as the minimum spanning tree of the unvisited cities).
- If the cost of the current tour plus the lower bound is less than the current best cost, proceed to the next city. If not, prune the current node and backtrack to the previous city.
- If all cities are visited, update the current best cost and tour if the current tour is better. Return the current best cost and tour.