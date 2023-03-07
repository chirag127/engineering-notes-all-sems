 Here is the content in markdown format:

## Write programs to

**(a) Implement All-Pairs Shortest Paths problem using Floyd's algorithm.**

- Floyd's algorithm is used to find shortest distances between every pair of vertices in a given edge weighted directed Graph.
- It solves the All-Pairs Shortest Path problem and runs in O(V^3) time, where V is the number of vertices in the graph.
- The algorithm works as follows:
  - Initialize the solution matrix same as the input graph matrix as a first step.
  - Then, update each entry (i, j) in the solution matrix by checking all possible intermediate vertices k and updating the i-j distance if a shorter path exists.
- Pseudocode:
  ```
  Initialize solution matrix D same as input graph matrix G
  for k = 1 to n
    for i = 1 to n
      for j = 1 to n
        D[i][j] = min(D[i][j], D[i][k] + D[k][j])
  ```
- Example:
  ```
  Input:  G = [[0, 5, INF, 10],
              [INF, 0, 3, INF],
              [INF, INF, 0, 1],
              [INF, INF, INF, 0]]
  
  Output: D = [[0, 5, 8, 9],
              [INF, 0, 3, 4],
              [INF, INF, 0, 1],
              [INF, INF, INF, 0]]
  ```
- Advantages: Simple and efficient. Handles negative weight cycles.
- Disadvantages: Higher order of growth.
- Applications: Finding shortest paths in networks, transportation problem, etc.

**(b) Implement Travelling Sales Person problem using Dynamic programming.**

- The Travelling Salesman Problem (TSP) is the problem of finding the shortest route to visit each city and return to the origin city.
- Dynamic Programming solves TSP by breaking the problem into subproblems and storing the solutions to subproblems to avoid re-computation.
- The steps are:
  1. Create a table tsp[n][1<<n] to store results of subproblems
  2. For every subset S of cities, find the cost of shortest Hamiltonian cycle in S and store in tsp[n][S]
  3. The final answer is tsp[n][(1<<n) - 1]
- The time complexity is O(n2^n) which makes it suitable only for small values of n.
- An example is as follows:
  ```
  Let cities be {1, 2, 3, 4} and distances be
  1-2: 5      2-3: 3      3-4: 6      4-1: 8
  tsp = {{}, {1}, {2}, {1, 2}, {3}, {1, 3}, {2, 3}, {1, 2, 3}, {4}, {1, 4}, {2, 4}, {1, 2, 4}, {3, 4}, {1, 3, 4},
         {2, 3, 4}, {1, 2, 3, 4}}
  tsp[4][{1, 2, 3, 4}] = min(tsp[3][{1, 2, 3}] + dist(3, 4) + dist(4, 1),
                              tsp[3][{1, 2, 4}] + dist(2, 3) + dist(3, 1),
                              tsp[3][{1, 3, 4}] + dist(2, 4) + dist(4, 1),
                              tsp[3][{2, 3, 4}] + dist(1, 2) + dist(2, 1))
  = min(9 + 6 + 8, 9 + 3 + 5, 9 + 6 + 5, 9 + 5 + 5) = 25
  ```
- Advantages: Optimal substructure and overlapping subproblems.
- Disadvantages: Exponential time complexity.
- Applications: Finding optimal routes, logistics, etc.