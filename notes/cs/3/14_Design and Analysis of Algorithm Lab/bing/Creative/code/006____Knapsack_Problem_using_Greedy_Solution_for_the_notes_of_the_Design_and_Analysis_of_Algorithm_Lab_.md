## Knapsack Problem using Greedy Solution

- The knapsack problem is a problem of finding the optimal way to fill a knapsack with a given capacity and a set of items, each with a value and a weight.
- The fractional knapsack problem is a variation of the knapsack problem, where the items can be divided into smaller pieces and the knapsack can be filled with fractions of items.
- The greedy solution for the fractional knapsack problem is an efficient and optimal method that works as follows   :
  - Sort the items by their value-to-weight ratio in descending order.
  - Start with the item with the highest ratio and take as much of it as possible, until the knapsack is full or the item is exhausted.
  - If the knapsack is not full and there are more items, move to the next item with the next highest ratio and repeat the previous step.
  - Continue this process until the knapsack is full or there are no more items.
- The greedy solution for the fractional knapsack problem has a time complexity of O(n log n), where n is the number of items, because the sorting step dominates the algorithm.
- The greedy solution for the fractional knapsack problem is optimal because at each step, it chooses the item that gives the maximum value per unit weight, which maximizes the total value of the knapsack.
- The greedy solution for the fractional knapsack problem does not work for the 0-1 knapsack problem, where the items cannot be divided and the knapsack can only be filled with whole items. In this case, the greedy solution may not find the optimal solution, because it may miss some combinations of items that have a higher total value than the greedy choice.
- An example of the fractional knapsack problem using the greedy solution is shown below:

  - Suppose we have a knapsack with a capacity of 15 kg and four items with the following values and weights:

    | Item | Value | Weight | Value/Weight |
    | ---- | ----- | ------ | ------------ |
    | A    | 10    | 2      | 5            |
    | B    | 5     | 3      | 1.67         |
    | C    | 15    | 5      | 3            |
    | D    | 7     | 7      | 1            |

  - The first step is to sort the items by their value-to-weight ratio in descending order:

    | Item | Value | Weight | Value/Weight |
    | ---- | ----- | ------ | ------------ |
    | A    | 10    | 2      | 5            |
    | C    | 15    | 5      | 3            |
    | B    | 5     | 3      | 1.67         |
    | D    | 7     | 7      | 1            |

  - The second step is to start with the item with the highest ratio, which is A, and take as much of it as possible. Since the weight of A is 2 kg and the capacity of the knapsack is 15 kg, we can take the whole item A and put it in the knapsack. The value of the knapsack is now 10 and the remaining capacity is 13 kg.

  - The third step is to move to the next item with the next highest ratio, which is C, and take as much of it as possible. Since the weight of C is 5 kg and the remaining capacity of the knapsack is 13 kg, we can also take the whole item C and put it in the knapsack. The value of the knapsack is now 25 and the remaining capacity is 8 kg.

  - The fourth step is to move to the next item with the next highest ratio, which is B, and take as much of it as possible. Since the weight of B is 3 kg and the remaining capacity of the knapsack is 8 kg, we can also take the whole item B and put it in the knapsack. The value of the knapsack is now 30 and the remaining capacity is 5 kg.

  - The fifth step is to move to the last item, which is D, and take as much of it as possible. Since the weight of D is 7 kg and