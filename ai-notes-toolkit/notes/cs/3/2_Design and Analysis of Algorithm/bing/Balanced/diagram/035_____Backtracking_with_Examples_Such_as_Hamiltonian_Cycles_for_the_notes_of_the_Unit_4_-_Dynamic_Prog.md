### Backtracking with Examples Such as Hamiltonian Cycles

- Backtracking is a general algorithmic technique that considers searching every possible combination in order to solve a computational problem.
- Backtracking works by recursively trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time (by time, here, is referred to the time elapsed till reaching any level of the search tree).
- Backtracking can be applied to solve problems that involve finding all (or some) of the solutions to a problem, such as generating permutations, combinations, or subsets of a set of elements; solving puzzles such as Sudoku, N-Queens, or crossword; and finding an optimal solution for optimization problems such as the knapsack problem or the traveling salesman problem.
- Backtracking is often implemented using recursion, where the recursive calls correspond to exploring the subproblems of the original problem, and the base cases correspond to reaching a leaf node in the search tree, where a solution is either found or rejected.
- Backtracking can be optimized by using some heuristics or pruning techniques to avoid exploring parts of the search space that are guaranteed to be irrelevant or suboptimal.

#### Hamiltonian Cycles

- A Hamiltonian cycle (or Hamiltonian circuit) is a cycle in an undirected graph that visits each vertex exactly once and also returns to the starting vertex.
- Finding a Hamiltonian cycle in a given graph is an NP-complete problem, meaning that there is no known efficient algorithm that can solve it in polynomial time for all possible inputs.
- However, backtracking can be used to find a Hamiltonian cycle (if it exists) in a given graph, by trying to extend a partial solution (a path that visits some of the vertices) until it becomes a cycle that covers all the vertices.
- The algorithm works as follows:

  - Start from any vertex and mark it as visited.
  - For each adjacent vertex that is not visited, add it to the path and recursively check if this path can be extended to a Hamiltonian cycle.
  - If the path cannot be extended, remove the last vertex from the path and backtrack to the previous vertex.
  - If the path can be extended to a cycle that visits all the vertices, return the path as a solution.
  - If all the adjacent vertices are visited and the path is not a cycle, return false.

- The algorithm can be implemented using a boolean array to keep track of the visited vertices, and a list or an array to store the path.
- The algorithm can be optimized by using some heuristics, such as ordering the vertices by their degree (the number of adjacent vertices) or using a bitset instead of a boolean array to reduce the space complexity.