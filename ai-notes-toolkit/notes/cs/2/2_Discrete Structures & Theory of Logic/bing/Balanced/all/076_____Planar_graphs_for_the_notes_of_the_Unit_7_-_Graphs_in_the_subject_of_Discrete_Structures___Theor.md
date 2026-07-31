# Planar Graphs

- A **planar graph** is a graph that can be drawn on a plane without any edges crossing each other.
- A **plane graph** is a planar graph with a specific way of drawing it on the plane.
- A planar graph can have different plane graphs, depending on how it is drawn.
- A plane graph divides the plane into regions called **faces**.
- The **boundary** of a face is the cycle of edges that encloses it.
- The **degree** of a face is the number of edges on its boundary.
- The **outer face** is the unbounded face that contains the infinite region outside the graph.
- The **inner faces** are the bounded faces that are inside the graph.

## Properties of Planar Graphs

- A planar graph with $n$ vertices, $e$ edges, and $f$ faces satisfies the **Euler's formula**: $n - e + f = 2$.
- A planar graph with $n \geq 3$ vertices has at most $3n - 6$ edges.
- A planar graph with $n \geq 3$ vertices and no cycles of length 3 has at most $2n - 4$ edges.
- A planar graph is **bipartite** if and only if it has no cycles of odd length.
- A planar graph has a **dual graph** that is also planar and has a vertex for each face and an edge for each pair of adjacent faces.
- A planar graph is **Hamiltonian** if and only if its dual graph is Hamiltonian.
- A planar graph is **3-colorable** if and only if it has no subgraph that is a subdivision of $K_4$ (the complete graph on 4 vertices).
- A planar graph is **4-colorable**. This is the famous **Four Color Theorem**.