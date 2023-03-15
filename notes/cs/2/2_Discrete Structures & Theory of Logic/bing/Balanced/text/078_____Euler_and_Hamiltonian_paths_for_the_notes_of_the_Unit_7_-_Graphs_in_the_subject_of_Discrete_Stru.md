### Euler and Hamiltonian paths

- An **Euler path** is a path in a graph that passes through every **edge** exactly once  . If it ends at the initial vertex, then it is an **Euler cycle**  .
- A **Hamiltonian path** is a path in a graph that passes through every **vertex** exactly once  . If it ends at the initial vertex, then it is a **Hamiltonian cycle**  .
- Euler paths and cycles can exist in both directed and undirected graphs, but Hamiltonian paths and cycles can only exist in undirected graphs .
- To check if a graph has an Euler path or cycle, we can use the following criteria :
  - A connected graph has an Euler cycle if and only if every vertex has an even degree.
  - A connected graph has an Euler path but not an Euler cycle if and only if it has exactly two vertices of odd degree.
- To check if a graph has a Hamiltonian path or cycle, there is no simple necessary and sufficient criteria, but we can use some sufficient conditions :
  - A graph has a Hamiltonian cycle if it is a complete graph, i.e., every pair of vertices is connected by an edge.
  - A graph has a Hamiltonian cycle if it is a cycle graph, i.e., a graph with n vertices and n edges forming a single cycle.
  - A graph has a Hamiltonian path if it is a path graph, i.e., a graph with n vertices and n-1 edges forming a single path.
- Euler and Hamiltonian paths and cycles have applications in various fields, such as network routing, DNA sequencing, traveling salesman problem, etc  .