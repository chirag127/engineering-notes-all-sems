### Dynamic Programming with Examples Such as Resource Allocation Problem

- Dynamic programming is a technique for solving optimization problems that have overlapping subproblems and optimal substructure.
- Overlapping subproblems means that the same subproblem is solved repeatedly, and optimal substructure means that the optimal solution of a problem can be obtained from the optimal solutions of its subproblems.
- Dynamic programming can be applied to both discrete and continuous problems, and can be implemented using either a top-down (memoization) or a bottom-up (tabulation) approach.
- One example of a dynamic programming problem is the resource allocation problem, where a limited amount of resources (such as time, money, or materials) needs to be allocated to a number of activities (such as projects, tasks, or locations) in order to maximize the total return (such as profit, utility, or satisfaction).
- The resource allocation problem can be formulated as follows:

  - Let N be the number of activities, and let X be the total amount of resources available.
  - Let x_k be the amount of resources allocated to activity k, and let r_k(x_k) be the return function of activity k, which gives the return from allocating x_k resources to activity k.
  - The objective is to find the optimal allocation x* = (x*_1, x*_2, ..., x*_N) that maximizes the total return R(x) = sum_{k=1}^N r_k(x_k), subject to the constraint sum_{k=1}^N x_k <= X and x_k >= 0 for all k.

- The resource allocation problem can be solved using dynamic programming by defining a subproblem as follows:

  - Let R_k(x) be the maximum return that can be obtained by allocating x resources to the first k activities, and let x*_k be the optimal amount of resources allocated to activity k in this subproblem.
  - The base case is R_0(x) = 0 for all x, which means that no return can be obtained by allocating resources to zero activities.
  - The recursive relation is R_k(x) = max_{0 <= x_k <= x} {R_{k-1}(x - x_k) + r_k(x_k)} for k = 1, 2, ..., N, which means that the optimal return for allocating x resources to the first k activities is obtained by choosing the optimal amount of resources x_k to allocate to activity k, and adding it to the optimal return for allocating the remaining x - x_k resources to the first k - 1 activities.
  - The optimal solution is R_N(X), which gives the maximum return for allocating X resources to all N activities, and the optimal allocation x* can be obtained by tracing back the values of x*_k from the subproblems.

- An example of a resource allocation problem is the following:

  - Suppose there are three activities, A, B, and C, and 10 units of resources available.
  - The return functions of the activities are r_A(x) = 10x - x^2, r_B(x) = 12x - x^2, and r_C(x) = 15x - x^2, which are concave and have a maximum at x = 5, 6, and 7.5, respectively.
  - The optimal allocation can be found by using dynamic programming as follows:

    - R_0(x) = 0 for all x
    - R_1(x) = max_{0 <= x_1 <= x} {R_0(x - x_1) + r_A(x_1)} = max_{0 <= x_1 <= x} {10x_1 - x_1^2}
    - R_2(x) = max_{0 <= x_2 <= x} {R_1(x - x_2) + r_B(x_2)} = max_{0 <= x_2 <= x} {max_{0 <= x_1 <= x - x_2} {10x_1 - x_1^2} + 12x_2 - x_2^2}
    - R_3(x) = max_{0 <= x_3 <= x} {R_2(x - x_3) + r_C(x_3)} = max_{0 <= x_3 <= x} {max_{0 <= x_2 <= x - x_3} {max_{0 <= x_1 <= x - x_2 - x_3} {10x_1 - x_1^2