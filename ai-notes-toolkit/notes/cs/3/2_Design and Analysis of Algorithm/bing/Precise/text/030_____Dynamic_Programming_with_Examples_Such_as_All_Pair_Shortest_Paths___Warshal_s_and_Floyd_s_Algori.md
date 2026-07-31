### Dynamic Programming with Examples Such as All Pair Shortest Paths – Warshal’s and Floyd’s Algorithms

Dynamic programming is a method for solving complex problems by breaking them down into smaller subproblems. It is applicable to problems that exhibit the properties of overlapping subproblems and optimal substructure. When a problem can be solved by combining optimal solutions to non-overlapping subproblems, the strategy is called "divide and conquer" instead. Dynamic programming is used when the subproblems are not independent, such as in the shortest path problem.

#### Warshal’s Algorithm

Warshal’s algorithm, also known as the Floyd–Warshall algorithm, is an algorithm for finding the shortest paths between all pairs of vertices in a weighted graph. It works by iteratively improving an estimate on the shortest path between two vertices until the estimate is optimal.

The algorithm can be described as follows:

1. Initialize the distance matrix with the weights of the edges in the graph.
2. For each vertex k, update the distance matrix by considering all pairs of vertices i and j, and checking if the path from i to j through k is shorter than the current shortest path from i to j. If it is, update the distance matrix with the new shortest path.
3. Repeat step 2 for all vertices in the graph.

#### Floyd’s Algorithm

Floyd’s algorithm is similar to Warshal’s algorithm, but it uses a different approach to updating the distance matrix. Instead of considering all pairs of vertices, it considers all pairs of edges. The algorithm can be described as follows:

1. Initialize the distance matrix with the weights of the edges in the graph.
2. For each edge (i, j) with weight w, update the distance matrix by considering all pairs of vertices k and l, and checking if the path from k to l through i and j is shorter than the current shortest path from k to l. If it is, update the distance matrix with the new shortest path.
3. Repeat step 2 for all edges in the graph.

Both Warshal’s and Floyd’s algorithms have a time complexity of O(n^3), where n is the number of vertices in the graph. They are commonly used to solve the all-pairs shortest paths problem in dense graphs, where the number of edges is close to the maximum possible number of edges.