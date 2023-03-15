# Backtracking, Branch and Bound with Examples Such as Graph Coloring

## Backtracking

- Backtracking is a technique to solve problems that involve searching for a feasible solution among a large set of possible candidates.
- Backtracking works by incrementally building a partial solution and checking if it satisfies some constraints. If it does, the algorithm continues to extend the partial solution. If it does not, the algorithm backtracks to a previous state and tries a different option.
- Backtracking can be applied to problems such as Sudoku, N-Queens, Hamiltonian cycle, etc.
- Backtracking is often implemented using recursion, where each recursive call represents a choice point in the search space.
- The advantages of backtracking are that it can find all possible solutions and it can prune the search space by using heuristics or bounds.
- The disadvantages of backtracking are that it can be very time-consuming and memory-intensive, especially for large or complex problems.

## Branch and Bound

- Branch and bound is a technique to solve optimization problems that involve finding the best solution among a large set of possible candidates.
- Branch and bound works by dividing the search space into smaller subproblems (branches) and evaluating a lower or upper bound for each subproblem (bounds). If the bound of a subproblem is worse than the best solution found so far, the subproblem can be discarded (pruned). Otherwise, the subproblem is further explored.
- Branch and bound can be applied to problems such as Travelling Salesman Problem, Knapsack Problem, Sum of Subsets, etc.
- Branch and bound can be implemented using a priority queue, where each subproblem is inserted with a priority based on its bound. The subproblem with the highest priority is extracted and processed first.
- The advantages of branch and bound are that it can find the optimal solution and it can prune the search space by using bounds.
- The disadvantages of branch and bound are that it can be very time-consuming and memory-intensive, especially for large or complex problems or when the bounds are not tight enough.

## Graph Coloring

- Graph coloring is a problem of assigning colors to the vertices of a graph such that no two adjacent vertices have the same color.
- Graph coloring can be used to model various real-world problems such as scheduling, map coloring, register allocation, etc.
- Graph coloring can be solved using both backtracking and branch and bound techniques .
- To solve graph coloring using backtracking, the algorithm follows these steps:

  - Assign a color to a vertex (1 to m)
  - For every assigned color, recursively call the function with the next index and the number of vertices
  - Check if the output color configuration is safe, i.e., check if the adjacent vertices do not have the same color
  - If the conditions are met, print the configuration and break
  - If not, backtrack and try a different color

- To solve graph coloring using branch and bound, the algorithm follows these steps:

  - Initialize a lower bound (LB) and an upper bound (UB) for the minimum number of colors needed
  - Start with the first vertex and assign it the first color
  - For each subsequent vertex, assign it the smallest available color that does not conflict with its adjacent vertices
  - Update the UB as the maximum color used so far
  - If the UB is equal to the LB, return the UB as the optimal solution
  - Otherwise, branch into two subproblems: one where the last vertex is assigned a new color, and one where the last vertex is assigned an existing color
  - For each subproblem, calculate a new LB based on the number of colors used and the degree of the vertices
  - Prune the subproblem if its LB is greater than or equal to the UB
  - Otherwise, explore the subproblem recursively
  - Return the minimum UB among all the subproblems as the optimal solution