## Write programs to (a) Implement All-Pairs Shortest Paths problem using Floyd's algorithm. (b) Implement Travelling Sales Person problem using Dynamic programming.

In the Design and Analysis of Algorithm Lab, we will learn about two important problems in the field of algorithms - the All-Pairs Shortest Paths problem and the Travelling Sales Person problem. We will also learn to implement them using two popular algorithms, Floyd's algorithm and Dynamic programming, respectively. Let's discuss them in detail:

### All-Pairs Shortest Paths problem

The All-Pairs Shortest Paths problem is to find the shortest path between all pairs of vertices in a given graph. Floyd's algorithm is a popular algorithm used to solve this problem. Here are the steps to implement it:

1. Create a 2D array `dist` of size `n x n` to store the shortest distances between all pairs of vertices, where `n` is the number of vertices in the graph.
2. Initialize the array `dist` with the weights of the edges in the graph. If there is no edge between two vertices, the distance between them is considered as infinity.
3. For each vertex `k`, iterate over all pairs of vertices `i` and `j` and update the value of `dist[i][j]` as `min(dist[i][j], dist[i][k] + dist[k][j])`.
4. After iterating over all vertices, the array `dist` will contain the shortest distances between all pairs of vertices in the graph.

### Travelling Sales Person problem

The Travelling Sales Person problem is to find the shortest possible route that visits every city exactly once and returns to the starting city. Dynamic programming is a popular algorithm used to solve this problem. Here are the steps to implement it:

1. Create a 2D array `dp` of size `2^n x n` to store the optimal solutions to subproblems, where `n` is the number of cities in the given graph.
2. Initialize the first row of the array `dp` with the distances between the starting city and all other cities in the graph.
3. For each subproblem `S` of size `k`, where `k` ranges from 2 to `n`, iterate over all possible sets of cities `T` of size `k` that contain the starting city and are a subset of `S`. For each set `T`, calculate the optimal route that visits all cities in `T` exactly once and returns to the starting city. Update the value of `dp[S][i]` as `min(dp[S-T][j] + dist[j][i])`, where `j` is the last city visited before returning to the starting city.
4. After iterating over all subproblems, the optimal route that visits every city exactly once and returns to the starting city can be obtained from the value of `dp[2^n-1][i]`, where `i` is the starting city.

By implementing these two algorithms, we can efficiently solve the All-Pairs Shortest Paths problem and the Travelling Sales Person problem.