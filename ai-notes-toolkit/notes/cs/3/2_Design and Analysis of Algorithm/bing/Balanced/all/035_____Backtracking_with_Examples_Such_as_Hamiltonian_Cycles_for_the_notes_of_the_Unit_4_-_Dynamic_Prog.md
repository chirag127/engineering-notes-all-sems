# Backtracking with Examples Such as Hamiltonian Cycles

- Backtracking is a class of algorithms for finding solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution.
- The backtracking algorithm enumerates a set of partial candidates that, in principle, could be completed in various ways to give all the possible solutions to the given problem. The completion is done incrementally, by a sequence of candidate extension steps.
- Backtracking can be viewed as a depth-first search of a state space tree, where each node represents a partial candidate, and the branches are the possible extensions of the candidate. The algorithm traverses the tree by exploring one branch at a time until a solution is found or a dead end is reached .
- The algorithm can be implemented using recursion or iteration. A recursive implementation typically uses a procedure that takes a partial candidate as a parameter and performs the following steps:
  - If the candidate is a solution, output it or store it in a list.
  - If the candidate is not a solution, but can be extended, generate the possible extensions and recursively call the procedure for each extension.
  - If the candidate is not a solution and cannot be extended, return or backtrack to the previous level.
- A common way to implement backtracking iteratively is to use a stack to store the partial candidates and the possible extensions at each level. The algorithm pops a candidate from the stack, checks if it is a solution or can be extended, and pushes the extensions back to the stack. The algorithm terminates when the stack is empty or a solution is found.
- Backtracking is an important tool for solving constraint satisfaction problems, such as crosswords, verbal arithmetic, Sudoku, and many other puzzles. It is often the most convenient technique for parsing, for the knapsack problem and other combinatorial optimization problems.
- However, backtracking can be very inefficient, as it can generate a lot of candidates that are eventually rejected. The worst-case time complexity of backtracking is exponential in the size of the problem, and the space complexity is linear in the depth of the recursion.
- To improve the efficiency of backtracking, some techniques can be applied, such as pruning, ordering, caching, and heuristics. Pruning is the process of discarding candidates that are guaranteed to be invalid or suboptimal, based on some criteria or constraints. Ordering is the process of choosing the order of generating and exploring the candidates, based on some criteria or heuristics, to reduce the number of backtracks. Caching is the process of storing the results of previously computed subproblems, to avoid recomputing them. Heuristics are rules of thumb that guide the search towards promising candidates, based on some domain knowledge or experience.
- One example of a problem that can be solved by backtracking is the Hamiltonian cycle problem. A Hamiltonian cycle is a cycle in an undirected graph that visits each vertex exactly once and returns to the starting vertex. The problem is to determine whether a given graph has a Hamiltonian cycle, and if so, to find one or all of them.
- A possible backtracking algorithm for the Hamiltonian cycle problem is as follows:
  - Start from any vertex and mark it as visited.
  - For each adjacent vertex that is not visited, add it to the cycle and recursively check if the cycle can be extended from that vertex.
  - If the cycle cannot be extended, remove the last vertex from the cycle and backtrack to the previous vertex.
  - If the cycle can be extended and the last vertex is adjacent to the first vertex, output the cycle or store it in a list.
  - Return true if a cycle is found, or false otherwise.
- The following is a pseudocode implementation of the algorithm:

```python
# Input: a graph G and a starting vertex v
# Output: true if G has a Hamiltonian cycle, or false otherwise
# Side effect: print or store the cycle if found
def hamiltonian_cycle(G, v):
  # Initialize an empty list to store the cycle
  cycle = []
  # Initialize a set to store the visited vertices
  visited = set()
  # Call the recursive helper function
  return hamiltonian_cycle_helper(G, v, cycle, visited)

# Input: a graph G, a current

```
