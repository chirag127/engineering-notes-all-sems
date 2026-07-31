## Implementing the 0/1 Knapsack problem using (a) Dynamic Programming method (b) Greedy method

The 0/1 Knapsack problem is a combinatorial optimization problem where we are given a set of items, each with a weight and a value, and we need to determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. There are two common methods to solve this problem: the Dynamic Programming method and the Greedy method.

### (a) Dynamic Programming method

The Dynamic Programming method is an efficient way to solve the 0/1 Knapsack problem. It is based on the principle of optimality, which states that an optimal solution to a problem can be constructed from optimal solutions to its subproblems.

1. Create a 2D array `K[n+1][W+1]` where `n` is the number of items and `W` is the maximum weight the knapsack can carry.
2. Initialize the first row and the first column of the array to 0.
3. For `i` from 1 to `n`, do the following:
    1. For `w` from 1 to `W`, do the following:
        1. If the weight of the `i`-th item is less than or equal to `w`, then `K[i][w] = max(K[i-1][w], K[i-1][w-wt[i-1]] + val[i-1])`.
        2. Else, `K[i][w] = K[i-1][w]`.
4. The maximum value that can be obtained is `K[n][W]`.

### (b) Greedy method

The Greedy method is a simple and intuitive way to solve the 0/1 Knapsack problem. It is based on the idea of selecting the most valuable items first, until the knapsack is full or there are no more items to select.

1. Calculate the value per unit weight for each item and sort the items in decreasing order of their value per unit weight.
2. Initialize the total value of the knapsack to 0 and the total weight of the knapsack to 0.
3. For each item in the sorted list, do the following:
    1. If the weight of the item is less than or equal to the remaining capacity of the knapsack, add the item to the knapsack, update the total value and the total weight of the knapsack.
    2. Else, break the loop.
4. The maximum value that can be obtained is the total value of the knapsack.

It is important to note that the Greedy method does not always produce an optimal solution to the 0/1 Knapsack problem. However, it is a fast and easy-to-implement method that can provide a good approximate solution in many cases. On the other hand, the Dynamic Programming method always produces an optimal solution, but it can be more time-consuming to implement and has a higher time complexity. The choice of method depends on the specific requirements of the problem at hand.