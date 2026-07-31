# Dynamic Programming with Examples Such as All Pair Shortest Paths – Warshal’s and Floyd’s Algorithms

## What is Dynamic Programming?

- Dynamic programming is a technique for solving problems that have overlapping subproblems and optimal substructure .
- Overlapping subproblems means that the same subproblem is solved repeatedly, and optimal substructure means that the optimal solution of a problem can be obtained from the optimal solutions of its subproblems.
- Dynamic programming can be used to optimize the time and space complexity of recursive solutions by storing the results of subproblems in a table (memoization) or by computing the results of subproblems in a bottom-up manner (tabulation) .
- Dynamic programming can be applied to various types of problems, such as optimization, counting, and decision making.

## Examples of Dynamic Programming Problems

### Knapsack Problem

- Given a set of items, each with a weight and a value, determine the number of each item to include in a knapsack so that the total weight is less than or equal to a given limit and the total value is as large as possible.
- This problem has overlapping subproblems, because the optimal solution for a smaller knapsack can be used to find the optimal solution for a larger knapsack.
- This problem also has optimal substructure, because the optimal solution for a knapsack can be obtained by adding or excluding an item from the optimal solution for a smaller knapsack.
- A dynamic programming solution for this problem can use a two-dimensional array to store the maximum value that can be obtained for each weight limit and each item.
- The base case is when the weight limit or the number of items is zero, in which case the value is zero.
- The recursive case is when the weight limit or the number of items is positive, in which case the value is the maximum of two cases: including the current item (if it does not exceed the weight limit) or excluding the current item.

### All Pair Shortest Paths – Warshal’s and Floyd’s Algorithms

- Given a weighted graph, find the shortest path between every pair of vertices.
- This problem has overlapping subproblems, because the shortest path between two vertices can be composed of the shortest paths between intermediate vertices.
- This problem also has optimal substructure, because the shortest path between two vertices is the minimum of the shortest paths between them and all possible intermediate vertices.
- A dynamic programming solution for this problem can use a three-dimensional array to store the shortest distance between every pair of vertices for every possible number of intermediate vertices.
- The base case is when the number of intermediate vertices is zero, in which case the distance is the direct edge weight between the vertices (or infinity if there is no edge).
- The recursive case is when the number of intermediate vertices is positive, in which case the distance is the minimum of two cases: using the current intermediate vertex or not using it.
- Warshal's algorithm is a special case of this problem when the graph is unweighted and the distance is measured by the number of edges.
- Floyd's algorithm is a general case of this problem when the graph is weighted and the distance is measured by the sum of edge weights.