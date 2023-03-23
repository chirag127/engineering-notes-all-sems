 Here is the content in markdown format:

### Dynamic Programming with Examples Such as Knapsack

- Dynamic Programming is a technique to solve complex problems by breaking them down into smaller subproblems.
- It solves each subproblem only once, and then saves its answer in a table. Each answer that is saved can be used to solve larger subproblems.
- This technique is useful for optimization problems, i. e. problems where we are trying to maximize or minimize something.

**Knapsack Problem:**

- Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.
- Formulation:
    - Let w[i] be the weight of item i
    - Let v[i] be the value of item i
    - Let W be the maximum weight our knapsack can hold
    - n be the number of items
- We solve it using Dynamic Programming with a table K[i][w] that stores the maximum value we can achieve using only the first i items and having a maximum weight of w for our knapsack.
- The recursion is:
K[i][w] = max(K[i-1][w], v[i] + K[i-1][w-w[i]]) if w[i] <= w else K[i-1][w]
- The base cases are: K[0][w] = 0 and K[i][0] = 0
- The optimal solution is K[n][W]

[Remaining content removed for brevity]