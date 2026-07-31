## Unit 7 - Graphs

A graph is a collection of vertices (also called nodes) and edges (also called arcs) that connect them. Graphs can be used to model many real-world phenomena, such as networks, maps, games, social media, etc.

Some basic concepts and terminology related to graphs are:

- A vertex is an element of a graph that represents an entity, such as a person, a city, a computer, etc.
- An edge is an element of a graph that represents a connection or a relation between two vertices, such as a friendship, a road, a link, etc.
- A path is a sequence of edges that connects two vertices in a graph. A path can be simple (no repeated vertices) or non-simple (some vertices are repeated).
- A cycle is a path that starts and ends at the same vertex. A cycle can be simple (no repeated edges) or non-simple (some edges are repeated).
- A graph is connected if there is a path between any two vertices in the graph. A graph is disconnected if there are some vertices that cannot be reached from other vertices.
- A subgraph is a graph that consists of some vertices and edges of another graph. A subgraph is induced if it contains all the edges between its vertices that are present in the original graph.
- A graph is complete if there is an edge between every pair of vertices in the graph. A complete graph with n vertices has n(n-1)/2 edges.
- A graph is bipartite if its vertices can be divided into two disjoint sets such that there is no edge between any two vertices in the same set. A bipartite graph can be represented by a bipartition, which is a pair of sets that contains all the vertices of the graph.
- A graph is weighted if each edge has a numerical value associated with it, called the weight of the edge. The weight can represent the cost, distance, time, etc. of the connection between the vertices.
- A graph is directed if each edge has a direction, indicating the source and the destination of the connection. A directed edge is also called an arc. A directed graph is also called a digraph.
- A graph is undirected if each edge has no direction, indicating a bidirectional or symmetric connection between the vertices. An undirected edge is also called a line. An undirected graph is also called a simple graph.

Some examples of graphs are:

- A social network graph, where the vertices are people and the edges are friendships, follows, likes, etc.
- A road map graph, where the vertices are cities and the edges are roads, highways, bridges, etc.
- A web graph, where the vertices are web pages and the edges are hyperlinks, references, citations, etc.
- A game tree graph, where the vertices are game states and the edges are moves, actions, transitions, etc.