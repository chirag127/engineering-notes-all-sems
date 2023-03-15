## Knapsack Problem using Greedy Solution

- The knapsack problem is a problem of finding the optimal way to fill a knapsack with a given capacity and a set of items, each with a value and a weight.
- The fractional knapsack problem is a variant of the knapsack problem, where the items can be divided into smaller pieces and the knapsack can be filled with fractions of items.
- The greedy solution for the fractional knapsack problem is an efficient and optimal method, where the items are sorted by their value-to-weight ratio in descending order and the knapsack is filled with the highest ratio items first, until it is full or no more items are left.
- The algorithm for the greedy solution is as follows   :

  - Sort the items by their value-to-weight ratio in descending order.
  - Initialize the total value of the knapsack to zero and the remaining capacity of the knapsack to the given capacity.
  - For each item in the sorted list, do the following:
    - If the item's weight is less than or equal to the remaining capacity, then add the whole item to the knapsack, update the total value by adding the item's value, and update the remaining capacity by subtracting the item's weight.
    - If the item's weight is greater than the remaining capacity, then add a fraction of the item to the knapsack, such that the knapsack is filled to its capacity, update the total value by adding the fraction of the item's value, and update the remaining capacity to zero.
    - If the remaining capacity is zero, then stop the loop and return the total value of the knapsack.

- The time complexity of the greedy solution is O(n log n), where n is the number of items, since the sorting step takes O(n log n) time and the loop takes O(n) time.
- The greedy solution is optimal for the fractional knapsack problem, since it always chooses the item with the highest marginal value per unit weight, and thus maximizes the total value of the knapsack.
- The greedy solution is not optimal for the 0-1 knapsack problem, where the items cannot be divided and the knapsack can only be filled with whole items. In this case, the greedy solution may miss some better combinations of items that have lower value-to-weight ratios but higher total value.
- An example of the greedy solution for the fractional knapsack problem is shown below:

  - Given a knapsack with capacity 15 kg and four items with the following values and weights:

    | Item | Value | Weight | Value-to-weight ratio |
    |------|-------|--------|-----------------------|
    | A    | 10    | 2      | 5                     |
    | B    | 5     | 3      | 1.67                  |
    | C    | 15    | 5      | 3                     |
    | D    | 7     | 7      | 1                     |

  - Sort the items by their value-to-weight ratio in descending order:

    | Item | Value | Weight | Value-to-weight ratio |
    |------|-------|--------|-----------------------|
    | A    | 10    | 2      | 5                     |
    | C    | 15    | 5      | 3                     |
    | B    | 5     | 3      | 1.67                  |
    | D    | 7     | 7      | 1                     |

  - Initialize the total value of the knapsack to zero and the remaining capacity of the knapsack to 15 kg.
  - For each item in the sorted list, do the following:
    - For item A, the weight is 2 kg, which is less than the remaining capacity of 15 kg, so add the whole item to the knapsack, update the total value to 10, and update the remaining capacity to 13 kg.
    - For item C, the weight is 5 kg, which is less than the remaining capacity of 13 kg, so add the whole item to the knapsack, update the total value to 25, and update the remaining capacity to 8 kg.
    - For item B, the weight is 3 kg, which is less than the remaining capacity of 8 kg, so add the whole item to the knapsack, update the total