### Dynamic Programming with Examples Such as All Pair Shortest Paths – Warshal’s and Floyd’s Algorithms

Dynamic programming is a method for solving complex problems by breaking them down into smaller subproblems. It is applicable to problems that exhibit the properties of overlapping subproblems and optimal substructure. When a problem can be solved by combining optimal solutions to non-overlapping subproblems, the strategy is called "divide and conquer" instead. Dynamic programming is used when the subproblems are not independent, such as in the shortest path problem.

#### Warshal’s Algorithm

Warshal’s algorithm, also known as the Floyd–Warshall algorithm, is an algorithm for finding shortest paths in a weighted graph with positive or negative edge weights (but with no negative cycles). A single execution of the algorithm will find the lengths (summed weights) of the shortest paths between all pairs of vertices.

The algorithm works by iteratively improving an estimate on the shortest path between two vertices, until the estimate is optimal. The algorithm maintains a matrix D, where D[i][j] is an estimate of the shortest path between vertices i and j. Initially, D[i][j] is set to the weight of the edge between i and j, or infinity if there is no such edge. Then, for each vertex k, the algorithm updates the matrix D by considering all pairs of vertices i and j, and checking if the path from i to j through k is shorter than the current estimate of the shortest path from i to j. If it is, the estimate is updated.

#### Floyd’s Algorithm

Floyd’s algorithm is similar to Warshal’s algorithm, but it also keeps track of the actual path between vertices, not just the length of the shortest path. The algorithm maintains a matrix P, where P[i][j] is the last vertex on the shortest path from i to j. Initially, P[i][j] is set to i if there is an edge from i to j, or to a special value indicating that there is no path from i to j. Then, for each vertex k, the algorithm updates the matrix P by considering all pairs of vertices i and j, and checking if the path from i to j through k is shorter than the current estimate of the shortest path from i to j. If it is, the estimate is updated and P[i][j] is set to P[k][j].

#### Example

Consider the following weighted graph:

```
   A
  / \
 2   3
/     \
B--1--C
```

The initial matrices D and P for Warshal’s and Floyd’s algorithms, respectively, are:

```
D = [[0, 2, 3],
     [2, 0, 1],
     [3, 1, 0]]

P = [[None, A, A],
     [B, None, B],
     [C, C, None]]
```

After the first iteration, with k = A, the matrices are updated to:

```
D = [[0, 2, 3],
     [2, 0, 1],
     [3, 1, 0]]

P = [[None, A, A],
     [B, None, B],
     [C, C, None]]
```

After the second iteration, with k = B, the matrices are updated to:

```
D = [[0, 2, 3],
     [2, 0, 1],
     [3, 1, 0]]

P = [[None, A, A],
     [B, None, B],
     [C, C, None]]
```

After the third and final iteration, with k = C, the matrices are updated to:

```
D = [[0, 2, 3],
     [2, 0, 1],
     [3, 1, 0]]

P = [[None, A, A],
     [B, None, B],
     [C, C, None]]
```

The final matrix D gives the shortest distances between all pairs of vertices, and the matrix P can be used to reconstruct the actual paths.

#### Resource Allocation Problem

The resource allocation problem is a problem of assigning a set of resources to a set of tasks in such a way that the total cost of the assignment is minimized. This problem can be solved using dynamic programming by defining a subproblem as the minimum cost of assigning the first i resources to the first j tasks. The solution to the original problem is then the solution to the subproblem with i = the number of resources and j = the number of tasks.

#### Backtracking

Backtracking is a general algorithm for finding all (or some) solutions to a problem that incrementally builds candidates to the solutions