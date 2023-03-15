# Knapsack Problem using Greedy Solution

- The knapsack problem is a combinatorial optimization problem that asks: Given a set of items, each with a weight and a value, determine which items to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.
- The greedy solution for the knapsack problem is an efficient method to solve it when the items can be fractionally divided, meaning that we can take a part of an item instead of the whole item. This variant is also called the fractional knapsack problem.
- The greedy solution works as follows   :
  - For each item, compute its value/weight ratio, which indicates how much value we get per unit of weight.
  - Sort the items in decreasing order of their value/weight ratios.
  - Starting from the item with the highest ratio, add as much of it as possible to the knapsack, without exceeding the weight limit.
  - Repeat the previous step for the next item in the sorted order, until the knapsack is full or there are no more items left.
- The greedy solution is optimal for the fractional knapsack problem, because it always chooses the item that gives the most value per unit of weight at each step, leaving more room for the remaining items.
- The greedy solution is not optimal for the 0-1 knapsack problem, where the items cannot be fractionally divided. In this case, the greedy solution may miss some items that have lower value/weight ratios but higher values, and thus lead to a suboptimal solution.
- The greedy solution has a time complexity of O(n log n), where n is the number of items, because the main operation is sorting the items by their value/weight ratios.