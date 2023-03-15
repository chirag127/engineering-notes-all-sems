## Implementing the 0/1 Knapsack problem using (a) Dynamic Programming method (b) Greedy method

The 0/1 Knapsack problem is a combinatorial optimization problem where the goal is to maximize the total value of items that can be placed into a knapsack of limited capacity. Each item has a weight and a value, and only one of each item can be selected. There are two common methods to solve this problem: the Dynamic Programming method and the Greedy method.

### (a) Dynamic Programming method

The Dynamic Programming method is an efficient approach to solve the 0/1 Knapsack problem. It is based on the principle of optimality, which states that an optimal solution to a problem can be constructed from optimal solutions to its subproblems.

1. Create a 2D array `K[n+1][W+1]` where `n` is the number of items and `W` is the maximum capacity of the knapsack.
2. Initialize the first row and the first column of the array to 0.
3. For each item `i` from 1 to `n`, and for each capacity `w` from 1 to `W`, do the following:
    - If the weight of the item `i` is less than or equal to `w`, then set `K[i][w]` to the maximum of `K[i-1][w]` and `K[i-1][w-wt[i-1]] + val[i-1]`.
    - Otherwise, set `K[i][w]` to `K[i-1][w]`.
4. The maximum value that can be placed into the knapsack is `K[n][W]`.

### (b) Greedy method

The Greedy method is a simple approach to solve the 0/1 Knapsack problem. It is based on the idea of selecting the most valuable items first, until the knapsack is full or there are no more items to select.

1. Calculate the value per unit weight for each item, and sort the items in decreasing order of this value.
2. Initialize the total value of the knapsack to 0 and the remaining capacity of the knapsack to `W`.
3. For each item `i` from 1 to `n`, do the following:
    - If the weight of the item `i` is less than or equal to the remaining capacity of the knapsack, then add the item to the knapsack, update the total value of the knapsack, and decrease the remaining capacity of the knapsack by the weight of the item.
    - Otherwise, break the loop.
4. The maximum value that can be placed into the knapsack is the total value of the knapsack.

It is important to note that the Greedy method does not always produce an optimal solution to the 0/1 Knapsack problem. However, it is a simple and fast approach that can provide a good approximation to the optimal solution in many cases. In contrast, the Dynamic Programming method always produces an optimal solution, but it can be more time-consuming to implement and execute. The choice of method depends on the specific requirements of the problem at hand.