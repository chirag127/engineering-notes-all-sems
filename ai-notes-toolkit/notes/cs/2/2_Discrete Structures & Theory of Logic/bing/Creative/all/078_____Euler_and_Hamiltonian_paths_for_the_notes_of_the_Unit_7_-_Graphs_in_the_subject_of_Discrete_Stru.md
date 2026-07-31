# Euler and Hamiltonian paths

- Euler and Hamiltonian paths are two types of paths in graphs that have different properties and applications.
- A **path** in a graph is a sequence of vertices connected by edges, such that no vertex is repeated.
- A **cycle** in a graph is a path that starts and ends at the same vertex, such that no other vertex is repeated.

## Euler paths and cycles

- An **Euler path** is a path that passes through every **edge** exactly once. If it ends at the initial vertex then it is an **Euler cycle**.
- For example, the graph below has an Euler path from A to D, and an Euler cycle from A to A.

![Euler path and cycle](https://i.imgur.com/0Zw0w8L.png)

- An Euler path or cycle can exist both in a directed and undirected graph, as long as the graph is connected and has no isolated vertices.
- A necessary and sufficient condition for the existence of an Euler path or cycle in a graph is based on the degrees of the vertices.
  - A graph has an Euler cycle if and only if every vertex has an **even degree**.
  - A graph has an Euler path but not an Euler cycle if and only if exactly two vertices have an **odd degree**, and these are the endpoints of the path.
  - A graph has no Euler path or cycle if and only if more than two vertices have an **odd degree**.

## Hamiltonian paths and cycles

- A **Hamiltonian path** is a path that passes through every **vertex** exactly once. If it ends at the initial vertex then it is a **Hamiltonian cycle**.
- For example, the graph below has a Hamiltonian path from A to E, and a Hamiltonian cycle from A to A.

![Hamiltonian path and cycle](https://i.imgur.com/4q1lq6i.png)

- A Hamiltonian path or cycle can exist both in a directed and undirected graph, as long as the graph is connected and has no isolated vertices.
- Unlike Euler paths and cycles, there is no simple necessary and sufficient condition for the existence of a Hamiltonian path or cycle in a graph. However, there are some sufficient conditions that can be used to check if a graph has a Hamiltonian path or cycle, such as the following:
  - If a graph has **n** vertices and the degree of every vertex is at least **n/2**, then the graph has a Hamiltonian cycle. This is known as **Dirac's theorem**.
  - If a graph has **n** vertices and the sum of the degrees of any two non-adjacent vertices is at least **n**, then the graph has a Hamiltonian cycle. This is known as **Ore's theorem**.
  - If a graph is **complete**, meaning that every pair of vertices is connected by an edge, then the graph has a Hamiltonian cycle. This is a special case of Dirac's theorem.

## Applications of Euler and Hamiltonian paths and cycles

- Euler and Hamiltonian paths and cycles have various applications in different fields, such as computer science, mathematics, engineering, biology, and more. Some examples are:
  - The **traveling salesman problem** is a famous optimization problem that asks for the shortest Hamiltonian cycle in a weighted graph, where the weights represent the distances or costs between the vertices. This problem has applications in logistics, scheduling, routing, and more.
  - The **Chinese postman problem** is another optimization problem that asks for the shortest Euler cycle or path in a weighted graph, where the weights represent the distances or costs between the edges. This problem has applications in mail delivery, garbage collection, street sweeping, and more.
  - The **de Bruijn sequence** is a cyclic sequence of symbols that contains every possible subsequence of a given length exactly once. For example, the de Bruijn sequence of length 2 over the alphabet {0, 1} is 00110. This sequence can be constructed by finding an Euler cycle in a de Bruijn graph, which is a directed graph where the vertices are all possible subsequences of a given length, and the edges are labeled by the symbols that extend the subsequences. This sequence has applications in coding theory, cryptography, combinatorics, and more.
  - The **genome assembly problem** is a problem in bioinformatics that asks for the reconstruction of a DNA sequence from a set of overlapping fragments. This problem can be modeled by finding a Hamiltonian path in a de Bruijn