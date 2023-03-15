## Unit 7 - Graphs

A graph is a collection of vertices (also called nodes) and edges (also called arcs) that connect them. Graphs can be used to model many real-world phenomena, such as networks, maps, social media, games, etc.

Some basic concepts and terminology related to graphs are:

- A vertex is an entity that has a name or an identifier. Vertices can represent objects, people, places, etc.
- An edge is a connection or a relation between two vertices. Edges can have a direction, a weight, or a label. Edges can represent links, paths, distances, costs, etc.
- A directed graph (or digraph) is a graph where all edges have a direction, indicating the source and the destination of the edge. A directed edge is denoted by an arrow, such as u -> v.
- An undirected graph is a graph where all edges are bidirectional, meaning that they can be traversed in either direction. An undirected edge is denoted by a line, such as u - v.
- A weighted graph is a graph where all edges have a numerical value associated with them, called the weight. The weight can represent the length, cost, capacity, etc. of the edge. A weighted edge is denoted by a line with a number, such as u - 5 - v.
- A labeled graph is a graph where all edges have a name or a symbol associated with them, called the label. The label can represent the type, name, or category of the edge. A labeled edge is denoted by a line with a letter, such as u - a - v.
- A simple graph is a graph that has no loops or multiple edges. A loop is an edge that connects a vertex to itself, such as u -> u. A multiple edge is an edge that connects the same pair of vertices more than once, such as u - v and u - v.
- A multigraph is a graph that may have loops or multiple edges. A multigraph can be directed, undirected, weighted, or labeled.
- A subgraph is a graph that is a part of another graph. A subgraph contains some of the vertices and edges of the original graph, but not necessarily all of them. A subgraph is denoted by G' = (V', E'), where V' is a subset of V and E' is a subset of E.
- A path is a sequence of edges that connects a sequence of vertices. A path can be directed or undirected, depending on the type of the graph. A path is denoted by a list of vertices, such as u, v, w, x.
- A cycle is a path that starts and ends at the same vertex. A cycle can be directed or undirected, depending on the type of the graph. A cycle is denoted by a list of vertices, such as u, v, w, u.
- A connected graph is a graph where there is a path between any pair of vertices. A connected graph has no isolated vertices, which are vertices that have no edges incident to them.
- A disconnected graph is a graph that is not connected. A disconnected graph has at least one isolated vertex, or two or more components, which are subgraphs that are connected within themselves but not with each other.
- A tree is a connected graph that has no cycles. A tree has exactly one path between any pair of vertices. A tree has n - 1 edges, where n is the number of vertices.
- A forest is a graph that has no cycles. A forest may have one or more components, each of which is a tree.
- A bipartite graph is a graph where the vertices can be divided into two disjoint sets, such that no edge connects two vertices from the same set. A bipartite graph can be colored with two colors, such that no two adjacent vertices have the same color.
- A complete graph is a graph where there is an edge between every pair of vertices. A complete graph has n(n - 1) / 2 edges, where n is the number of vertices. A complete graph is denoted by K_n, where n is the number of vertices.