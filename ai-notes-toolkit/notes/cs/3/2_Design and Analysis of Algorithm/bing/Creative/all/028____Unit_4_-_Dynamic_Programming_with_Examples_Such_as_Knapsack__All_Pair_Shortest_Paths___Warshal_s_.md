## Unit 4 - Dynamic Programming with Examples Such as Knapsack. All Pair Shortest Paths – Warshal’s and Floyd’s Algorithms, Resource Allocation Problem. Backtracking, Branch and Bound with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

- Dynamic programming is a technique for solving optimization problems that have overlapping subproblems and optimal substructure. It works by breaking down the problem into smaller subproblems, solving them once and storing their solutions in a table, and then using the table to construct the optimal solution for the original problem.
- Knapsack problem is an example of dynamic programming. It is a problem of packing a set of items with different weights and values into a knapsack with a limited capacity, such that the total value of the items in the knapsack is maximized. The dynamic programming solution for this problem is to define a function `f(i, w)` that returns the maximum value that can be obtained by packing items from `1` to `i` into a knapsack with capacity `w`. The function can be computed recursively as follows:

  - Base case: `f(0, w) = 0` for any `w`.
  - Recursive case: `f(i, w) = max(f(i-1, w), f(i-1, w-wi) + vi)` for any `i` and `w`, where `wi` and `vi` are the weight and value of item `i`, respectively. The first term in the max function represents the case of not including item `i` in the knapsack, and the second term represents the case of including item `i` in the knapsack, if possible.
  - The optimal value for the problem is `f(n, W)`, where `n` is the number of items and `W` is the capacity of the knapsack.

- All pair shortest paths problem is another example of dynamic programming. It is a problem of finding the shortest distance between every pair of vertices in a weighted graph. There are two algorithms for solving this problem using dynamic programming: Warshal's algorithm and Floyd's algorithm. Both algorithms use a matrix `D` to store the shortest distances between vertices, and update the matrix iteratively using the following formula:

  - `D(k)[i][j] = min(D(k-1)[i][j], D(k-1)[i][k] + D(k-1)[k][j])` for any `i`, `j`, and `k`, where `D(k)[i][j]` is the shortest distance between vertices `i` and `j` using only vertices from `1` to `k` as intermediate vertices.
  - The difference between Warshal's algorithm and Floyd's algorithm is the order of updating the matrix. Warshal's algorithm updates the matrix row by row, while Floyd's algorithm updates the matrix in a diagonal fashion. Both algorithms have a time complexity of `O(n^3)`, where `n` is the number of vertices in the graph.

- Resource allocation problem is a problem of allocating a limited amount of resources among a number of competing activities, such that the total profit or benefit is maximized. The dynamic programming solution for this problem is to define a function `g(i, r)` that returns the maximum profit that can be obtained by allocating `r` units of resources to activities from `1` to `i`. The function can be computed recursively as follows:

  - Base case: `g(0, r) = 0` for any `r`.
  - Recursive case: `g(i, r) = max(g(i-1, r), g(i-1, r-ri) + pi)` for any `i` and `r`, where `ri` and `pi` are the resource requirement and profit of activity `i`, respectively. The first term in the max function represents the case of not allocating resources to activity `i`, and the second term represents the case of allocating resources to activity `i`, if possible.
  - The optimal value for the problem is `g(m, R)`, where `m` is the number of activities and `R` is the total amount of resources available.

- Backtracking is a technique for solving problems that involve searching for a solution among a large number of possibilities. It works by exploring the solution space in a depth-first manner, and pruning the branches that do not lead to a feasible or optimal solution. Backtracking can be implemented using recursion or a stack.
- Travelling salesman problem is an example of backtracking. It is a problem of finding the shortest tour that visits every city in a given set of