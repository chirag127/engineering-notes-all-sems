# Dynamic Programming with Examples Such as Knapsack

- Dynamic programming is a technique for solving optimization problems that have overlapping subproblems and optimal substructure.
- Overlapping subproblems means that the same subproblem is solved repeatedly, and optimal substructure means that the optimal solution of a problem can be obtained from the optimal solutions of its subproblems.
- Dynamic programming can be applied to problems that can be divided into stages, where each stage has a set of states and a set of decisions that lead to the next stage.
- Dynamic programming can be implemented using either a top-down approach (with memoization) or a bottom-up approach (with tabulation).
- Dynamic programming can reduce the time complexity of some problems from exponential to polynomial.

## Knapsack Problem

- The knapsack problem is a classic example of a dynamic programming problem.
- The problem statement is as follows: Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight does not exceed a given limit and the total value is as large as possible.
- There are two variants of the knapsack problem: the 0/1 knapsack problem and the fractional knapsack problem.
- In the 0/1 knapsack problem, each item can be either included or excluded from the collection, but not partially.
- In the fractional knapsack problem, each item can be included partially or fully in the collection, depending on the remaining capacity of the knapsack.

### 0/1 Knapsack Problem using Dynamic Programming

- A simple solution for the 0/1 knapsack problem is to consider all subsets of items and calculate the total weight and value of each subset, and then select the subset with the maximum value and the weight within the limit. This solution has an exponential time complexity of O(2^n), where n is the number of items.
- A better solution for the 0/1 knapsack problem is to use dynamic programming, which can reduce the time complexity to O(nM), where n is the number of items and M is the capacity of the knapsack.
- The idea of dynamic programming is to define a table K of size (n+1) x (M+1), where K[i][j] represents the maximum value that can be obtained by using the first i items and a knapsack of capacity j.
- The table K can be filled up using the following recurrence relation:

  - K[i][j] = 0, if i = 0 or j = 0 (base case)
  - K[i][j] = K[i-1][j], if w[i] > j (item i cannot be included)
  - K[i][j] = max(K[i-1][j], v[i] + K[i-1][j-w[i]]), if w[i] <= j (item i can be included or excluded)

- The maximum value of the knapsack problem is given by K[n][M], and the items included in the optimal solution can be traced back by comparing K[i][j] with K[i-1][j] and K[i-1][j-w[i]].

#### Example

- Suppose we have the following 0/1 knapsack problem:

  - Number of items n = 4
  - Knapsack capacity M = 5
  - Weights (w1, w2, w3, w4) = (2, 3, 4, 5)
  - Values (v1, v2, v3, v4) = (3, 4, 5, 6)

- The table K can be filled up as follows:

| i\j | 0 | 1 | 2 | 3 | 4 | 5 |
| --- | - | - | - | - | - | - |
| 0   | 0 | 0 | 0 | 0 | 0 | 0 |
| 1   | 0 | 0 | 3 | 3 | 3 | 3 |
| 2   | 0 | 0 | 3 | 4 | 4 | 7 |
| 3   | 0 | 0 | 3 | 4 | 5 | 7 |
| 4   | 0 | 0 | 3 | 4 | 5 | 7 |

- The maximum value of the knapsack problem is 7, and the items included in