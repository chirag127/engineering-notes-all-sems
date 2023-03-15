## Knapsack Problem using Greedy Solution

The knapsack problem is a problem in combinatorial optimization, where we are given a set of items, each with a weight and a value, and we have to determine which items to include in a collection (knapsack) so that the total weight is less than or equal to a given limit (capacity) and the total value is as large as possible.

There are two variants of the knapsack problem:

- The 0-1 knapsack problem, where we can only take whole items or leave them.
- The fractional knapsack problem, where we can take fractions of items as well.

The greedy solution is an efficient method to solve the fractional knapsack problem, where we can break items to maximize the knapsack's total value. The greedy solution does not work for the 0-1 knapsack problem, as it may not produce the optimal solution.

The greedy solution for the fractional knapsack problem works as follows  :

- For each item, compute its value/weight ratio, which indicates how much value we get per unit of weight.
- Sort the items in decreasing order of their value/weight ratios.
- Start with an empty knapsack and iterate over the sorted items.
- For each item, if its weight is less than or equal to the remaining capacity of the knapsack, take the whole item and add its value to the total value of the knapsack. Otherwise, take a fraction of the item that fills the knapsack completely and add the corresponding fraction of its value to the total value of the knapsack.
- Return the total value of the knapsack as the optimal solution.

The following diagram illustrates the greedy solution for the fractional knapsack problem with five items and a capacity of 15 units:

![Fractional Knapsack Problem using Greedy Solution](https://www.gatevidyalay.com/wp-content/uploads/2018/07/Fractional-Knapsack-Problem-Using-Greedy-Approach-Example.png)

The greedy solution for the fractional knapsack problem has a time complexity of O(n log n), where n is the number of items, as the main step is to sort the items by their value/weight ratios. The space complexity is O(1), as we only need constant extra space to store the total value and the remaining capacity of the knapsack.