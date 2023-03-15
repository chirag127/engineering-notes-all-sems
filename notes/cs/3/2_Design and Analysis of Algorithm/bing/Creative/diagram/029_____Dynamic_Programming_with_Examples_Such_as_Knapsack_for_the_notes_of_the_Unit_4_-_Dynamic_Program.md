# Dynamic Programming with Examples Such as Knapsack

## What is Dynamic Programming?

- Dynamic programming is a technique for solving problems that have overlapping subproblems and optimal substructure.
- Overlapping subproblems means that the same subproblem is solved multiple times in the process of solving the larger problem.
- Optimal substructure means that the optimal solution of the larger problem can be obtained by combining the optimal solutions of the subproblems.
- Dynamic programming reduces the time complexity of solving problems by storing and reusing the solutions of the subproblems, instead of recomputing them.
- Dynamic programming can be applied to problems that can be divided into stages, where each stage has a set of states and decisions.
- The goal is to find an optimal sequence of decisions that leads to the optimal final state.

## How to Solve Problems using Dynamic Programming?

- To solve a problem using dynamic programming, we need to follow these steps:
  - Identify the stages, states, and decisions of the problem.
  - Define a recurrence relation that relates the optimal value of a state to the optimal values of its substates.
  - Initialize the base cases of the recurrence relation.
  - Fill up a table or an array that stores the optimal values of all the states, following a bottom-up or a top-down approach.
  - Trace back the optimal sequence of decisions from the final state, using the table or the array.

## What is the Knapsack Problem?

- The knapsack problem is a classic example of a problem that can be solved using dynamic programming.
- The problem statement is as follows:

  - Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight doesn't exceed a given limit and the total value is as large as possible.

- The knapsack problem can be divided into two variants: the 0/1 knapsack problem and the fractional knapsack problem.
- In the 0/1 knapsack problem, we can either include an item completely or not at all in the collection.
- In the fractional knapsack problem, we can include a fraction of an item in the collection.

## How to Solve the 0/1 Knapsack Problem using Dynamic Programming?

- To solve the 0/1 knapsack problem using dynamic programming, we can follow these steps:

  - Identify the stages, states, and decisions of the problem.
    - The stages are the items, from 1 to n.
    - The states are the remaining capacity of the knapsack, from 0 to W.
    - The decisions are whether to include or exclude an item in the collection.
  - Define a recurrence relation that relates the optimal value of a state to the optimal values of its substates.
    - Let V[i][w] be the optimal value of the collection when we have items from 1 to i and the remaining capacity of the knapsack is w.
    - Then, we have two cases:
      - If we exclude item i, then V[i][w] = V[i-1][w].
      - If we include item i, then V[i][w] = V[i-1][w-wi] + vi, where wi and vi are the weight and value of item i, respectively.
    - However, we can only include item i if w >= wi, otherwise it would exceed the capacity of the knapsack.
    - Therefore, the recurrence relation is:

      - V[i][w] = max(V[i-1][w], V[i-1][w-wi] + vi) if w >= wi
      - V[i][w] = V[i-1][w] otherwise

  - Initialize the base cases of the recurrence relation.
    - When we have no items, the optimal value of the collection is zero, regardless of the remaining capacity of the knapsack.
    - Therefore, V[0][w] = 0 for all w from 0 to W.
    - When we have no remaining capacity, the optimal value of the collection is zero, regardless of the items we have.
    - Therefore, V[i][0] = 0 for all i from 0 to n.
  - Fill up a table or an array that stores the optimal values of all the states, following a bottom-up or a top-down approach.
    - A bottom-up approach starts from the base cases and fills up the table in increasing order of the stages and the states.
    - A top-down approach starts from the final state and fills up the table