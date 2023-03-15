## Implement the 0/1 Knapsack problem using (a) Dynamic Programming method (b) Greedy method.

The 0/1 Knapsack problem is a classic optimization problem where we have a set of items, each with a weight and a value, and we want to choose a subset of items that maximizes the total value while keeping the total weight within a given limit. The 0/1 means that we can either take an item or leave it, but not take a fraction of it.

There are two common methods to solve this problem: dynamic programming and greedy method.

### (a) Dynamic Programming method

Dynamic programming is a technique that breaks down a complex problem into smaller and overlapping subproblems, and solves them by reusing the solutions of the subproblems. The idea is to use a table to store the optimal value for each subproblem, and then use the table to construct the final solution.

The steps for the dynamic programming method are:

- Define the subproblems: Let `V[i][w]` be the maximum value that can be obtained by using the first `i` items and a knapsack of capacity `w`. The base case is `V[0][w] = 0` for any `w`, meaning that no items can be taken.
- Define the recurrence relation: For each `i > 0` and `w >= 0`, we have two choices: either take the `i`-th item or leave it. If we take it, we add its value to the optimal value of the subproblem with `i-1` items and `w-wi` capacity, where `wi` is the weight of the `i`-th item. If we leave it, we get the optimal value of the subproblem with `i-1` items and `w` capacity. Therefore, the recurrence relation is:

  `V[i][w] = max(V[i-1][w], vi + V[i-1][w-wi])` if `wi <= w`

  `V[i][w] = V[i-1][w]` otherwise

  where `vi` is the value of the `i`-th item.
- Fill the table: We can fill the table in a bottom-up manner, starting from the base case and following the recurrence relation. The final answer will be `V[n][W]`, where `n` is the number of items and `W` is the knapsack capacity.
- Reconstruct the solution: To find the subset of items that gives the optimal value, we can trace back the table from `V[n][W]` and check which items were taken. If `V[i][w] > V[i-1][w]`, then the `i`-th item was taken, and we reduce the problem to `V[i-1][w-wi]`. Otherwise, the `i`-th item was not taken, and we reduce the problem to `V[i-1][w]`. We repeat this process until we reach the base case.

The pseudocode for the dynamic programming method is:

```
// Input: n = number of items, W = knapsack capacity, w[] = array of item weights, v[] = array of item values
// Output: V[n][W] = maximum value, S[] = array of items taken (1 = taken, 0 = not taken)

// Initialize the table V[][] with 0
for i = 0 to n
  for j = 0 to W
    V[i][j] = 0

// Fill the table using the recurrence relation
for i = 1 to n
  for j = 0 to W
    if w[i] <= j // the item can be taken
      V[i][j] = max(V[i-1][j], v[i] + V[i-1][j-w[i]])
    else // the item cannot be taken
      V[i][j] = V[i-1][j]

// Initialize the solution array S[] with 0
for i = 0 to n
  S[i] = 0

// Trace back the table to find the items taken
i = n
j = W
while i > 0 and j > 0
  if V[i][j] > V[i-1][j] // the item was taken
    S[i] = 1 // mark the item as taken
    j = j - w[i] // reduce the capacity by the item weight
  i = i - 1 // move to the previous item

// Return the maximum value and the solution array
return V[n][W],