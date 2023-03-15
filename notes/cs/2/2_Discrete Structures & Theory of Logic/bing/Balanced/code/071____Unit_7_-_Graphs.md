## Unit 7 - Graphs

A graph is a collection of vertices (also called nodes) and edges (also called arcs) that connect them. Graphs can be used to model many real-world phenomena, such as networks, maps, games, social media, etc.

Some basic concepts and terminology related to graphs are:

- A vertex is an element of a graph that represents an entity, such as a person, a city, a computer, etc.
- An edge is a connection between two vertices that represents a relationship, such as a friendship, a road, a link, etc.
- A path is a sequence of edges that connects two vertices in a graph. A path can be simple (no repeated vertices) or non-simple (some vertices are repeated).
- A cycle is a path that starts and ends at the same vertex. A cycle can be simple (no repeated vertices except the first and last one) or non-simple (some vertices are repeated more than once).
- A graph is connected if there is a path between any two vertices in the graph. A graph is disconnected if there are some pairs of vertices that have no path between them.
- A subgraph is a graph that consists of some vertices and edges of another graph. A subgraph is induced if it contains all the edges between the vertices in the subgraph.
- A graph is complete if there is an edge between every pair of vertices in the graph. A complete graph with n vertices has n(n-1)/2 edges.
- A graph is bipartite if its vertices can be divided into two sets, such that there is no edge between two vertices in the same set. A bipartite graph can be represented by a bipartition, which is a pair of sets that contains all the vertices of the graph.
- A graph is weighted if each edge has a numerical value associated with it, which can represent the cost, distance, capacity, etc. of the connection. A graph is unweighted if all the edges have the same value (usually 1).
- A graph is directed if each edge has an orientation, which indicates the direction of the connection. A directed edge is also called an arc. A graph is undirected if the edges have no orientation, and can be traversed in either direction.
- A graph is simple if it has no loops (edges that connect a vertex to itself) and no multiple edges (more than one edge between the same pair of vertices). A graph is multigraph if it can have loops and multiple edges.
- A graph is planar if it can be drawn on a plane without any edges crossing each other. A graph is non-planar if it cannot be drawn on a plane without edge crossings.
- A graph is regular if every vertex has the same degree, which is the number of edges incident to the vertex. A graph is k-regular if every vertex has degree k.
- A graph is Eulerian if it has a cycle that contains every edge exactly once. A graph is Hamiltonian if it has a cycle that contains every vertex exactly once.
- A graph is a tree if it is connected and has no cycles. A tree is a special type of graph that has many applications in computer science, such as data structures, algorithms, etc.
- A graph is a forest if it is a collection of trees. A forest is also a special type of graph that can be used to model hierarchical structures, such as family trees, organizational charts, etc.