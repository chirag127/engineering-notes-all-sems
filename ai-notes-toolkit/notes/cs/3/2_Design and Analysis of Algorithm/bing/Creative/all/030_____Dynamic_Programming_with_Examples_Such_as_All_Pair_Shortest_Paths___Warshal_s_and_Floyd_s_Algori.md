Hello, I am Sydney, your AI assistant. I can help you with your topic of dynamic programming with examples such as all pair shortest paths, Warshal's and Floyd's algorithms, resource allocation problem, etc. Here are some notes that I have prepared for you based on the web search results:

# Dynamic Programming with Examples

## What is Dynamic Programming?

- Dynamic programming is a technique of solving complex problems by breaking them down into smaller subproblems and reusing the solutions of the subproblems to avoid repeated computations .
- Dynamic programming can be applied to problems that have two main characteristics: optimal substructure and overlapping subproblems.
- Optimal substructure means that the optimal solution of a problem can be obtained by using the optimal solutions of its subproblems.
- Overlapping subproblems means that the same subproblems are encountered multiple times while solving the problem.
- Dynamic programming can be implemented using two approaches: top-down (memoization) or bottom-up (tabulation).
- Top-down approach involves starting from the original problem and recursively solving the subproblems, while storing the results of the subproblems in a data structure (such as an array or a map) to avoid recomputation.
- Bottom-up approach involves starting from the base cases (the smallest subproblems) and iteratively building up the solutions of larger subproblems using the results of the smaller ones.

## Examples of Dynamic Programming Problems

### Fibonacci Sequence

- The Fibonacci sequence is the series of numbers where each number is the sum of the two preceding ones, starting from 0 and 1.
- The Fibonacci sequence can be defined recursively as:

  - F(0) = 0
  - F(1) = 1
  - F(n) = F(n-1) + F(n-2) for n > 1

- The Fibonacci sequence is an example of a problem that has optimal substructure and overlapping subproblems, and can be solved using dynamic programming.
- A naive recursive solution would involve calling the same function multiple times with the same arguments, leading to exponential time complexity.
- A dynamic programming solution would involve storing the results of the subproblems in an array and using them to calculate the results of larger subproblems, leading to linear time complexity.

### Knapsack Problem

- The knapsack problem is a problem of finding the maximum value of items that can be packed into a knapsack with a given weight capacity.
- The knapsack problem can be defined as:

  - Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.
  - The items are indivisible, meaning that they cannot be split or fractioned.

- The knapsack problem is an example of a problem that has optimal substructure and overlapping subproblems, and can be solved using dynamic programming.
- A naive recursive solution would involve trying all possible combinations of items and selecting the one with the maximum value, leading to exponential time complexity.
- A dynamic programming solution would involve using a two-dimensional array to store the maximum value that can be obtained for each subproblem (i.e., each combination of items and weight capacity), and using them to calculate the results of larger subproblems, leading to polynomial time complexity.

### All Pair Shortest Paths

- The all pair shortest paths problem is a problem of finding the shortest distances between every pair of vertices in a weighted graph.
- The all pair shortest paths problem can be defined as:

  - Given a weighted graph G = (V, E), where V is the set of vertices, E is the set of edges, and each edge has a weight w(u, v) representing the distance between vertices u and v, find the shortest distance d(u, v) for every pair of vertices u and v in V.
  - The graph may or may not contain negative edge weights, but it should not contain negative cycles (i.e., cycles whose total weight is negative).

- The all pair shortest paths problem is an example of a problem that has optimal substructure and overlapping subproblems, and can be solved using dynamic programming.
- Two common dynamic programming algorithms for solving the all pair shortest paths problem are Warshal's algorithm and Floyd's algorithm.
- Warshal's algorithm is