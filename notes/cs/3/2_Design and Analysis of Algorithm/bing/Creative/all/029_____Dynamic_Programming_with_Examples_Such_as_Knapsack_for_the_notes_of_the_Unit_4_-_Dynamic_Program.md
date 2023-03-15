# Dynamic Programming with Examples Such as Knapsack

- Dynamic programming is a technique for solving problems that have overlapping subproblems and optimal substructure.
- Overlapping subproblems means that the same subproblem is solved repeatedly, and optimal substructure means that the optimal solution of a problem can be obtained from the optimal solutions of its subproblems.
- Dynamic programming can be used to solve problems that can be divided into smaller subproblems of the same type, such as the knapsack problem, the longest common subsequence problem, the matrix chain multiplication problem, etc.
- Dynamic programming can reduce the time complexity of solving a problem from exponential to polynomial, by avoiding recomputation of subproblems and storing the results in a table or an array.
- Dynamic programming can be implemented using two approaches: top-down and bottom-up. The top-down approach starts from the original problem and recursively solves the subproblems, while the bottom-up approach starts from the base cases and iteratively builds up the solution.

## Knapsack Problem

- The knapsack problem is a classic example of a problem that can be solved using dynamic programming. The problem statement is as follows:

  - Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight does not exceed a given limit and the total value is as large as possible.

- There are two variants of the knapsack problem: the 0/1 knapsack problem and the fractional knapsack problem. The 0/1 knapsack problem only allows to include or exclude an item, while the fractional knapsack problem allows to include a fraction of an item.

- The 0/1 knapsack problem can be solved using dynamic programming by defining a table K[i][j] that stores the maximum value that can be obtained by using items from 1 to i with a weight limit of j. The table can be filled using the following recurrence relation:

  - K[i][j] = max(K[i-1][j], K[i-1][j-w[i]] + v[i]) if w[i] <= j
  - K[i][j] = K[i-1][j] if w[i] > j

  where w[i] and v[i] are the weight and value of the ith item, respectively.

- The time and space complexity of this algorithm is O(nW), where n is the number of items and W is the weight limit.

- The fractional knapsack problem can be solved using a greedy approach by sorting the items in decreasing order of their value per unit weight, and then selecting the items in that order until the weight limit is reached or all the items are exhausted. The time complexity of this algorithm is O(n log n), where n is the number of items.