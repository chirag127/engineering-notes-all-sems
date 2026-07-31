# Unit 7 - Graphs in the subject of Discrete Structures & Theory of Logic

### Euler and Hamiltonian paths

- An **Euler path** is a path in a graph that visits every edge exactly once.
- An **Euler circuit** is an Euler path that starts and ends at the same vertex.
- A graph has an Euler circuit if and only if it is connected and every vertex has an even degree.
- A graph has an Euler path if and only if it is connected and has exactly two vertices of odd degree.
- A **Hamiltonian path** is a path in a graph that visits every vertex exactly once.
- A **Hamiltonian circuit** is a Hamiltonian path that starts and ends at the same vertex.
- The problem of determining whether a graph has a Hamiltonian circuit is NP-complete, meaning that it is unlikely that there is an efficient algorithm to solve it.
- There are several necessary conditions for a graph to have a Hamiltonian circuit, but no sufficient conditions are known.
- Some common necessary conditions include the degree of each vertex being at least half the number of vertices in the graph, and the graph being connected.
- There are several algorithms to find Euler and Hamiltonian paths and circuits, including Fleury's algorithm and the backtracking algorithm.