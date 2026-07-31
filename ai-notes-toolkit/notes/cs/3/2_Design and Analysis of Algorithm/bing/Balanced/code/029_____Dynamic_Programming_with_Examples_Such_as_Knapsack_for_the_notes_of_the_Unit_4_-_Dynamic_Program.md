### Dynamic Programming with Examples Such as Knapsack

- Dynamic programming is a technique for solving problems that have overlapping subproblems and optimal substructure.
- Overlapping subproblems means that the same subproblem is solved repeatedly, and optimal substructure means that the optimal solution of a problem can be obtained from the optimal solutions of its subproblems.
- Dynamic programming can be used to avoid recomputing the same subproblem multiple times, by storing the results of subproblems in a table and reusing them when needed.
- Dynamic programming can be applied to problems that have two properties: a recursive formulation and a memoization function.
- A recursive formulation is a way of expressing the problem in terms of smaller instances of the same problem, such as a recurrence relation or a recursive function.
- A memoization function is a way of mapping each subproblem to a unique index, such as a tuple of parameters or a hash value, that can be used to store and retrieve the results of subproblems in a table.
- Dynamic programming can be implemented in two ways: top-down and bottom-up.
- Top-down dynamic programming starts with the original problem and recursively solves the subproblems, while storing and reusing the results in a table. This approach is also known as memoization or lazy evaluation.
- Bottom-up dynamic programming starts with the smallest subproblems and iteratively solves larger subproblems, while storing and reusing the results in a table. This approach is also known as tabulation or eager evaluation.
- Dynamic programming can be used to solve various types of problems, such as optimization, counting, decision making, and path finding.
- One of the classic examples of dynamic programming is the 0/1 knapsack problem, which is an optimization problem.

#### 0/1 Knapsack Problem

- The 0/1 knapsack problem is defined as follows: given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight does not exceed a given limit and the total value is as large as possible.
- The 0/1 knapsack problem is called so because each item can be either included (1) or excluded (0) from the collection, and there is no fractional or partial inclusion of items.
- The 0/1 knapsack problem can be formulated as a recursive function as follows:

```
// K(n, W) is the maximum value that can be obtained by using items 1 to n with a weight limit of W
// w[i] and v[i] are the weight and value of item i, respectively
// n is the number of items and W is the weight limit

K(n, W) = 0, if n == 0 or W == 0 // base case
K(n, W) = K(n - 1, W), if w[n] > W // item n cannot be included
K(n, W) = max(K(n - 1, W), v[n] + K(n - 1, W - w[n])), if w[n] <= W // item n can be included or excluded
```

- The 0/1 knapsack problem can be solved using top-down dynamic programming by implementing the recursive function with a memoization table, such as a two-dimensional array, that stores the results of subproblems and avoids recomputing them.

```
// K[n][W] is the memoization table that stores the results of subproblems
// K[i][j] is the maximum value that can be obtained by using items 1 to i with a weight limit of j
// w[i] and v[i] are the weight and value of item i, respectively
// n is the number of items and W is the weight limit

// initialize the table with -1 values to indicate that the subproblems are not solved yet
for i = 0 to n
  for j = 0 to W
    K[i][j] = -1

// define the recursive function with memoization
K(n, W) = 0, if n == 0 or W == 0 // base case
K(n, W) = K[n][W], if K[n][W] != -1 // subproblem already solved
K(n, W) = K(n - 1, W), if w[n] > W // item n cannot be included
K(n, W) = max(K(n - 1, W), v[n] + K(n - 1, W - w[n])), if w[n] <= W //

```
