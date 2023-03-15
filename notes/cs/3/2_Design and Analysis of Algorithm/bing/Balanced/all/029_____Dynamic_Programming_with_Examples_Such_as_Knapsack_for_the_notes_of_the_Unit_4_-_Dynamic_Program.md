# Dynamic Programming with Examples Such as Knapsack

- Dynamic programming is a technique for solving problems that have overlapping subproblems and optimal substructure.
- Overlapping subproblems means that the same subproblem is solved repeatedly, and optimal substructure means that the optimal solution of a problem can be obtained from the optimal solutions of its subproblems.
- Dynamic programming can be used to solve problems that can be divided into smaller subproblems of the same type, and the solutions of the subproblems can be combined to obtain the solution of the original problem.
- Dynamic programming can reduce the time complexity of solving a problem by avoiding recomputation of the same subproblems, and can also save space by storing the solutions of the subproblems in a table or an array.
- Dynamic programming can be implemented using two approaches: top-down and bottom-up. In the top-down approach, the problem is solved recursively by breaking it into smaller subproblems, and the solutions of the subproblems are stored in a table or an array for future use. In the bottom-up approach, the problem is solved iteratively by starting from the smallest subproblems and building up the solution of the original problem by using the solutions of the subproblems.
- One of the classic examples of dynamic programming is the 0/1 knapsack problem, which is stated as follows:

## 0/1 Knapsack Problem

- Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight does not exceed a given limit and the total value is as large as possible.
- The 0/1 knapsack problem is called so because each item can be either included (1) or excluded (0) from the collection, and there is no fractional inclusion of any item.
- The 0/1 knapsack problem can be solved using dynamic programming by defining a function `f(i, w)` that returns the maximum value that can be obtained by using the first `i` items and a knapsack of capacity `w`.
- The function `f(i, w)` can be computed recursively as follows:

```
f(i, w) = 0, if i = 0 or w = 0
f(i, w) = f(i - 1, w), if wi > w
f(i, w) = max(f(i - 1, w), f(i - 1, w - wi) + vi), if wi <= w
```

- Where `wi` and `vi` are the weight and value of the `i`-th item, respectively.
- The base case of the recursion is when `i = 0` or `w = 0`, which means that there are no items or no capacity left, and the maximum value is zero.
- The recursive case has two possibilities: either the `i`-th item is not included in the optimal solution, in which case the maximum value is the same as using the first `i - 1` items and the same capacity, or the `i`-th item is included in the optimal solution, in which case the maximum value is the sum of the value of the `i`-th item and the maximum value of using the first `i - 1` items and the remaining capacity after subtracting the weight of the `i`-th item.
- The optimal solution of the 0/1 knapsack problem is given by `f(n, W)`, where `n` is the number of items and `W` is the capacity of the knapsack.
- The function `f(i, w)` can be computed using a two-dimensional array of size `(n + 1) x (W + 1)`, where each element `f[i][w]` stores the value of `f(i, w)`.
- The array can be filled up in a bottom-up manner, starting from the base case of `f[0][w] = 0` for all `w`, and `f[i][0] = 0` for all `i`, and then using the recursive formula to compute the rest of the elements.
- The time complexity of this algorithm is `O(nW)`, and the space complexity is also `O(nW)`.
- The following is an example of solving the 0/1 knapsack problem using dynamic programming:

### Example

- Find an optimal solution for the following 0/1 knapsack problem using dynamic programming:

```
Number of items n = 4
Knapsack capacity W =