## Implement the 0/1 Knapsack problem using (a) Dynamic Programming method (b) Greedy method.

The 0/1 Knapsack problem is a classic optimization problem where we have a set of items, each with a weight and a value, and we need to determine the subset of items that maximizes the total value while keeping the total weight within a given limit. The name 0/1 comes from the fact that we can either take an item or leave it, but not take a fraction of it.

### (a) Dynamic Programming method

Dynamic programming is a technique for solving problems that have overlapping subproblems and optimal substructure. The idea is to break down the problem into smaller subproblems, solve them once and store their solutions, and then use them to solve the original problem.

The dynamic programming method for the 0/1 Knapsack problem works as follows:

- Define a 2D array `dp[n+1][W+1]`, where `n` is the number of items and `W` is the knapsack capacity. Each cell `dp[i][j]` will store the maximum value that can be obtained by using the first `i` items and a knapsack of capacity `j`.
- Initialize the first row and the first column of `dp` to zero, since no value can be obtained with zero items or zero capacity.
- For each item `i` from `1` to `n`, and for each capacity `j` from `1` to `W`, do the following:
  - If the weight of the item `i` is less than or equal to `j`, then we have two options: either take the item or leave it. The maximum value in this case is the maximum of these two options:
    - Take the item: the value is `dp[i-1][j-w[i]] + v[i]`, where `w[i]` and `v[i]` are the weight and value of the item `i`, and `dp[i-1][j-w[i]]` is the maximum value that can be obtained by using the first `i-1` items and a knapsack of capacity `j-w[i]`.
    - Leave the item: the value is `dp[i-1][j]`, which is the maximum value that can be obtained by using the first `i-1` items and a knapsack of capacity `j`.
  - If the weight of the item `i` is greater than `j`, then we cannot take the item, and the maximum value is `dp[i-1][j]`.
  - Update `dp[i][j]` with the maximum value obtained from the above cases.
- The final answer is `dp[n][W]`, which is the maximum value that can be obtained by using all the items and a knapsack of capacity `W`.

The pseudocode for the dynamic programming method is:

```
function knapsack_dp(w, v, n, W):
  // w: array of item weights
  // v: array of item values
  // n: number of items
  // W: knapsack capacity
  // returns: maximum value that can be obtained

  // create a 2D array of size (n+1) x (W+1)
  dp = array[n+1][W+1]

  // initialize the first row and column to zero
  for i = 0 to n:
    dp[i][0] = 0
  for j = 0 to W:
    dp[0][j] = 0

  // fill the rest of the array using the recurrence relation
  for i = 1 to n:
    for j = 1 to W:
      if w[i] <= j:
        // either take the item or leave it
        dp[i][j] = max(dp[i-1][j-w[i]] + v[i], dp[i-1][j])
      else:
        // cannot take the item
        dp[i][j] = dp[i-1][j]

  // return the final answer
  return dp[n][W]
```

The time complexity of the dynamic programming method is `O(nW)`, where `n` is the number of items and `W` is the knapsack capacity. The space complexity is also `O(nW)`, since we need to store the `dp` array.

### (b) Greedy method

The greedy method for the 0/1 Knaps