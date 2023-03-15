# Dynamic Programming with Examples Such as Knapsack

Dynamic programming is a method for solving complex problems by breaking them down into simpler subproblems. It is applicable to problems that exhibit the properties of overlapping subproblems and optimal substructure. When a problem can be solved by combining optimal solutions to non-overlapping subproblems, the strategy is called "divide and conquer" instead.

One example of a problem that can be solved using dynamic programming is the knapsack problem. In the knapsack problem, you are given a set of items, each with a weight and a value, and a knapsack with a maximum weight capacity. The goal is to determine the maximum value of items that can be placed in the knapsack without exceeding its weight capacity.

To solve the knapsack problem using dynamic programming, we can create a table where the rows represent the items and the columns represent the weight capacity of the knapsack. The entry in the table at row i and column j represents the maximum value that can be achieved by considering the first i items and a knapsack with weight capacity j.

We can fill in the table using the following recursive formula:

- If the weight of the i-th item is greater than j, then the value at row i and column j is the same as the value at row i-1 and column j (i.e., we cannot include the i-th item in the knapsack).
- If the weight of the i-th item is less than or equal to j, then the value at row i and column j is the maximum of two values: the value at row i-1 and column j (i.e., not including the i-th item in the knapsack), and the value of the i-th item plus the value at row i-1 and column j minus the weight of the i-th item (i.e., including the i-th item in the knapsack).

Once the table is filled in, the maximum value that can be achieved by the knapsack is the value at the bottom right corner of the table.

This is just one example of how dynamic programming can be used to solve problems. Other examples include the all pair shortest paths problem, the resource allocation problem, and the traveling salesman problem. These problems can also be solved using other techniques such as backtracking and branch and bound. However, dynamic programming is often a more efficient approach.