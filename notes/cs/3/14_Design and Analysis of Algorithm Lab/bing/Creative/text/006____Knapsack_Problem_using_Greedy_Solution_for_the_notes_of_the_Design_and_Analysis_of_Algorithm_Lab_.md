## Knapsack Problem using Greedy Solution

- The knapsack problem is a combinatorial optimization problem that asks: Given a set of items, each with a weight and a value, determine which items to include in the collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.
- The fractional knapsack problem is a variation of the knapsack problem, where the items can be broken into smaller pieces and the thief can take any fraction of an item.
- The greedy solution for the fractional knapsack problem is an efficient method that works as follows   :
  - For each item, compute its value/weight ratio.
  - Sort the items in decreasing order of their value/weight ratio.
  - Initialize the total value and the total weight of the knapsack to zero.
  - For each item in the sorted order, do the following:
    - If the item's weight is less than or equal to the remaining capacity of the knapsack, then take the whole item and add its value and weight to the knapsack.
    - If the item's weight is more than the remaining capacity of the knapsack, then take a fraction of the item that fills the knapsack and add its proportional value and weight to the knapsack.
    - Break the loop if the knapsack is full.
  - Return the total value and the total weight of the knapsack as the optimal solution.
- The greedy solution for the fractional knapsack problem has a time complexity of O(n log n), where n is the number of items, because the main operation is sorting the items by their value/weight ratio.
- The greedy solution for the fractional knapsack problem is optimal, meaning that it always gives the maximum possible value for the knapsack, because it satisfies the greedy choice property and the optimal substructure property:
  - The greedy choice property states that a globally optimal solution can be obtained by making a locally optimal (greedy) choice at each step. In this case, the greedy choice is to take the item with the highest value/weight ratio that fits in the knapsack.
  - The optimal substructure property states that an optimal solution to a problem can be constructed from optimal solutions to its subproblems. In this case, the subproblems are the remaining items and the remaining capacity of the knapsack after each greedy choice.