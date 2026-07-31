# Knapsack Problem using Greedy Solution

- The knapsack problem is a problem of finding the optimal way to fill a knapsack with a given capacity and a set of items, each with a value and a weight.
- The fractional knapsack problem is a variation of the knapsack problem, where the items can be divided into smaller pieces and the knapsack can be filled with fractions of items.
- The greedy solution for the fractional knapsack problem is an efficient and optimal method that works as follows:
  - Sort the items by their value-to-weight ratio in descending order.
  - Start with the item with the highest ratio and take as much of it as possible, until the knapsack is full or the item is exhausted.
  - If the knapsack is not full, move to the next item with the next highest ratio and repeat the previous step.
  - Continue this process until the knapsack is full or there are no more items left.
- The greedy solution for the fractional knapsack problem has a time complexity of O(n log n), where n is the number of items, because the sorting step dominates the algorithm.
- The greedy solution for the fractional knapsack problem is optimal because at each step, it chooses the item that gives the maximum value per unit weight, which maximizes the total value of the knapsack.