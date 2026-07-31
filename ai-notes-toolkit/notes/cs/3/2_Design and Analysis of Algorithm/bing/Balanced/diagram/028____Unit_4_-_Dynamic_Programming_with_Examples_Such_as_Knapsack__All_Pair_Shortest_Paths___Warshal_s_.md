## Unit 4 - Dynamic Programming with Examples Such as Knapsack. All Pair Shortest Paths – Warshal’s and Floyd’s Algorithms, Resource Allocation Problem. Backtracking, Branch and Bound with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

### Dynamic Programming
- Dynamic programming is a technique for solving optimization problems that have overlapping subproblems and optimal substructure.
- Overlapping subproblems means that the same subproblem is solved repeatedly, and optimal substructure means that the optimal solution of a problem can be obtained from the optimal solutions of its subproblems.
- Dynamic programming can be applied to problems that can be divided into stages, where each stage has a set of states and decisions. The goal is to find an optimal sequence of decisions that leads to the optimal final state.
- Dynamic programming can be implemented using two approaches: top-down and bottom-up. Top-down approach starts from the original problem and recursively breaks it down into smaller subproblems, until the base cases are reached. Bottom-up approach starts from the base cases and iteratively builds up the solution for larger subproblems, until the original problem is solved.
- Dynamic programming can reduce the time complexity of solving a problem from exponential to polynomial, by avoiding recomputation of subproblems and storing the intermediate results in a table or an array.

### Knapsack Problem
- Knapsack problem is an example of a dynamic programming problem. It is also known as 0-1 knapsack problem, because each item can be either included or excluded from the knapsack.
- The problem is to find the maximum value of items that can be packed into a knapsack of a given capacity, without exceeding the weight limit.
- The problem can be formulated as follows:

  - Let n be the number of items, and W be the capacity of the knapsack.
  - Let w[i] and v[i] be the weight and value of the i-th item, for i = 1, 2, ..., n.
  - Let x[i] be a binary variable that indicates whether the i-th item is included in the knapsack or not, for i = 1, 2, ..., n.
  - The objective is to maximize the total value of the items in the knapsack, given by:

    - `sum(i = 1 to n) x[i] * v[i]`

  - The constraint is to not exceed the weight limit of the knapsack, given by:

    - `sum(i = 1 to n) x[i] * w[i] <= W`

- The problem can be solved using dynamic programming as follows:

  - Define a function `f(i, j)` that returns the maximum value of items that can be packed into a knapsack of capacity j, using only the first i items, for i = 0, 1, ..., n and j = 0, 1, ..., W.
  - The base cases are:

    - `f(0, j) = 0` for all j, because no items can be packed into an empty knapsack.
    - `f(i, 0) = 0` for all i, because no items can be packed into a knapsack of zero capacity.

  - The recursive relation is:

    - `f(i, j) = max(f(i - 1, j), f(i - 1, j - w[i]) + v[i])` for all i > 0 and j > 0, because the optimal solution for a knapsack of capacity j, using the first i items, is either to exclude the i-th item and use the optimal solution for a knapsack of capacity j, using the first i - 1 items, or to include the i-th item and use the optimal solution for a knapsack of capacity j - w[i], using the first i - 1 items.

  - The final solution is given by `f(n, W)`, which is the maximum value of items that can be packed into a knapsack of capacity W, using all n items.
  - The optimal subset of items can be traced back by checking the values of `f(i, j)` and `x[i]` in the table or array.

- The time complexity of this algorithm is O(nW), where n is the number of items and W is the capacity of the knapsack. The space complexity is also O(nW), because a table or an array of size n x W is used to store the intermediate results.

### All Pair Shortest Paths – Warshal’s and Floyd’s Algorithms
- All pair shortest paths problem is another example of