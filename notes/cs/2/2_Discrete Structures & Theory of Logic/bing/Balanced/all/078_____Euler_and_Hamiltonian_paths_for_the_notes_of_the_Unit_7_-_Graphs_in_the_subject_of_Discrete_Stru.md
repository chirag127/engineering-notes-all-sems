# Euler and Hamiltonian paths

- Euler and Hamiltonian paths are two types of paths in graphs that have different properties and applications.
- A path in a graph is a sequence of vertices and edges that starts at a vertex and ends at another vertex, such that no edge is repeated.
- A cycle in a graph is a path that starts and ends at the same vertex, such that no edge or vertex (except the first and last) is repeated.

## Euler paths and cycles

- An Euler path is a path that passes through every edge exactly once . If it ends at the initial vertex then it is an Euler cycle .
- An example of an Euler path is shown below:

![Euler path](https://i.stack.imgur.com/0cB0P.png)

- An example of an Euler cycle is shown below:

![Euler cycle](https://i.stack.imgur.com/9Zm7o.png)

- A graph that has an Euler path or cycle is called an Eulerian graph.
- A necessary and sufficient condition for a graph to be Eulerian is that all its vertices have even degree (number of edges incident to them) .
- This condition can be proved by using the handshaking lemma, which states that the sum of the degrees of all vertices in a graph is equal to twice the number of edges.
- If a graph has an Euler path but not an Euler cycle, then it must have exactly two vertices of odd degree, which are the endpoints of the path .

## Hamiltonian paths and cycles

- A Hamiltonian path is a path that passes through every vertex exactly once (NOT every edge) . If it ends at the initial vertex then it is a Hamiltonian cycle .
- An example of a Hamiltonian path is shown below:

![Hamiltonian path](https://i.stack.imgur.com/9Zm7o.png)

- An example of a Hamiltonian cycle is shown below:

![Hamiltonian cycle](https://i.stack.imgur.com/0cB0P.png)

- A graph that has a Hamiltonian path or cycle is called a Hamiltonian graph.
- Unlike Euler paths and cycles, there is no simple necessary and sufficient criteria to determine if a graph has a Hamiltonian path or cycle .
- However, there are some sufficient conditions that guarantee the existence of a Hamiltonian path or cycle, such as the following:
  - If a graph is complete (has an edge between every pair of vertices), then it has a Hamiltonian cycle .
  - If a graph has n vertices and the degree of every vertex is at least n/2, then it has a Hamiltonian cycle (Dirac's theorem) .
  - If a graph has n vertices and the sum of the degrees of any two non-adjacent vertices is at least n, then it has a Hamiltonian cycle (Ore's theorem) .
- There are also some necessary conditions that prevent the existence of a Hamiltonian path or cycle, such as the following:
  - If a graph has a vertex of degree 1, then it cannot have a Hamiltonian cycle .
  - If a graph has a cut-vertex (a vertex whose removal disconnects the graph), then it cannot have a Hamiltonian cycle .

## Applications

- Euler and Hamiltonian paths and cycles have various applications in different fields, such as computer science, mathematics, physics, biology, and engineering.
- Some examples of applications are:
  - Finding an optimal route for a traveling salesman, who wants to visit a set of cities and return to the starting point, while minimizing the total distance traveled. This is an example of a Hamiltonian cycle problem, which is known to be NP-hard (no efficient algorithm is known to solve it) .
  - Finding a way to draw a figure without lifting the pen from the paper and without retracing any line. This is an example of an Euler path or cycle problem, which can be solved efficiently using algorithms such as Fleury's algorithm or Hierholzer's algorithm .
  - Finding a way to decompose a graph into cycles, which can be useful for designing circuits, networks,