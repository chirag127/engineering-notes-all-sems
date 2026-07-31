## Knapsack Problem using Greedy Solution

The knapsack problem is a problem of finding the optimal way to fill a knapsack with a given capacity and a set of items, each with a value and a weight. The goal is to maximize the total value of the items in the knapsack without exceeding the capacity.

There are two variants of the knapsack problem: the 0-1 knapsack problem and the fractional knapsack problem. In the 0-1 knapsack problem, each item can either be taken or left out, while in the fractional knapsack problem, each item can be taken partially or fully.

The greedy solution is a heuristic algorithm that works well for the fractional knapsack problem, but not for the 0-1 knapsack problem. The greedy solution is based on the following steps   :

- Sort the items by their value-to-weight ratio in descending order.
- Start with an empty knapsack and iterate over the sorted items.
- For each item, if the knapsack can accommodate the whole item, take it fully and update the knapsack value and weight. Otherwise, if the knapsack can accommodate a fraction of the item, take that fraction and fill the knapsack completely. Stop the iteration.
- Return the final knapsack value and the items taken.

The greedy solution has a time complexity of O(n log n), where n is the number of items, since the sorting step dominates the iteration step. The greedy solution is optimal for the fractional knapsack problem, since it always takes the item with the highest value-to-weight ratio at each step, and thus maximizes the value per unit of weight. However, the greedy solution is not optimal for the 0-1 knapsack problem, since it may miss some combinations of items that have a higher value than the greedy choice.

An example of the greedy solution for the fractional knapsack problem is shown below:

| Item | Value | Weight | Value/Weight |
|------|-------|--------|--------------|
| A    | 60    | 10     | 6            |
| B    | 100   | 20     | 5            |
| C    | 120   | 30     | 4            |

The knapsack capacity is 50 units. The greedy solution sorts the items by their value-to-weight ratio and obtains the following order: A, B, C. The greedy solution then takes the following steps:

- Take item A fully, since the knapsack can accommodate it. The knapsack value is 60 and the knapsack weight is 10.
- Take item B fully, since the knapsack can accommodate it. The knapsack value is 160 and the knapsack weight is 30.
- Take 2/3 of item C, since the knapsack can only accommodate 20 units of weight. The knapsack value is 240 and the knapsack weight is 50.
- Stop the iteration, since the knapsack is full.

The final knapsack value is 240 and the items taken are A, B, and 2/3 of C. This is the optimal solution for the fractional knapsack problem.