 Here are the notes on Dynamic Programming with Examples Such as Resource Allocation Problem:

### Dynamic Programming with Examples Such as Resource Allocation Problem

- Dynamic Programming is a technique to solve complex problems by breaking them down into smaller subproblems.
- It solves each subproblem only once, and then saves its answer in a table. Each answer that is saved can be used to solve larger subproblems.
- This technique avoids solving the same subproblem multiple times. It reduces the exponential time complexity of some problems to polynomial time complexity.
- Some key characteristics of problems that can be solved using Dynamic Programming are:

1. Optimal substructure: An optimal solution can be constructed from optimal solutions of its subproblems.
2. Overlapping subproblems: Subproblems are reused multiple times.
3. Tabulation: Subproblems are solved in a bottom-up fashion by filling a table ( DP array ).
4. Memorization: Top-down approach where results of subproblems are stored in a table to avoid redundant calculations.

- Some examples of problems solved using Dynamic Programming are:

1. Fibonacci Number: fib(n) = fib(n-1) + fib(n-2).
2. Knapsack Problem: Maximize profit within a given weight capacity.
3. Travelling Salesman Problem: Minimize distance travelled to visit each city only once.
4. Resource Allocation Problem: Allocate limited resources to tasks to maximize profit/outcome.

- In Resource Allocation Problem, we are given a set of resources and a set of tasks. Each task requires a specific amount of each resource and has a profit/outcome. We need to allocate resources to tasks to maximize the total profit/outcome while not exceeding the available resources. It can be solved using Dynamic Programming by filling a table bottom-up based on the optimal solutions of subproblems (subsets of tasks).