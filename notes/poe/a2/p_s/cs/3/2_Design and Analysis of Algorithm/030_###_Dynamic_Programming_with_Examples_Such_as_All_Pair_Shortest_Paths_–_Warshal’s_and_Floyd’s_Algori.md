 Here is the content in markdown format:

### Dynamic Programming with Examples Such as All Pair Shortest Paths – Warshal’s and Floyd’s Algorithms

Dynamic programming is a technique for solving complex problems by breaking them down into smaller subproblems. It solves each subproblem only once, and then saves its answer in a table. Each answer that is saved can be used to solve larger subproblems.

Two famous algorithms for finding shortest paths between all pairs of vertices in a graph are:

- Warshall's algorithm: Runs in O(V^3) time where V is the number of vertices. It uses dynamic programming to fill out a distance matrix.
- Floyd's algorithm: Also runs in O(V^3) time. It iteratively updates a distance matrix by considering all possible intermediate vertices in shortest paths.

**Warshall's algorithm:**

1. Input: Adjacency matrix A of the graph
2. Create a distance matrix D where Dijk = Aij for all i, j, k
3. For k = 1 to n:
    - For i = 1 to n:
        - For j = 1 to n:
            - Dij = min(Dij, Dik + Dkj)
4. Output: Matrix D contains shortest distances between all pairs of vertices

**Floyd's algorithm:**

1. Input: Adjacency matrix A of the graph
2. Create a distance matrix D where Dij = Aij for all i ≠ j
3. For k = 1 to n:
    - For i = 1 to n:
        - For j = 1 to n:
            - Dij = min(Dij, Dik + Dkj)
4. Output: Matrix D contains shortest distances between all pairs of vertices

[Detailed explanations, examples and ascii diagrams can be added here]

Advantages:

- Both algorithms have a running time of O(V^3) which is efficient for sparse graphs
- They can detect negative weight cycles

Disadvantages:

- The running time is high for dense graphs due to the cubic complexity
- They may not be suitable for large graphs due to the high space complexity of O(V^2)

Applications:

- Finding shortest paths between all pairs of vertices in a graph
- Detecting negative weight cycles in a graph