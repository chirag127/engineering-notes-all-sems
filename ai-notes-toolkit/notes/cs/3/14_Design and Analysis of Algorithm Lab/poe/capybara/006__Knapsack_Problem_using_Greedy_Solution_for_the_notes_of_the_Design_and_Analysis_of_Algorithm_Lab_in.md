## Knapsack Problem using Greedy Solution

The Knapsack Problem is a classic optimization problem in Computer Science. It involves selecting a set of items to maximize the value of the items selected, subject to a constraint on the total weight of the items selected.

Greedy algorithms are a class of algorithms that make locally optimal choices at each step in the hope of finding a global optimum solution. The Greedy approach for the Knapsack Problem involves selecting the items with the highest value-to-weight ratio first.

### Algorithm

1. Sort the items by value-to-weight ratio in descending order.
2. Initialize the total value and total weight to 0.
3. For each item, in order from highest value-to-weight ratio to lowest:
   - If adding the item to the knapsack would not exceed the maximum weight, add the item to the knapsack and update the total value and total weight.
   - If adding the item would exceed the maximum weight, skip the item.
4. Return the total value and total weight of the items in the knapsack.

### Time Complexity

The time complexity of the Greedy approach for the Knapsack Problem is O(n log n), where n is the number of items. This is due to the sorting step that is required before the algorithm can begin.

### Space Complexity

The space complexity of the Greedy approach for the Knapsack Problem is O(n), where n is the number of items. This is due to the need to store the weight and value of each item.

### Advantages

1. The Greedy approach for the Knapsack Problem is simple to implement and easy to understand.
2. It provides a good approximation of the optimal solution for many instances of the problem.
3. It runs in polynomial time, making it efficient for small to medium-sized instances of the problem.

### Disadvantages

1. The Greedy approach for the Knapsack Problem does not guarantee an optimal solution in all cases.
2. It can be outperformed by other algorithms for certain types of instances of the problem.
3. It is not suitable for instances of the problem with non-linear relationships between item value and weight.