
## Unit 4 - Graphs

- Graphs are collections of objects called **vertices** or **nodes**, connected by lines called **edges**.
- Graphs are used to represent relationships between objects, such as the connections between cities on a map.
- **Adjacency Matrices** are 2-dimensional arrays that represent a graph. The rows and columns of the matrix represent the vertices of the graph, and the entries in the matrix indicate the presence or absence of an edge between the vertices.
- **Adjacency Lists** are linked lists that represent a graph. Each vertex in the graph is represented by a linked list, with each element in the list representing a destination vertex.
- **Graph Traversal** algorithms are used to traverse a graph and visit every vertex in the graph.
    - **Depth First Search** is an algorithm that visits each vertex in the graph by recursively visiting each adjacent vertex until it reaches the end of the graph.
    - **Breadth First Search** is an algorithm that visits each vertex in the graph by visiting each adjacent vertex in a level-by-level manner.
- **Connected Component** is a set of connected vertices in a graph.
- **Spanning Trees** are subgraphs of a graph that connect all the vertices in the graph.
- **Minimum Cost Spanning Trees** are spanning trees that have the minimum cost possible.
    - **Prim's Algorithm** is an algorithm that finds a minimum cost spanning tree by adding the cheapest edge to the tree at each step.
    - **Kruskal's Algorithm** is an algorithm that finds a minimum cost spanning tree by adding the least expensive edge to the tree at each step.
- **Transitive Closure** is a matrix that shows the reachability of each vertex in a graph.
- **Shortest Path Algorithm** is an algorithm that finds the shortest path between two vertices in a graph.
    - **Warshall's Algorithm** is an algorithm that finds the transitive closure of a graph.
    - **Dijkstra's Algorithm** is an algorithm that finds the shortest path between two vertices in a graph.