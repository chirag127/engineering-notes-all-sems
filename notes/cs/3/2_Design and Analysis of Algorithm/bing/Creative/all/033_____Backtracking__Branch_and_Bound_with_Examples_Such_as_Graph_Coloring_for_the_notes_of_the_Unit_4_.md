# Backtracking, Branch and Bound with Examples Such as Graph Coloring

Backtracking and branch and bound are two techniques for solving optimization problems that involve searching a finite set of possible solutions. Both techniques use a recursive approach to explore the solution space in a systematic way, but they differ in how they prune the search tree and how they determine the optimal solution.

## Backtracking

Backtracking is a technique that tries to find a feasible solution to a problem by incrementally building a partial solution and then backtracking (undoing) the last decision if it leads to a dead end. Backtracking is often used for solving constraint satisfaction problems, such as sudoku, crossword puzzles, n-queens problem, etc.

The general algorithm for backtracking is as follows:

- Start with an empty partial solution.
- Choose a decision point and try all possible choices for it.
- For each choice, check if it is consistent with the constraints of the problem. If yes, add it to the partial solution and recursively explore the remaining decision points. If no, discard it and try another choice.
- If all decision points are explored and a feasible solution is found, return it. Otherwise, backtrack to the previous decision point and try another choice.
- If no feasible solution is found after trying all possible choices at all decision points, return failure.

The main advantage of backtracking is that it can find all possible solutions to a problem, or prove that none exists. The main disadvantage is that it can be very inefficient, as it may explore a large number of suboptimal or infeasible solutions before finding a good one or giving up.

## Branch and Bound

Branch and bound is a technique that tries to find an optimal solution to a problem by maintaining a lower bound and an upper bound on the objective function value. Branch and bound is often used for solving combinatorial optimization problems, such as travelling salesman problem, knapsack problem, graph coloring problem, etc.

The general algorithm for branch and bound is as follows:

- Start with an empty partial solution and an initial lower bound and upper bound on the objective function value.
- Choose a branching variable and split the solution space into two or more subproblems based on the possible values of the variable.
- For each subproblem, calculate a lower bound and an upper bound on the objective function value using some heuristic or relaxation method. If the lower bound is greater than or equal to the current upper bound, prune the subproblem as it cannot lead to a better solution. If the upper bound is less than the current upper bound, update the upper bound and the best solution found so far. If the lower bound is equal to the upper bound, the subproblem is solved optimally and no further branching is needed.
- Recursively explore the remaining subproblems using the same procedure, until all subproblems are either pruned or solved optimally.
- Return the best solution found or report that the problem is infeasible.

The main advantage of branch and bound is that it can find the optimal solution to a problem, or prove that none exists. The main disadvantage is that it can be very memory-intensive, as it may need to store a large number of subproblems in a queue or a stack.

## Graph Coloring Problem

Graph coloring is a problem of assigning colors to the vertices of a graph such that no two adjacent vertices have the same color. The minimum number of colors needed to color a graph is called its chromatic number. Graph coloring has applications in scheduling, map coloring, register allocation, etc.

Graph coloring can be solved using both backtracking and branch and bound techniques. The following are some examples of how to apply these techniques to the graph coloring problem.

### Backtracking for Graph Coloring

One way to use backtracking for graph coloring is to assign colors to the vertices one by one, starting from an arbitrary vertex. For each vertex, try all possible colors that are not already used by its adjacent vertices. If a color is consistent, add it to the partial solution and recursively explore the next vertex. If no color is consistent, backtrack to the previous vertex and try another color. If all vertices are colored, return the solution. Otherwise, return failure.

The pseudocode for this algorithm is as follows:

```python
# Input: A graph G with n vertices and m colors
# Output: A coloring of G with m colors or failure

def backtrack(G, n, m):
  # Initialize an array to store the colors of the vertices
  colors = [0] * n
  
  # Start from the first vertex
  if backtrack_helper(G, n, m, colors, 0):
    # If a solution is found,