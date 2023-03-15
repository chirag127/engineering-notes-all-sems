### Backtracking with Examples Such as Hamiltonian Cycles

- Backtracking is a general algorithmic technique that considers searching every possible combination in order to solve an optimization problem.
- Backtracking is often implemented recursively by trying to extend a partial solution obtained so far and backtrack (go back) if the extension is not valid or does not lead to a desired solution.
- Backtracking can be applied to problems that require finding all (or some) solutions, such as enumerating permutations, combinations, subsets, or satisfying assignments.
- Backtracking can also be applied to problems that require finding a single solution that satisfies some constraints, such as puzzles, games, or combinatorial optimization problems.
- Backtracking is based on the idea of depth-first search (DFS), where the nodes of a search tree are explored in a LIFO (last-in first-out) order.
- Backtracking differs from DFS in that it abandons a branch of the search tree when it determines that the branch cannot possibly lead to a valid solution. This can save a lot of time and space, especially when the search space is large and the constraints are tight.
- Backtracking can be implemented using a stack to store the nodes of the search tree, or using recursion, which implicitly uses the call stack.
- Backtracking can be optimized by using heuristics, pruning, and memoization to reduce the size of the search space and avoid repeated work.

#### Example: Hamiltonian Cycles

- A Hamiltonian cycle is a cycle in an undirected graph that visits every vertex exactly once and returns to the starting vertex.
- Finding a Hamiltonian cycle in a graph is an NP-complete problem, which means that there is no known polynomial-time algorithm to solve it for all graphs.
- However, backtracking can be used to find a Hamiltonian cycle (if it exists) or determine that none exists in a given graph.
- The idea is to start from any vertex and try to extend a partial path by adding adjacent vertices that are not already in the path, until either a cycle is formed or all vertices are exhausted.
- If a cycle is formed, check if it is a Hamiltonian cycle (i.e., it contains all vertices). If yes, return the cycle as a solution. If no, backtrack and try another extension.
- If all vertices are exhausted, backtrack and try another extension.
- If all possible extensions have been tried and no Hamiltonian cycle is found, return that none exists.

##### Algorithm

- Input: A graph G = (V, E) with n vertices and m edges
- Output: A Hamiltonian cycle in G or a message that none exists

- Choose a starting vertex v and initialize a path P = [v]
- Define a recursive function backtrack(P) that takes a path P as input and returns a Hamiltonian cycle or None
  - If P contains n vertices, check if the last vertex in P is adjacent to the first vertex in P
    - If yes, return P as a Hamiltonian cycle
    - If no, return None
  - For each vertex u that is adjacent to the last vertex in P and not already in P
    - Append u to P and call backtrack(P)
    - If backtrack(P) returns a Hamiltonian cycle, return it
    - Otherwise, remove u from P and continue the loop
  - If the loop ends without returning a Hamiltonian cycle, return None
- Call backtrack(P) and return its result