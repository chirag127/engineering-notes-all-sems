## Implement the 0/1 Knapsack problem using (a) Dynamic Programming method (b) Greedy method

The 0/1 Knapsack problem is a maximization problem in which we are given a set of items, each with a weight and a value, and we have to determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.

### (a) Dynamic Programming method

Dynamic Programming (DP) is an algorithmic paradigm that solves a problem by breaking it down into smaller subproblems and storing the results of these subproblems in a table to avoid recomputation. DP is suitable for problems that have overlapping subproblems and optimal substructure properties.

To solve the 0/1 Knapsack problem using DP, we can follow these steps:

- Define a 2D array `K[n+1][W+1]` where `n` is the number of items and `W` is the weight limit. `K[i][j]` will store the maximum value that can be obtained by using items from `1` to `i` with a weight limit of `j`.
- Initialize the first row and the first column of `K` to `0`, since no item or no weight can give any value.
- For each item `i` from `1` to `n`, do the following:
  - For each weight `j` from `1` to `W`, do the following:
    - If the weight of item `i` is less than or equal to `j`, then compare the value of including item `i` or excluding item `i` in the solution. The value of including item `i` is `K[i-1][j-wi] + pi`, where `wi` and `pi` are the weight and value of item `i`, respectively. The value of excluding item `i` is `K[i-1][j]`. Choose the maximum of these two values and store it in `K[i][j]`.
    - If the weight of item `i` is greater than `j`, then the value of `K[i][j]` is the same as the value of `K[i-1][j]`, since item `i` cannot be included in the solution.
- Return the value of `K[n][W]` as the final answer.

The time complexity of this algorithm is `O(nW)` and the space complexity is `O(nW)`.

### (b) Greedy method

Greedy method is an algorithmic paradigm that makes the locally optimal choice at each stage with the hope of finding a global optimum. Greedy method is suitable for problems that have greedy choice property and optimal substructure property.

To solve the 0/1 Knapsack problem using Greedy method, we can follow these steps:

- Sort the items in decreasing order of their value/weight ratio, which is also called the profit density.
- Initialize the total value to `0` and the remaining weight to `W`.
- For each item `i` from `1` to `n`, do the following:
  - If the weight of item `i` is less than or equal to the remaining weight, then include item `i` in the solution, add its value to the total value, and subtract its weight from the remaining weight.
  - If the weight of item `i` is greater than the remaining weight, then break the loop and return the total value as the final answer.

The time complexity of this algorithm is `O(n log n)` and the space complexity is `O(1)`.

However, the Greedy method may not always give an optimal solution for the 0/1 Knapsack problem, since it does not consider the whole problem, but only the current choice . For example, consider the following instance of the problem:

| Item | Weight | Value |
|------|--------|-------|
| 1    | 10     | 60    |
| 2    | 20     | 100   |
| 3    | 30     | 120   |

The weight limit is `50`. The Greedy method will sort the items by their value/weight ratio as follows:

| Item | Weight | Value | Value/Weight |
|------|--------|-------|--------------|
| 1    | 10     |