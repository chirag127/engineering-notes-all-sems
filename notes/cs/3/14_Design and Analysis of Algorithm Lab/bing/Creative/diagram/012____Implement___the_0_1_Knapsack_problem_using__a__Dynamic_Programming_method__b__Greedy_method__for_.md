## Implement the 0/1 Knapsack problem using (a) Dynamic Programming method (b) Greedy method

The 0/1 Knapsack problem is a combinatorial optimization problem where we are given a set of items, each with a weight and a value, and we have to determine the subset of items to include in a knapsack such that the total weight does not exceed a given capacity and the total value is maximized.

### (a) Dynamic Programming method

Dynamic Programming is a technique that solves a problem by breaking it down into smaller subproblems and storing the optimal solutions of the subproblems in a table. The main idea is to avoid recomputing the same subproblems over and over again.

To solve the 0/1 Knapsack problem using Dynamic Programming, we can use the following steps:

- Define a 2D array `dp[n+1][W+1]`, where `n` is the number of items and `W` is the knapsack capacity. Each cell `dp[i][j]` will store the maximum value that can be obtained by using the first `i` items and a knapsack of capacity `j`.
- Initialize the first row and the first column of the array to zero, since no items or no capacity means no value.
- For each item `i` from `1` to `n`, and for each capacity `j` from `1` to `W`, do the following:
  - If the weight of the item `i` is less than or equal to the capacity `j`, then we have two options: either include the item `i` in the knapsack or exclude it. The optimal value is the maximum of these two options. Therefore, we can write `dp[i][j] = max(dp[i-1][j], dp[i-1][j-wi] + vi)`, where `wi` and `vi` are the weight and value of the item `i` respectively.
  - If the weight of the item `i` is greater than the capacity `j`, then we cannot include the item `i` in the knapsack, so we just copy the value from the previous row. Therefore, we can write `dp[i][j] = dp[i-1][j]`.
- The final answer is the value stored in the bottom-right cell of the array, i.e., `dp[n][W]`.
- To find the subset of items that gives the optimal value, we can backtrack from the bottom-right cell and check which items were included or excluded in each step.

The following is an example of the Dynamic Programming method for the 0/1 Knapsack problem:

| Item | Weight | Value |
|------|--------|-------|
| 1    | 2      | 3     |
| 2    | 3      | 4     |
| 3    | 4      | 5     |
| 4    | 5      | 6     |

Knapsack capacity: 8

| dp[i][j] | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|----------|---|---|---|---|---|---|---|---|---|
| i = 0    | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| i = 1    | 0 | 0 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| i = 2    | 0 | 0 | 3 | 4 | 4 | 7 | 7 | 7 | 7 |
| i = 3    | 0 | 0 | 3 | 4 | 5 | 7 | 8 | 9 | 9 |
| i = 4    | 0 | 0 | 3 | 4 | 5 | 7 | 8 | 9 | 10|

Optimal value: 10

Optimal subset: {1, 2, 4}

### (b) Greedy method

Greedy method is a technique that makes a locally optimal choice at each step, hoping that it will lead to a globally optimal solution. The main idea is to pick the most promising item at each step without considering the future consequences.

To solve the 0/1 Knapsack problem using Greedy method