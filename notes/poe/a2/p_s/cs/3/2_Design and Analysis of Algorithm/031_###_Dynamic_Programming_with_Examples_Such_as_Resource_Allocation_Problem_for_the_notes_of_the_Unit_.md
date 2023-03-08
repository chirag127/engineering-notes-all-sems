 Here are the notes for the topic ### Dynamic Programming with Examples Such as Resource Allocation Problem:

Dynamic Programming is a technique to solve complex problems by breaking them down into smaller subproblems. It solves each subproblem only once, and then saves its answer in a table. Each answer that is saved can be used to solve larger subproblems.

This technique is useful for optimization problems exhibiting optimal substructures. A problem exhibits optimal substructure if an optimal solution can be constructed from optimal solutions of its subproblems.

Some key steps to solve a problem using Dynamic Programming are:

1. Identify if the problem exhibits optimal substructure and overlapping subproblems.
2. Formulate the recurrence relation between subproblems.
3. Evaluate the base cases.
4. Construct a table (array) to store the solutions to subproblems.
5. Use the table to solve the original problem.

Example: Resource Allocation Problem

Given: n resources and m tasks. Each task requires a specific amount of each resource. Determine if it is possible to allocate resources to tasks such that all tasks can be completed.

This problem can be solved using Dynamic Programming by following the steps:

1. The problem exhibits optimal substructure as optimal allocation of resources to first i-1 tasks can be used to determine allocation for i'th task. There are overlapping subproblems as allocations for previous tasks are reused.
2. The recurrence relation is:

is_possible(i) = is_possible(i-1)        // If task i can be allocated using remaining resources
                    OR
                    is_possible(i-1) && (resource_available >= resource_required_for_task_i)   // If new task i can be accommodated

3. Base cases are: is_possible(0) = True and is_possible(1) = (resource_available >= resource_required_for_task_1)
4. Construct a table (array) to store results of subproblems.
5. Return is_possible(n-1) where n is the number of tasks.

This Dynamic Programming based solution has time and space complexity of O(mn) where m is number of tasks and n is number of resources.