### Euler and Hamiltonian paths

- An **Euler path** is a path in a graph that passes through every **edge** exactly once  . If it ends at the initial vertex, then it is an **Euler cycle**  .
- A **Hamiltonian path** is a path in a graph that passes through every **vertex** exactly once  . If it ends at the initial vertex, then it is a **Hamiltonian cycle**  .
- Euler paths and cycles can exist in both directed and undirected graphs, but Hamiltonian paths and cycles can only exist in undirected graphs .
- To check if a graph has an Euler path or cycle, we can use the following criteria :
  - A graph has an Euler cycle if and only if it is connected and every vertex has an even degree.
  - A graph has an Euler path if and only if it is connected and has exactly two vertices with odd degree.
- To check if a graph has a Hamiltonian path or cycle, there is no simple necessary and sufficient criteria, but there are some sufficient conditions that can be used as heuristics :
  - A graph has a Hamiltonian cycle if and only if it is a complete graph, i.e., every pair of vertices is connected by an edge.
  - A graph has a Hamiltonian cycle if it is connected and the sum of the degrees of any two non-adjacent vertices is at least the number of vertices in the graph. This is known as the Ore's theorem.
  - A graph has a Hamiltonian path if it is connected and the sum of the degrees of any two non-adjacent vertices is at least the number of vertices minus one in the graph. This is known as the Dirac's theorem.

Here are some examples of graphs with Euler and Hamiltonian paths and cycles:

![Euler and Hamiltonian paths and cycles](https://i.imgur.com/0f0yY8h.png)

- Graph A has an Euler cycle (a-b-c-d-e-f-a) and a Hamiltonian cycle (a-b-c-e-f-d-a).
- Graph B has an Euler path (a-b-c-d-e-f) but no Hamiltonian path or cycle.
- Graph C has a Hamiltonian path (a-b-c-d-e-f) but no Euler path or cycle.
- Graph D has neither an Euler path or cycle nor a Hamiltonian path or cycle.