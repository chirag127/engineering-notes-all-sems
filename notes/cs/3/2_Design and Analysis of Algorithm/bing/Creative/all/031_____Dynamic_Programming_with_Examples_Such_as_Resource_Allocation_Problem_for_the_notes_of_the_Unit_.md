# Dynamic Programming with Examples Such as Resource Allocation Problem

- Dynamic programming is a technique for solving optimization problems that have overlapping subproblems and optimal substructure.
- Overlapping subproblems means that the same subproblem is solved repeatedly, and optimal substructure means that the optimal solution of a problem can be obtained from the optimal solutions of its subproblems.
- Dynamic programming can be applied to both discrete and continuous problems, and can be implemented using either a top-down (memoization) or a bottom-up (tabulation) approach.
- A common example of a dynamic programming problem is the knapsack problem, where we have a set of items, each with a weight and a value, and we want to find the maximum value we can obtain by choosing a subset of items that fit in a knapsack with a given capacity.
- Another example of a dynamic programming problem is the resource allocation problem, where we have a set of resources and a set of activities, and we want to find the optimal way to allocate the resources to the activities to maximize the total return.
- The resource allocation problem can be formulated as follows:

  - Let N be the number of activities, and let X be the total amount of resources available.
  - Let x_k be the amount of resources allocated to activity k, and let r_k(x_k) be the return function of activity k, which gives the return from allocating x_k units of resources to activity k.
  - The objective is to maximize the total return, R(x_1, x_2, ..., x_N) = r_1(x_1) + r_2(x_2) + ... + r_N(x_N), subject to the constraint that the sum of the allocated resources does not exceed the total amount available, x_1 + x_2 + ... + x_N <= X.
  - The problem can be solved using dynamic programming by defining a subproblem as follows:

    - Let R_k(x) be the maximum return that can be obtained by optimally allocating x units of resources to the first k activities, 1 <= k <= N.
    - The base case is R_1(x) = r_1(x) for 0 <= x <= X, since there is only one activity to allocate resources to.
    - The recursive case is R_k(x) = max{R_k-1(x), R_k-1(x - x_k) + r_k(x_k)} for 1 < k <= N and 0 <= x <= X, since we can either not allocate any resources to activity k, or allocate x_k units of resources to activity k and the remaining x - x_k units to the first k - 1 activities.
    - The optimal solution is R_N(X), which gives the maximum return from allocating X units of resources to N activities.
    - The optimal allocation can be obtained by tracing back the decisions made at each stage of the recursion.

- A numerical example of the resource allocation problem is as follows:

  - Suppose there are three activities, A, B, and C, and 10 units of resources available.
  - The return functions of the activities are:

    - r_A(x) = 10x - x^2 for 0 <= x <= 10
    - r_B(x) = 12x - x^2 for 0 <= x <= 12
    - r_C(x) = 15x - x^2 for 0 <= x <= 15

  - The dynamic programming table for this problem is shown below, where each cell contains the value of R_k(x) and the corresponding allocation to activity k.

| x \ k | 1 (A) | 2 (B) | 3 (C) |
| ----- | ----- | ----- | ----- |
| 0     | 0 (0) | 0 (0) | 0 (0) |
| 1     | 9 (1) | 11 (1) | 14 (1) |
| 2     | 16 (2) | 20 (2) | 26 (2) |
| 3     | 21 (3) | 27 (3) | 36 (3) |
| 4     | 24 (4) | 32 (4) | 44 (4) |
| 5     | 25 (5) | 35 (5) | 50 (5) |
| 6     | 24 (6) | 36 (6) | 54 (6) |
| 7     | 21 (7