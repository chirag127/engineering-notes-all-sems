# Dynamic Programming with Examples Such as Resource Allocation Problem

## What is Dynamic Programming?

- Dynamic programming is a technique for solving optimization problems that have overlapping subproblems and optimal substructure.
- Overlapping subproblems means that the same subproblem is solved repeatedly, and optimal substructure means that the optimal solution of a problem can be obtained from the optimal solutions of its subproblems.
- Dynamic programming can be applied to both discrete and continuous problems, and can be implemented using either a top-down (memoization) or a bottom-up (tabulation) approach.
- Dynamic programming can reduce the time complexity of solving a problem from exponential to polynomial, by avoiding recomputation of subproblems and storing the results in a table or an array.

## Resource Allocation Problem

- A resource allocation problem is a type of optimization problem where a resource or resources are allocated to a number of independent activities in order to maximize the total return or minimize the total cost.
- A resource allocation problem can be formulated as a dynamic programming problem if the following conditions are met:
  - The resource or resources are divisible and can be allocated in fractional units.
  - The activities are ordered and the allocation of a resource to an activity depends only on the amount of resource available and the previous allocations.
  - The return or cost function of each activity is concave or convex, respectively, and satisfies the principle of diminishing returns or increasing costs, respectively.
- A resource allocation problem can be solved using dynamic programming by defining the following elements:
  - The state variable: the amount of resource available at each stage (activity).
  - The decision variable: the amount of resource allocated to each activity.
  - The state transition equation: the relation between the state variables of consecutive stages.
  - The return or cost function: the function that gives the return or cost of allocating a certain amount of resource to an activity.
  - The objective function: the function that gives the total return or cost of allocating the resource to all the activities.
  - The boundary conditions: the initial and final values of the state variable.

## Example: Resource Allocation Problem with One Resource and N Activities

- Suppose there is one resource with X units available, and N activities that can use the resource. The return from allocating x units of resource to activity k is given by r_k(x), where r_k(x) is a concave function and satisfies r_k(0) = 0 and r_k'(x) > 0 for all x > 0. The objective is to maximize the total return from allocating the resource to all the activities.
- The dynamic programming formulation of this problem is as follows:
  - The state variable: x_k, the amount of resource available after allocating to activity k, for k = 0, 1, ..., N. Note that x_0 = X and x_N = 0.
  - The decision variable: x_k - x_k+1, the amount of resource allocated to activity k+1, for k = 0, 1, ..., N-1.
  - The state transition equation: x_k+1 = x_k - (x_k - x_k+1), for k = 0, 1, ..., N-1.
  - The return function: r_k+1(x_k - x_k+1), the return from allocating x_k - x_k+1 units of resource to activity k+1, for k = 0, 1, ..., N-1.
  - The objective function: R(x_0, x_1, ..., x_N) = sum_{k=0}^{N-1} r_k+1(x_k - x_k+1), the total return from allocating the resource to all the activities.
  - The boundary conditions: x_0 = X and x_N = 0.
- The optimal solution of this problem can be obtained by using the following recursive relation:

  - R(x_k, x_k+1, ..., x_N) = max_{0 <= x_k - x_k+1 <= x_k} {r_k+1(x_k - x_k+1) + R(x_k+1, x_k+2, ..., x_N)}, for k = 0, 1, ..., N-1.
  - R(x_N) = 0.

- The optimal allocation of the resource to each activity can be found by tracing back the optimal values of x_k, for k = 0, 1, ..., N.