### Dynamic Programming with Examples Such as Knapsack

- Dynamic programming is a technique for solving problems that have overlapping subproblems and optimal substructure.
- Overlapping subproblems means that the same subproblem is solved repeatedly, and optimal substructure means that the optimal solution of a problem can be obtained from the optimal solutions of its subproblems.
- Dynamic programming can be used to solve problems that can be formulated as recurrence relations, which express the solution of a problem in terms of the solutions of smaller instances of the same problem.
- Dynamic programming can reduce the time complexity of solving a problem from exponential to polynomial, by avoiding recomputation of subproblems and storing the results in a table or an array.
- One of the classic examples of dynamic programming is the 0/1 knapsack problem, which can be stated as follows:

  - Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight does not exceed a given limit and the total value is as large as possible.
  - The 0/1 knapsack problem is called so because each item can be either included (1) or excluded (0) from the collection, but not partially.
  - The 0/1 knapsack problem can be solved using dynamic programming by defining a two-dimensional array `K[n+1][W+1]`, where `n` is the number of items and `W` is the weight limit of the knapsack.
  - The array `K[i][j]` stores the maximum value that can be obtained by using items from `1` to `i` and having a total weight of at most `j`.
  - The array can be filled up using the following recurrence relation:

    - `K[0][j] = 0` for all `j`, because no items can be included if there are none.
    - `K[i][0] = 0` for all `i`, because no value can be obtained if the weight limit is zero.
    - `K[i][j] = K[i-1][j]` if `w[i] > j`, because the `i`th item cannot be included if its weight exceeds the current weight limit.
    - `K[i][j] = max(K[i-1][j], v[i] + K[i-1][j-w[i]])` if `w[i] <= j`, because the `i`th item can be either included or excluded, and the maximum value is the maximum of these two options.
  - The optimal value of the problem is `K[n][W]`, and the optimal subset of items can be obtained by tracing back the array from this cell and checking which items were included or excluded at each step.
  - The time complexity of this algorithm is `O(nW)`, and the space complexity is also `O(nW)`.