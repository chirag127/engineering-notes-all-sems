### Graph Implementation, BFS, DFS, Minimum cost spanning tree, shortest path algorithm

A graph is a data structure that consists of a set of vertices (or nodes) and a set of edges that connect pairs of vertices. Graphs can be used to represent many real-world problems, such as transportation networks, social networks, and computer networks.

#### Graph Implementation
There are two common ways to implement a graph: adjacency matrix and adjacency list.

- **Adjacency Matrix:** An adjacency matrix is a two-dimensional array where the element at row i and column j represents the edge between vertex i and vertex j. If the graph is weighted, the element at row i and column j represents the weight of the edge between vertex i and vertex j. If the graph is unweighted, the element at row i and column j is 1 if there is an edge between vertex i and vertex j, and 0 otherwise.

- **Adjacency List:** An adjacency list is an array of linked lists. The linked list at index i represents the edges connected to vertex i. Each element in the linked list represents an edge and contains the vertex at the other end of the edge and the weight of the edge (if the graph is weighted).

#### Breadth-First Search (BFS)
Breadth-First Search (BFS) is an algorithm for traversing or searching a graph. It starts at a source vertex and explores all the vertices at the current depth level before moving on to the vertices at the next depth level.

The algorithm uses a queue to keep track of the vertices to be visited. It first enqueues the source vertex, then dequeues a vertex, visits it, and enqueues all its unvisited neighbors. The process is repeated until the queue is empty.

#### Depth-First Search (DFS)
Depth-First Search (DFS) is an algorithm for traversing or searching a graph. It starts at a source vertex and explores as far as possible along each branch before backtracking.

The algorithm uses a stack to keep track of the vertices to be visited. It first pushes the source vertex onto the stack, then pops a vertex, visits it, and pushes all its unvisited neighbors onto the stack. The process is repeated until the stack is empty.

#### Minimum Cost Spanning Tree
A Minimum Cost Spanning Tree (MCST) of a graph is a spanning tree of the graph that has the minimum possible total edge weight. There are two common algorithms for finding the MCST of a graph: Kruskal's algorithm and Prim's algorithm.

- **Kruskal's Algorithm:** Kruskal's algorithm starts with an empty set of edges and adds edges to the set in increasing order of their weight, as long as the edge does not create a cycle. The algorithm terminates when the set of edges forms a spanning tree.

- **Prim's Algorithm:** Prim's algorithm starts with an arbitrary vertex and grows the tree one vertex at a time by adding the edge with the minimum weight that connects a vertex in the tree to a vertex not in the tree. The algorithm terminates when all the vertices are in the tree.

#### Shortest Path Algorithm
The shortest path algorithm is used to find the shortest path between two vertices in a graph. There are several algorithms for finding the shortest path, including Dijkstra's algorithm and Bellman-Ford algorithm.

- **Dijkstra's Algorithm:** Dijkstra's algorithm is used to find the shortest path between a source vertex and all other vertices in a graph with non-negative edge weights. The algorithm maintains a set of vertices for which the shortest path from the source has been found, and repeatedly selects the vertex with the minimum distance from the source that is not in the set, and updates the distances of its neighbors.

- **Bellman-Ford Algorithm:** The Bellman-Ford algorithm is used to find the shortest path between a source vertex and all other vertices in a graph with possibly negative edge weights. The algorithm repeatedly relaxes the edges, updating the distance of each vertex to the source if a shorter path is found. The algorithm terminates after |V|-1 iterations, where |V| is the number of vertices in the graph.
