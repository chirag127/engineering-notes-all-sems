## Write programs to (a) Implement All-Pairs Shortest Paths problem using Floyd's algorithm. (b) Implement Travelling Sales Person problem using Dynamic programming.

### Introduction
In the subject of Real Time System, Design and Analysis of Algorithm Lab, we will learn about two important algorithms - Floyd's algorithm for the All-Pairs Shortest Paths problem and Dynamic programming for the Travelling Sales Person problem. These algorithms are widely used in various applications such as network routing, transportation planning, and logistics optimization.

### Implementation of All-Pairs Shortest Paths problem using Floyd's algorithm
Floyd's algorithm is used to find the shortest path between all pairs of vertices in a weighted graph. The steps to implement Floyd's algorithm are as follows:

1. Create a 2D array `dist` of size `n x n`, where `n` is the number of vertices in the graph. Initialize the array with the weight of the edges between the vertices. If there is no edge between two vertices, set the distance to infinity.
2. Use a nested loop to iterate through all pairs of vertices `i` and `j`. For each pair, check if there exists a vertex `k` such that the path from `i` to `k` and from `k` to `j` is shorter than the current distance between `i` and `j`. If such a vertex exists, update the distance between `i` and `j` with the sum of the distances from `i` to `k` and from `k` to `j`.
3. After completing the loop, the `dist` array will contain the shortest distance between all pairs of vertices.

### Implementation of Travelling Sales Person problem using Dynamic programming
The Travelling Sales Person problem is a combinatorial optimization problem where the goal is to find the shortest possible route that visits every city exactly once and returns to the starting city. Dynamic programming can be used to solve this problem efficiently. The steps to implement Dynamic programming for the Travelling Sales Person problem are as follows:

1. Create a 2D array `dp` of size `2^n x n`, where `n` is the number of cities. Initialize the array with a large value.
2. Set `dp[0][0]` to 0.
3. Use a nested loop to iterate through all possible subsets of cities `S` of size `i`. For each subset, iterate through all cities `j` in the subset. For each city `j`, calculate the minimum cost of reaching `j` from any other city `k` in the subset `S`. Update `dp[S][j]` with this minimum cost.
4. After completing the loop, the minimum cost of visiting all cities exactly once and returning to the starting city will be the minimum value in the last row of the `dp` array.

### Advantages of Floyd's algorithm and Dynamic programming
1. Floyd's algorithm is simple to implement and guarantees to find the shortest path between all pairs of vertices in a graph.
2. Dynamic programming is a powerful technique that can be used to solve a wide range of optimization problems efficiently.

### Disadvantages of Floyd's algorithm and Dynamic programming
1. Floyd's algorithm has a time complexity of O(n^3) and requires a lot of memory for large graphs.
2. Dynamic programming can be difficult to implement and requires careful analysis of the problem to find the optimal substructure.

### Applications of Floyd's algorithm and Dynamic programming
1. Floyd's algorithm is used in network routing algorithms, where the shortest path between all pairs of nodes needs to be calculated.
2. Dynamic programming is used in various optimization problems such as resource allocation, production planning, and scheduling.

### Conclusion
In the Design and Analysis of Algorithm Lab in the subject of Real Time System, we learned about two important algorithms - Floyd's algorithm for the All-Pairs Shortest Paths problem and Dynamic programming for the Travelling Sales Person problem. These algorithms have a wide range of applications and are essential tools for solving optimization problems efficiently.