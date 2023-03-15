# Dynamic Programming with Examples Such as Resource Allocation Problem

- Dynamic programming is a technique for solving optimization problems that have overlapping subproblems and optimal substructure.
- A problem has overlapping subproblems if the same subproblem is solved repeatedly in the process of finding the optimal solution.
- A problem has optimal substructure if the optimal solution of the original problem can be obtained by combining the optimal solutions of its subproblems.
- Dynamic programming can be applied to both discrete and continuous problems, and can handle deterministic or stochastic transitions.
- The main idea of dynamic programming is to break down a complex problem into simpler subproblems, and store the results of these subproblems in a table or a matrix, so that they can be reused later.
- The general steps of dynamic programming are:

  1. Identify the state variables that describe the problem.
  2. Define the optimal value function that gives the maximum (or minimum) return for each state.
  3. Find the recurrence relation that relates the optimal value function of a state to the optimal value functions of its successor states.
  4. Solve the recurrence relation using a bottom-up or a top-down approach, and fill in the table or matrix with the optimal values.
  5. Trace back the optimal solution from the final state to the initial state, using the table or matrix.

- An example of a problem that can be solved by dynamic programming is the resource allocation problem, where a fixed amount of a resource (such as money, time, or energy) has to be allocated to a number of independent activities (such as projects, tasks, or investments) in order to maximize the total return (such as profit, utility, or satisfaction).
- The resource allocation problem can be formulated as follows:

  - Let N be the number of activities, and M be the amount of resource available.
  - Let R(i,j) be the return obtained from allocating j units of resource to activity i, where i = 1, 2, ..., N and j = 0, 1, ..., M.
  - Let x(i) be the amount of resource allocated to activity i, where x(i) is an integer between 0 and M, and the sum of x(i) over all i is equal to M.
  - The objective is to find the optimal allocation x(i) for all i that maximizes the total return R(x) = sum of R(i,x(i)) over all i.

- The resource allocation problem can be solved by dynamic programming as follows:

  1. The state variables are the activity index i and the remaining resource x.
  2. The optimal value function is S(i,x), which gives the maximum return obtainable from activities i through N, given x units of resource remaining to be allocated.
  3. The recurrence relation is S(i,x) = max of R(i,j) + S(i+1,x-j) over all j = 0, 1, ..., x, with the base case S(N+1,x) = 0 for all x.
  4. The recurrence relation can be solved by a bottom-up approach, starting from i = N and x = 0, and filling in a table of size (N+1) x (M+1) with the optimal values S(i,x).
  5. The optimal solution can be traced back from S(1,M) by finding the value of j that maximizes R(1,j) + S(2,M-j), and then repeating the same process for i = 2, 3, ..., N. The optimal allocation is x(i) = j for each i.