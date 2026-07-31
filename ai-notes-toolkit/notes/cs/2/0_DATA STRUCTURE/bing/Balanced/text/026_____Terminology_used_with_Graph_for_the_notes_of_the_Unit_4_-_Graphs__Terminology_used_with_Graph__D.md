### Terminology used with Graph

- A **graph** is a collection of **vertices** (also called nodes or points) and **edges** (also called arcs or lines) that connect the vertices.
- A graph can be **directed** or **undirected**. A directed graph has edges that are associated with a direction, meaning that they can only be traversed in one way. An undirected graph has edges that are bidirectional, meaning that they can be traversed in both ways.
- A graph can be **weighted** or **unweighted**. A weighted graph has edges that are assigned a numerical value, called the **weight** or **cost**, that represents some attribute of the edge, such as distance, time, or capacity. An unweighted graph has edges that are not assigned any weight.
- A graph can be **simple** or **non-simple**. A simple graph has no **loops** (edges that connect a vertex to itself) and no **multiple edges** (more than one edge between the same pair of vertices). A non-simple graph may have loops and/or multiple edges.
- A graph can be **cyclic** or **acyclic**. A cyclic graph has at least one **cycle** (a path that starts and ends at the same vertex and has no repeated vertices or edges). An acyclic graph has no cycles.
- A graph can be **connected** or **disconnected**. A connected graph has a **path** (a sequence of vertices and edges) between any pair of vertices. A disconnected graph has at least one pair of vertices that are not connected by a path.
- A **subgraph** of a graph is a graph that consists of a subset of the vertices and edges of the original graph. A subgraph is said to be **induced** if it contains all the edges between the vertices in the subset.
- A **degree** of a vertex in a graph is the number of edges incident to that vertex. In a directed graph, the degree can be divided into **in-degree** (the number of edges entering the vertex) and **out-degree** (the number of edges leaving the vertex).
- A **walk** in a graph is a sequence of vertices and edges that starts and ends at any vertex and allows repeated vertices and edges. A walk is said to be **closed** if it starts and ends at the same vertex.
- A **trail** in a graph is a walk that does not repeat any edge. A trail is said to be **Eulerian** if it contains every edge of the graph exactly once.
- A **path** in a graph is a walk that does not repeat any vertex. A path is said to be **Hamiltonian** if it contains every vertex of the graph exactly once.
- A **circuit** in a graph is a closed trail. A circuit is said to be **Eulerian** if it is also Eulerian as a trail.
- A **cycle** in a graph is a closed path. A cycle is said to be **Hamiltonian** if it is also Hamiltonian as a path.
- A **tree** is a connected acyclic graph. A tree is said to be **rooted** if one of its vertices is designated as the **root** and every edge is directed away from the root.
- A **forest** is a graph that consists of one or more trees. A forest is said to be **rooted** if each of its trees is rooted.
- A **spanning tree** of a graph is a subgraph that is a tree and contains all the vertices of the original graph. A graph may have more than one spanning tree.
- A **minimum spanning tree** of a weighted graph is a spanning tree that has the minimum possible sum of edge weights among all the spanning trees of the graph. A weighted graph may have more than one minimum spanning tree.