Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on planar graphs for the unit 7 of discrete structures and theory of logic.

### Planar graphs

- A **planar graph** is a graph that can be drawn on a plane without any edges crossing each other.
- A **plane graph** is a planar graph with a specific way of drawing it on a plane, such that each edge is represented by a curve and each vertex by a point.
- A planar graph can have more than one plane graph, depending on how it is drawn.
- A **face** is a region of the plane that is bounded by edges of a plane graph.
- The **boundary** of a face is the set of edges and vertices that surround it.
- The **degree** of a face is the number of edges on its boundary.
- The **outer face** is the face that contains the infinite region outside the plane graph.
- The **inner faces** are the faces that do not contain the infinite region.

#### Properties of planar graphs

- A planar graph with n vertices, e edges and f faces satisfies the **Euler's formula**: n - e + f = 2.
- A planar graph with n vertices and e edges has at most 3n - 6 edges, if n >= 3.
- A planar graph with n vertices and e edges has at most 2n - 4 faces, if n >= 3.
- A planar graph has at least one vertex of degree at most 5.
- A planar graph cannot contain a subgraph that is a subdivision of K5 (the complete graph on 5 vertices) or K3,3 (the complete bipartite graph on 3 and 3 vertices).
- A planar graph is **bipartite** if and only if it has no odd cycles.
- A planar graph is **Hamiltonian** if and only if it is 3-connected.
- A planar graph is **dual** to another planar graph if there is a one-to-one correspondence between their faces and vertices, such that two faces are adjacent in one graph if and only if their corresponding vertices are adjacent in the other graph.