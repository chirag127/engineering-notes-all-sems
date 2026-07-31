### Dynamic Programming with Examples Such as Resource Allocation Problem

Dynamic Programming is a problem-solving technique that solves problems by breaking them down into smaller subproblems and solving each subproblem only once. The solutions to the subproblems are stored in a table and are used to solve the larger problem.

The Resource Allocation Problem is a classic example of a dynamic programming problem. In this problem, we have a set of resources and a set of tasks. Each task requires a certain amount of each resource, and we want to assign resources to tasks in a way that maximizes the total profit.

To solve the Resource Allocation Problem using dynamic programming, we can use the following steps:

1. Define the subproblems: We can define a subproblem as finding the maximum profit that can be obtained by assigning resources to a subset of the tasks.

2. Define the base case: The base case is when there are no tasks to assign resources to. In this case, the maximum profit is 0.

3. Define the recurrence relation: We can define the recurrence relation as follows:

   - Let P(i,j) be the maximum profit that can be obtained by assigning resources to the first i tasks, using j units of each resource.
   - Then, for each task i, we can either assign it resources or not assign it resources.
   - If we assign it resources, then the maximum profit is P(i-1,j-x) + p(i,x), where x is the amount of resources assigned to task i, and p(i,x) is the profit obtained by assigning x units of each resource to task i.
   - If we do not assign it resources, then the maximum profit is P(i-1,j).
   - Therefore, the recurrence relation is: P(i,j) = max(P(i-1,j-x) + p(i,x), P(i-1,j))

4. Solve the subproblems: We can solve the subproblems using dynamic programming by filling in a table with the values of P(i,j) for all i and j.

5. Construct the solution: Once we have filled in the table, we can construct the optimal solution by backtracking through the table.

Other examples of dynamic programming problems include the Knapsack problem, the All Pair Shortest Paths problem using Warshal’s and Floyd’s Algorithms, Backtracking, Branch and Bound with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets. These problems can also be solved using the same dynamic programming techniques as the Resource Allocation Problem.