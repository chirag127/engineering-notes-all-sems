# Backtracking, Branch and Bound with Examples Such as Travelling Salesman Problem

Backtracking and branch and bound are two techniques for solving optimization and decision problems that involve searching a large space of possible solutions. They both use a recursive approach to explore the solution space in a systematic way, but they differ in how they prune the search tree and estimate the quality of partial solutions.

## Backtracking

Backtracking is a technique that tries to find all possible solutions to a problem by building a solution incrementally, one component at a time, and backtracking whenever a component of the solution cannot be extended to a complete solution. Backtracking is useful for solving problems that have a finite number of solutions, such as the n-queen problem, the sum of subsets problem, and the graph coloring problem.

The general algorithm for backtracking is as follows:

- Start with an empty solution vector and a set of constraints that define the problem.
- Choose a component of the solution vector and assign a value to it that satisfies the constraints.
- If the solution vector is complete, then print or store the solution and return.
- If the solution vector is not complete, then recursively try to extend the solution vector by choosing another component and assigning a value to it.
- If no value can be assigned to a component without violating the constraints, then backtrack to the previous component and try a different value.

The backtracking algorithm can be implemented using a stack data structure to store the solution vector and the current component. The algorithm can also be modified to stop after finding the first solution, or to find the best solution according to some objective function.

## Branch and Bound

Branch and bound is a technique that tries to find an optimal solution to a problem by exploring a subset of the solution space that contains the optimal solution. Branch and bound is useful for solving problems that have a continuous or discrete solution space, such as the travelling salesman problem, the knapsack problem, and the resource allocation problem.

The general algorithm for branch and bound is as follows:

- Start with an empty solution vector and a set of constraints that define the problem.
- Choose a component of the solution vector and assign a value to it that satisfies the constraints.
- Compute a lower bound and an upper bound for the objective function of the partial solution.
- If the lower bound is equal to the upper bound, then the partial solution is optimal and return it.
- If the lower bound is greater than the current best solution, then prune the branch and backtrack to the previous component.
- If the lower bound is less than the current best solution, then branch into subproblems by choosing another component and assigning different values to it.
- Repeat the above steps until all branches are explored or pruned.

The branch and bound algorithm can be implemented using a priority queue data structure to store the partial solutions and their bounds. The priority queue can be ordered by the lower bound, the upper bound, or a combination of both. The algorithm can also be modified to find all optimal solutions, or to find an approximate solution within a given error tolerance.

## Examples

### Travelling Salesman Problem

The travelling salesman problem (TSP) is a problem of finding the shortest tour that visits a given set of cities exactly once and returns to the starting city. The TSP can be formulated as a graph problem, where the cities are the vertices and the distances between them are the edge weights. The TSP is an NP-hard problem, meaning that there is no known polynomial-time algorithm that can solve it exactly.

One way to solve the TSP using branch and bound is as follows:

- Start with an empty tour and a set of unvisited cities.
- Choose a city and add it to the tour as the starting and ending city.
- Compute a lower bound for the tour length by adding the minimum edge weight incident to each unvisited city and dividing by two. This is known as the 1-tree relaxation of the TSP.
- Compute an upper bound for the tour length by using a heuristic algorithm, such as the nearest neighbor algorithm, to construct a feasible tour from the current city.
- If the lower bound is equal to the upper bound, then the tour is optimal and return it.
- If the lower bound is greater than the current best tour, then prune the branch and backtrack to the previous city.
- If the lower bound is less than the current best tour, then branch into subproblems by choosing another city and adding it to the tour.
- Repeat the above steps until all branches are explored or pruned.

### Graph Coloring

The graph coloring problem is a problem of assigning colors to the vertices of a graph such that no two adjacent vertices have the same