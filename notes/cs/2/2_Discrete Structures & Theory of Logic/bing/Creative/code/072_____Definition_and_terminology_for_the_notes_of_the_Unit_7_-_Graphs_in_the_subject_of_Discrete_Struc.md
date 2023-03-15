Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of definition and terminology for the notes of the unit 7 - graphs in the subject of discrete structures and theory of logic.

```markdown
### Definition and terminology for the notes of the Unit 7 - Graphs in the subject of Discrete Structures & Theory of Logic

- A **graph** is a mathematical structure that consists of a set of **vertices** (also called **nodes**) and a set of **edges** (also called **arcs**) that connect pairs of vertices.
- A graph can be represented by a diagram, where vertices are drawn as points or circles, and edges are drawn as lines or curves connecting the vertices.
- A graph can also be represented by an **adjacency matrix**, where each row and column corresponds to a vertex, and the entry at row i and column j is 1 if there is an edge between vertex i and vertex j, and 0 otherwise.
- A graph can also be represented by an **adjacency list**, where each vertex is associated with a list of its **neighbors**, i.e., the vertices that are adjacent to it by an edge.
- A graph is **simple** if it has no **loops** (edges that connect a vertex to itself) and no **multiple edges** (more than one edge between the same pair of vertices).
- A graph is **directed** if each edge has a direction, i.e., it goes from one vertex to another. A directed edge is also called an **arc**. A directed graph is also called a **digraph**.
- A graph is **undirected** if each edge has no direction, i.e., it connects two vertices without any order. An undirected edge is also called a **line**. An undirected graph is also called a **simple graph**.
- A graph is **weighted** if each edge has a numerical value associated with it, called the **weight** of the edge. A weighted graph can be used to model situations where the cost, distance, or time of traversing an edge varies.
- A graph is **complete** if there is an edge between every pair of vertices. A complete graph with n vertices has n(n-1)/2 edges if it is undirected, and n(n-1) edges if it is directed.
- A graph is **bipartite** if its vertices can be divided into two disjoint sets, called **partitions**, such that every edge connects a vertex from one partition to a vertex from another partition. A bipartite graph can be colored with two colors, such that no two adjacent vertices have the same color.
- A graph is **connected** if there is a path between any two vertices, i.e., a sequence of edges that joins them. A graph is **disconnected** if it is not connected.
- A graph is **strongly connected** if it is directed and there is a path from any vertex to any other vertex, following the direction of the edges. A graph is **weakly connected** if it is directed and it becomes connected when the direction of the edges is ignored.
- A **subgraph** of a graph is a graph that consists of a subset of the vertices and a subset of the edges of the original graph, such that each edge in the subgraph connects two vertices in the subgraph.
- A **spanning subgraph** of a graph is a subgraph that contains all the vertices of the original graph.
- A **spanning tree** of a graph is a spanning subgraph that is a tree, i.e., a connected graph with no cycles (closed paths).
- A **cycle** in a graph is a path that starts and ends at the same vertex, and has no repeated vertices or edges (except the first and last vertex).
- A **Hamiltonian cycle** in a graph is a cycle that visits every vertex exactly once (except the first and last vertex, which are the same).
- A **Eulerian cycle** in a graph is a cycle that visits every edge exactly once.
- A **degree** of a vertex in a graph is the number of edges that are incident to it, i.e., that connect it to other vertices. In a directed graph, the degree of a vertex can be divided into **in-degree**, the number of edges that enter the vertex, and **out-degree**, the number of edges that leave the vertex.
- A **walk** in a graph is a sequence of vertices and edges that starts and ends at a vertex, and such that each edge connects two consecutive vertices in the sequence. A walk can repeat vertices and edges.
- A **trail** in a graph is a