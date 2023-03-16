### GraphUtil

GraphUtil is a utility class that provides a set of static methods for working with graphs. These methods can be used to perform common graph operations such as finding the shortest path between two nodes, computing the degree of a node, or finding the connected components of a graph.

Some of the key methods provided by GraphUtil include:

- `shortestPath(Graph graph, Node start, Node end)`: This method computes the shortest path between two nodes in a graph using Dijkstra's algorithm. It returns a list of nodes representing the shortest path from the start node to the end node.

- `degree(Graph graph, Node node)`: This method computes the degree of a node in a graph. The degree of a node is the number of edges connected to it.

- `connectedComponents(Graph graph)`: This method computes the connected components of a graph. A connected component is a subgraph in which any two nodes are connected to each other by a path. This method returns a list of subgraphs representing the connected components of the input graph.

These methods can be useful when developing social-semantic applications that involve working with graphs. For example, the `shortestPath` method can be used to find the shortest path between two users in a social network, while the `connectedComponents` method can be used to identify clusters of users with similar interests or behaviors.