Hello, I am Sydney, your AI assistant. I can help you with your topic. Here are some notes on Euler and Hamiltonian paths for the unit 7 - Graphs in the subject of Discrete Structures & Theory of Logic.

### Euler and Hamiltonian paths

- A **path** in a graph is a sequence of vertices connected by edges. A path is **simple** if it does not repeat any vertices or edges. A path is **closed** if it starts and ends at the same vertex.
- An **Euler path** is a path that passes through every **edge** exactly once. If it ends at the initial vertex then it is an **Euler cycle**. An Euler path can exist both in a directed and undirected graph  .
- A **Hamiltonian path** is a path that passes through every **vertex** exactly once (NOT every edge). If it ends at the initial vertex then it is a **Hamiltonian cycle**. A Hamiltonian path can exist both in a directed and undirected graph  .
- The difference between Euler and Hamiltonian paths is that Euler paths use every edge once, while Hamiltonian paths use every vertex once. For example, the graph below has an Euler cycle (a-b-c-d-e-f-a) but no Hamiltonian cycle, because there is no way to visit all six vertices without repeating an edge.

![graph](https://i.stack.imgur.com/4Z4jL.png)

- The existence of Euler and Hamiltonian paths depends on the structure of the graph. There are some necessary and sufficient conditions to determine if a graph has an Euler path or cycle, but there is no general algorithm to find a Hamiltonian path or cycle in a graph. Some graphs have neither Euler nor Hamiltonian paths, some have both, and some have one but not the other  .
- The **Euler's theorem** states that a connected graph has an Euler path if and only if it has exactly zero or two vertices of odd degree. A connected graph has an Euler cycle if and only if it has no vertices of odd degree .
- The **Dirac's theorem** states that a simple graph with n vertices (n >= 3) has a Hamiltonian cycle if every vertex has degree n/2 or greater. This is a sufficient but not necessary condition for the existence of a Hamiltonian cycle .
- Euler and Hamiltonian paths have applications in various fields, such as computer science, operations research, biology, chemistry, and cryptography. For example, the **travelling salesman problem** is a famous problem that asks for the shortest Hamiltonian cycle in a weighted graph, which represents the distances between cities. The **DNA sequencing problem** is a problem that asks for an Euler path in a directed graph, which represents the overlaps between fragments of DNA  .