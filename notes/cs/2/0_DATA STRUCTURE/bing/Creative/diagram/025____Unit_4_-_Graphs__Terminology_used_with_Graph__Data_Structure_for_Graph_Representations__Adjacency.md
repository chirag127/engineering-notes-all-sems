## Unit 4 - Graphs

A graph is a data structure that consists of a set of vertices (or nodes) and a set of edges that connect pairs of vertices. A graph can be used to model many types of problems, such as networks, maps, games, social networks, etc.

### Terminology used with Graph

Some common terms used with graphs are:

- **Directed graph**: A graph where the edges have a direction, indicating the source and the destination of the edge. For example, a graph that represents a road network with one-way streets can be modeled as a directed graph.
- **Undirected graph**: A graph where the edges do not have a direction, indicating that the edge can be traversed in either direction. For example, a graph that represents a road network with two-way streets can be modeled as an undirected graph.
- **Weighted graph**: A graph where the edges have a weight, indicating the cost or distance of the edge. For example, a graph that represents a road network with different lengths or tolls can be modeled as a weighted graph.
- **Unweighted graph**: A graph where the edges do not have a weight, indicating that the cost or distance of the edge is the same or irrelevant. For example, a graph that represents a social network with friends can be modeled as an unweighted graph.
- **Path**: A sequence of vertices and edges that connects two vertices in a graph. For example, a path from A to D in a graph can be A-B-C-D or A-E-D, depending on the edges available.
- **Cycle**: A path that starts and ends at the same vertex. For example, a cycle in a graph can be A-B-C-D-A or A-E-F-A, depending on the edges available.
- **Simple path**: A path that does not contain any repeated vertices. For example, a simple path from A to D in a graph can be A-B-C-D, but not A-B-C-A-D.
- **Simple cycle**: A cycle that does not contain any repeated vertices, except for the starting and ending vertex. For example, a simple cycle in a graph can be A-B-C-D-A, but not A-B-C-A-D-A.
- **Degree**: The number of edges incident to a vertex in a graph. For example, the degree of vertex A in a graph can be 2, 3, or 4, depending on the edges connected to A.
- **In-degree**: The number of edges directed to a vertex in a directed graph. For example, the in-degree of vertex A in a directed graph can be 1, 2, or 3, depending on the edges pointing to A.
- **Out-degree**: The number of edges directed from a vertex in a directed graph. For example, the out-degree of vertex A in a directed graph can be 1, 2, or 3, depending on the edges pointing from A.
- **Adjacent**: Two vertices are adjacent if there is an edge between them in a graph. For example, vertex A and B are adjacent in a graph if there is an edge A-B or B-A, depending on the direction of the edge.
- **Connected**: Two vertices are connected if there is a path between them in a graph. For example, vertex A and D are connected in a graph if there is a path A-B-C-D or A-E-D, depending on the edges available.
- **Disconnected**: Two vertices are disconnected if there is no path between them in a graph. For example, vertex A and G are disconnected in a graph if there is no path from A to G, regardless of the edges available.
- **Connected component**: A subgraph of a graph where every pair of vertices is connected. For example, a graph can have one, two, or more connected components, depending on the edges available.
- **Spanning tree**: A subgraph of a graph that is a tree (a connected graph with no cycles) and contains all the vertices of the graph. For example, a graph can have one, two, or more spanning trees, depending on the edges available.
- **Minimum cost spanning tree**: A spanning tree of a weighted graph that has the minimum total weight of all the spanning trees of the graph. For example, a graph can have one, two, or more minimum cost spanning trees, depending on the weights of the edges.

### Data Structure for Graph Representations

There are different ways to represent a graph in a computer program, such as:

- **Adjacency matrix**: A two-dimensional array of size V x V, where V is the number of vertices in the graph, and the element at row i and column j indicates the presence or absence of an edge between vertex i and vertex