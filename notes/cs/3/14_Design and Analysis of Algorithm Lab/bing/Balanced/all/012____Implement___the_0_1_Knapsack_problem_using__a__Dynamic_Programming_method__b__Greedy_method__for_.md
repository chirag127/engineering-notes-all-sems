## Implement the 0/1 Knapsack problem using (a) Dynamic Programming method (b) Greedy method.

The 0/1 Knapsack problem is a classic optimization problem where we have a set of items, each with a weight and a value, and we want to choose a subset of items that maximizes the total value while keeping the total weight within a given limit. The 0/1 means that we can either take an item or leave it, but not take a fraction of it.

There are two common methods to solve this problem: dynamic programming and greedy method.

### (a) Dynamic Programming method

Dynamic programming is a technique that breaks down a complex problem into smaller and overlapping subproblems, and solves them by reusing the solutions of the subproblems. The idea is to use a table to store the optimal value for each subproblem, and then use the table to construct the final solution.

The steps for the dynamic programming method are:

- Define the subproblems: Let `V[i][w]` be the maximum value that can be obtained by using the first `i` items and a knapsack of capacity `w`. The base case is `V[0][w] = 0` for any `w`, meaning that no items can be taken.
- Define the recurrence relation: For each `i > 0` and `w >= 0`, we have two options: either take the `i`-th item or leave it. If we take it, we add its value to the optimal value of the subproblem with `i-1` items and `w-wi` capacity, where `wi` is the weight of the `i`-th item. If we leave it, we keep the optimal value of the subproblem with `i-1` items and `w` capacity. Therefore, we have:

  `V[i][w] = max(V[i-1][w], vi + V[i-1][w-wi])` if `wi <= w`

  `V[i][w] = V[i-1][w]` if `wi > w`

  where `vi` is the value of the `i`-th item.
- Fill the table: We can use a nested loop to fill the table from bottom to top and left to right, following the recurrence relation.
- Construct the solution: We can use another nested loop to trace back the table from the bottom right corner to the top left corner, and check which items are included in the optimal solution. If `V[i][w] > V[i-1][w]`, it means that the `i`-th item is taken, and we reduce the capacity by `wi`. Otherwise, it means that the `i`-th item is not taken, and we move to the previous row.

The pseudocode for the dynamic programming method is:

```
// Input: n = number of items, W = knapsack capacity, w[] = array of item weights, v[] = array of item values
// Output: V[n][W] = maximum value, X[] = array of item choices (1 for taken, 0 for not taken)

// Initialize the table V[][] with 0
for i = 0 to n
  for j = 0 to W
    V[i][j] = 0

// Fill the table V[][] using the recurrence relation
for i = 1 to n
  for j = 0 to W
    if w[i] <= j // if the item can fit in the knapsack
      V[i][j] = max(V[i-1][j], v[i] + V[i-1][j-w[i]]) // choose the maximum value between taking and leaving the item
    else // if the item cannot fit in the knapsack
      V[i][j] = V[i-1][j] // leave the item

// Initialize the array X[] with 0
for i = 0 to n
  X[i] = 0

// Trace back the table V[][] to construct the solution
i = n // start from the last item
j = W // start from the full capacity
while i > 0 and j > 0
  if V[i][j] > V[i-1][j] // if the item is taken
    X[i] = 1 // mark the item as taken
    j = j - w[i] // reduce the capacity by the item weight
  i = i - 1 // move to the previous item
```

### (b) Greedy method

Greedy method is a technique that makes a locally optimal choice at each