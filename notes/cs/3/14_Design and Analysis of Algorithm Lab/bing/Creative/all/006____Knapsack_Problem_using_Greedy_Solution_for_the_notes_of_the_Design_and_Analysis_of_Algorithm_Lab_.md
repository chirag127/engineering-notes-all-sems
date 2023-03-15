# Knapsack Problem using Greedy Solution

The knapsack problem is a problem in combinatorial optimization, where we are given a set of items, each with a weight and a value, and we want to find a subset of items that maximizes the total value while keeping the total weight within a given limit.

There are two variants of the knapsack problem: the 0-1 knapsack problem and the fractional knapsack problem. In the 0-1 knapsack problem, we can only take an item in its entirety or leave it. In the fractional knapsack problem, we can take a fraction of an item as well.

The greedy solution is a heuristic that works for the fractional knapsack problem, but not for the 0-1 knapsack problem. The greedy solution is based on the following steps:

- For each item, compute its value/weight ratio.
- Sort the items in decreasing order of their value/weight ratio.
- Starting from the item with the highest ratio, take as much of it as possible, until the knapsack is full or the item is exhausted.
- Repeat the previous step for the next item in the sorted order, until the knapsack is full or there are no more items.

The greedy solution is optimal for the fractional knapsack problem, because it always picks the item that gives the most value per unit weight, and thus maximizes the total value. However, the greedy solution may not be optimal for the 0-1 knapsack problem, because it may miss some items that have lower value/weight ratio but higher value.

For example, consider the following items:

| Item | Weight | Value | Value/Weight |
|------|--------|-------|--------------|
| A    | 10     | 60    | 6            |
| B    | 20     | 100   | 5            |
| C    | 30     | 120   | 4            |

If the knapsack limit is 50, the greedy solution for the fractional knapsack problem would take 10 units of A, 20 units of B, and 6.67 units of C, for a total value of 60 + 100 + 26.67 = 186.67. This is the optimal solution for the fractional knapsack problem.

However, the greedy solution for the 0-1 knapsack problem would take A and B, for a total value of 60 + 100 = 160. This is not the optimal solution for the 0-1 knapsack problem, because we can do better by taking B and C, for a total value of 100 + 120 = 220.