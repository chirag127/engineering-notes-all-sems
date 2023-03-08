## Implement the 0/1 Knapsack problem using (a) Dynamic Programming method (b) Greedy method.

The 0/1 Knapsack problem is a classic optimization problem that involves maximizing the total value of items that can be put into a knapsack with a limited weight capacity. In this lab, we will learn how to solve this problem using two different methods - Dynamic Programming and Greedy.

### Dynamic Programming Method

Dynamic Programming is a technique that involves solving a problem by breaking it down into smaller subproblems and solving them recursively. The 0/1 Knapsack problem can be solved using Dynamic Programming in the following steps:

1. Create a table of size (n+1) x (W+1), where n is the number of items and W is the maximum weight capacity of the knapsack.
2. Initialize the first row and column of the table to 0.
3. For each item i, starting from the second row, calculate the maximum value that can be obtained by either including or excluding the item in the knapsack.
4. Fill the table row-wise, using the following formula:
   - If the weight of the current item is greater than the capacity of the knapsack, then the maximum value that can be obtained is the same as that of the previous row.
   - Otherwise, the maximum value that can be obtained is the maximum of the value of the previous row and the value of the current item + value of the item that can be obtained by reducing the remaining capacity of the knapsack.
5. The final value in the bottom-right corner of the table is the maximum value that can be obtained.

#### Advantages of Dynamic Programming Method

- Guarantees an optimal solution
- Can handle cases where items have fractional weights

#### Disadvantages of Dynamic Programming Method

- Requires a lot of memory and computation time for large inputs
- Not suitable for cases where items have negative weights or values

### Greedy Method

The Greedy method involves making locally optimal choices at each step in the hope of finding a global optimum. In the case of the 0/1 Knapsack problem, the Greedy method involves sorting the items in descending order of their value-to-weight ratio and then adding them to the knapsack in that order until the knapsack is full.

#### Advantages of Greedy Method

- Simpler and faster than Dynamic Programming for smaller inputs
- Can handle cases where items have negative weights or values

#### Disadvantages of Greedy Method

- Does not always guarantee an optimal solution
- Can produce suboptimal solutions for certain inputs

### Example

Consider the following input:

```
Number of items: 4
Maximum weight capacity: 7
Item 1: (value = 5, weight = 3)
Item 2: (value = 2, weight = 1)
Item 3: (value = 3, weight = 2)
Item 4: (value = 4, weight = 1)
```

Using Dynamic Programming, we can create the following table:

```
   0  1  2  3  4  5  6  7
0  0  0  0  0  0  0  0  0
1  0  0  0  5  5  5  5  5
2  0  2  2  5  7  7  7  7
3  0  2  3  5  7  8 10 10
4  0  4  4  7  9 10 12 13
```

The maximum value that can be obtained is 13.

Using the Greedy method, we can sort the items in descending order of their value-to-weight ratio:

```
Item 1: (value = 5, weight = 3, ratio = 5/3)
Item 4: (value = 4, weight = 1, ratio = 4/1)
Item 3: (value = 3, weight = 2, ratio = 3/2)
Item 2: (value = 2, weight = 1, ratio = 2/1)
```

We can then add the items to the knapsack in that order until the knapsack is full. The maximum value that can be obtained is 12.

### Applications

The 0/1 Knapsack problem has applications in various fields such as finance, logistics, and resource allocation. It is often used in portfolio optimization, where the goal is to maximize the return on investment subject to constraints on the total investment amount and the risk involved. It is also used in supply chain management, where the goal is to optimize the allocation of