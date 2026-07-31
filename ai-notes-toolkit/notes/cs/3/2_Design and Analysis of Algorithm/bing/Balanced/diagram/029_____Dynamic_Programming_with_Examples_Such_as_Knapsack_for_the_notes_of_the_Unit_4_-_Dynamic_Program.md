# Dynamic Programming with Examples Such as Knapsack

- Dynamic programming is a technique for solving problems that have overlapping subproblems and optimal substructure.
- Overlapping subproblems means that the same subproblem is solved repeatedly, which leads to wasteful computation.
- Optimal substructure means that the optimal solution of a problem can be obtained by combining the optimal solutions of its subproblems.
- Dynamic programming avoids repeated computation by storing the results of subproblems in a table and reusing them when needed.
- Dynamic programming can be applied to problems that have the following characteristics:
  - The problem can be divided into smaller subproblems of the same type.
  - The subproblems are independent of each other, i.e., solving one subproblem does not affect the solution of another subproblem.
  - There is an optimal way of combining the solutions of the subproblems to obtain the solution of the original problem.

## Knapsack Problem

- The knapsack problem is a classic example of a problem that can be solved using dynamic programming.
- The problem statement is as follows:
  - Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight does not exceed a given limit and the total value is as large as possible.
- There are two variants of the knapsack problem: the 0/1 knapsack problem and the fractional knapsack problem.
- In the 0/1 knapsack problem, each item can be either included or excluded from the collection, i.e., the decision is binary.
- In the fractional knapsack problem, each item can be partially included in the collection, i.e., the decision is fractional.

### 0/1 Knapsack Problem using Dynamic Programming

- To solve the 0/1 knapsack problem using dynamic programming, we use a two-dimensional table to store the optimal value for each subproblem.
- The table has n rows and M columns, where n is the number of items and M is the capacity of the knapsack.
- The entry in the i-th row and j-th column of the table, denoted by V[i][j], represents the maximum value that can be obtained by using the first i items and a knapsack of capacity j.
- The table can be filled up using the following recurrence relation:

  - V[i][j] = max(V[i-1][j], V[i-1][j-w[i]] + v[i]), if j >= w[i]
  - V[i][j] = V[i-1][j], otherwise

- The first case corresponds to including the i-th item in the collection, and the second case corresponds to excluding it.
- The base cases are:

  - V[0][j] = 0, for all j
  - V[i][0] = 0, for all i

- The optimal value of the problem is given by V[n][M], which is the bottom-right entry of the table.
- To find the optimal subset of items, we can trace back the table from V[n][M] and check which items were included or excluded at each step.

#### Example

- Consider the following 0/1 knapsack problem:

  - Number of items n = 4
  - Knapsack capacity M = 5
  - Weights (w1, w2, w3, w4) = (2, 3, 4, 5)
  - Values (v1, v2, v3, v4) = (3, 4, 5, 6)

- The table for this problem is shown below:

| i\j | 0 | 1 | 2 | 3 | 4 | 5 |
| --- | - | - | - | - | - | - |
| 0   | 0 | 0 | 0 | 0 | 0 | 0 |
| 1   | 0 | 0 | 3 | 3 | 3 | 3 |
| 2   | 0 | 0 | 3 | 4 | 4 | 7 |
| 3   | 0 | 0 | 3 | 4 | 5 | 7 |
| 4   | 0 | 0 | 3 | 4 | 5 | 7 |

- The optimal value is V[4][5] = 7, which means that the maximum value that can be obtained by using the first