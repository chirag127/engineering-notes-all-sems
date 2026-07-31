### Unit 7 - Graphs in Discrete Structures & Theory of Logic
#### Bipartite Graphs

- A bipartite graph is a type of graph where the vertex set can be divided into two disjoint sets such that every edge connects a vertex in one set to a vertex in the other set.
- In other words, there are no edges between vertices within the same set.
- A bipartite graph can also be called a bigraph or a bicolored graph.
- A simple example of a bipartite graph is a graph with two sets of vertices, where one set represents men and the other set represents women, and the edges represent romantic relationships between a man and a woman.
- A complete bipartite graph is a bipartite graph where every vertex in one set is connected to every vertex in the other set.
- The notation for a complete bipartite graph is K<sub>m,n</sub>, where m and n are the number of vertices in the two sets.
- A bipartite graph can be used to model many real-world situations, such as relationships between different sets of entities, or the flow of resources between different nodes in a network.
- A graph is bipartite if and only if it does not contain an odd cycle.
- An algorithm to determine if a graph is bipartite is to perform a depth-first search or a breadth-first search and check if the graph can be colored with two colors such that no two adjacent vertices have the same color.
- Bipartite graphs have many applications in computer science, including matching algorithms, network flow algorithms, and scheduling algorithms.