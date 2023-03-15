## Unit 7 - Graphs

A graph is a collection of vertices (or nodes) and edges (or links) that connect some pairs of vertices. Graphs are used to model various types of networks, such as social networks, communication networks, transportation networks, etc.

Some basic concepts and terminology related to graphs are:

- A vertex is an entity that can have a name, a value, or some other attributes. Vertices are also called nodes or points.
- An edge is a connection between two vertices. Edges are also called links or lines.
- A path is a sequence of edges that connects two vertices. A path can be simple (no repeated vertices) or non-simple (some vertices are repeated).
- A cycle is a path that starts and ends at the same vertex. A cycle can be simple (no repeated edges) or non-simple (some edges are repeated).
- A graph is connected if there is a path between any two vertices. A graph is disconnected if there are some pairs of vertices that have no path between them.
- A subgraph is a graph that consists of some vertices and edges of another graph. A subgraph can be proper (not equal to the original graph) or improper (equal to the original graph).
- A graph is complete if there is an edge between every pair of vertices. A complete graph with n vertices has n(n-1)/2 edges.
- A graph is bipartite if its vertices can be divided into two sets such that there is no edge between vertices in the same set. A bipartite graph can be complete if there is an edge between every pair of vertices in different sets.
- A graph is weighted if each edge has a numerical value associated with it. The value of an edge is also called its weight or cost.
- A graph is directed if each edge has a direction, indicating the source and the destination of the edge. A directed edge is also called an arc or an arrow.
- A graph is undirected if each edge has no direction, meaning that it can be traversed in either direction. An undirected edge is also called a line or a link.
- A graph is simple if it has no loops (edges that connect a vertex to itself) and no multiple edges (more than one edge between the same pair of vertices).
- A graph is multigraph if it has loops or multiple edges.
- A graph is mixed if it has both directed and undirected edges.
- A graph is planar if it can be drawn on a plane without any edges crossing each other. A graph is non-planar if it cannot be drawn on a plane without any edges crossing each other.
- A graph is regular if every vertex has the same degree. The degree of a vertex is the number of edges incident to it. The degree of a vertex in a directed graph is the sum of its in-degree (the number of edges coming into it) and its out-degree (the number of edges going out of it).
- A graph is Eulerian if it has a cycle that contains every edge exactly once. A graph is Hamiltonian if it has a cycle that contains every vertex exactly once.
- A graph is a tree if it is connected and has no cycles. A tree is a special type of graph that has a hierarchical structure. A tree has a root (a vertex with no incoming edges), leaves (vertices with no outgoing edges), and internal nodes (vertices with both incoming and outgoing edges).
- A graph is a forest if it is a collection of trees. A forest is a special type of graph that has no cycles. A forest can be disconnected or connected. A connected forest is also called a spanning tree.