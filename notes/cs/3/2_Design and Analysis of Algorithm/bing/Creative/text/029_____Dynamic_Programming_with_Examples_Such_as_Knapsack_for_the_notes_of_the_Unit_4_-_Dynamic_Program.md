### Dynamic Programming with Examples Such as Knapsack

- Dynamic programming is a technique for solving problems that have overlapping subproblems and optimal substructure.
- Overlapping subproblems means that the same subproblem is solved repeatedly, and optimal substructure means that the optimal solution of a problem can be obtained from the optimal solutions of its subproblems.
- Dynamic programming can be used to solve problems that can be formulated as recurrence relations, which express the solution of a problem in terms of the solutions of smaller instances of the same problem.
- Dynamic programming can reduce the time complexity of solving a problem from exponential to polynomial, by avoiding recomputation of subproblems and storing the intermediate results in a table or an array.
- One of the classic examples of dynamic programming is the 0/1 knapsack problem, which can be stated as follows:

  - Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given capacity and the total value is as large as possible.
  - The 0/1 knapsack problem is called so because each item can be either included (1) or excluded (0) from the collection, but not partially.
  - The 0/1 knapsack problem can be solved using dynamic programming by defining a function `f(i, w)` that returns the maximum value that can be obtained by using items from `1` to `i` with a weight limit of `w`.
  - The recurrence relation for `f(i, w)` is:

    - `f(i, w) = 0` if `i = 0` or `w = 0`
    - `f(i, w) = f(i - 1, w)` if `w < wi`
    - `f(i, w) = max(f(i - 1, w), f(i - 1, w - wi) + vi)` if `w >= wi`
  - Where `wi` and `vi` are the weight and value of the `i`-th item, respectively.
  - The base case of the recurrence is when there are no items or no weight limit, in which case the maximum value is zero.
  - The optimal solution of the problem is `f(n, W)`, where `n` is the number of items and `W` is the capacity of the knapsack.
  - The dynamic programming algorithm for the 0/1 knapsack problem can be implemented as follows:

    - Initialize a two-dimensional array `dp[n + 1][W + 1]` to store the values of `f(i, w)`.
    - For `i` from `0` to `n`, and for `w` from `0` to `W`, compute `dp[i][w]` according to the recurrence relation.
    - Return `dp[n][W]` as the optimal solution.
  - The time complexity of the dynamic programming algorithm is `O(nW)`, where `n` is the number of items and `W` is the capacity of the knapsack. The space complexity is also `O(nW)`, as we need to store the values of `f(i, w)` in a two-dimensional array.
  - An example of the 0/1 knapsack problem is:

    - Number of items `n = 4`, knapsack capacity `W = 5`, weights `(w1, w2, w3, w4) = (2, 3, 4, 5)` and values `(v1, v2, v3, v4) = (3, 4, 5, 6)`.
    - The dynamic programming table `dp` is:

      | i\w | 0 | 1 | 2 | 3 | 4 | 5 |
      | --- | - | - | - | - | - | - |
      | 0   | 0 | 0 | 0 | 0 | 0 | 0 |
      | 1   | 0 | 0 | 3 | 3 | 3 | 3 |
      | 2   | 0 | 0 | 3 | 4 | 4 | 7 |
      | 3   | 0 | 0 | 3 | 4 | 5 | 7 |
      | 4   | 0 | 0 | 3 | 4 | 5 | 7