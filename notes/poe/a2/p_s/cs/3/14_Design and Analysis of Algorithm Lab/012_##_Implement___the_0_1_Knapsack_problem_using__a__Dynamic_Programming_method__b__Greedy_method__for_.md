 Here is the content in markdown format:

## Implement, the 0/1 Knapsack problem using (a) Dynamic Programming method (b) Greedy method.

### Dynamic Programming method

1. State expression: Let dp[i][j] denote the maximum value we can obtain using the first i items and a knapsack of capacity j.
2. Base cases: dp[0][j] = 0 for all j, dp[i][0] = 0 for all i.
3. Recurrence relation: dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i]) where w[i] and v[i] are the weight and value of the ith item respectively.
4. Order of evaluation: Evaluate the subproblems in bottom-up manner.
5. Time complexity: O(n*C) where n is the number of items and C is the knapsack capacity.

Advantages:
- Guaranteed to find the optimal solution.
- Avoid repeated subproblems.

Disadvantages:
- Requires O(n*C) space to store the subproblems.

Examples:
Input: Weights: [1, 3, 4, 5], Values: [1, 4, 5, 7], Capacity: 7
Output: dp = [[0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1],
            [0, 1, 4, 4, 5, 5, 6],
            [0, 1, 4, 5, 7, 7, 9],
            [0, 1, 4, 5, 7, 9, 9]]
Max value achievable = 9

<Additional details and diagrams can be included here.>

### Greedy method

<Write details about the Greedy method here along with examples, advantages, disadvantages, etc.>