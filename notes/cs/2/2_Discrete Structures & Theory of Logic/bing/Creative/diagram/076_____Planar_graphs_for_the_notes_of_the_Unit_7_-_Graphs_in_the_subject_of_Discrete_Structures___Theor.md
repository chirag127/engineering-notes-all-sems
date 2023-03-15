### Planar graphs

- A **planar graph** is a graph that can be drawn on a plane without any edges crossing each other.
- A **plane graph** is a planar graph with a specific way of drawing it on the plane.
- A planar graph can have different plane graphs, depending on how it is drawn.
- A plane graph divides the plane into regions called **faces**.
- The **boundary** of a face is the cycle of edges that encloses it.
- The **degree** of a face is the number of edges on its boundary.
- The **outer face** is the unbounded face of a plane graph.
- The **inner faces** are the bounded faces of a plane graph.
- A **planar embedding** is a way of assigning the faces of a plane graph to the regions of the plane.
- A **planar map** is a plane graph with each face colored with one of a given set of colors.
- A **dual graph** of a plane graph is a graph that has a vertex for each face of the original graph, and an edge for each pair of faces that share a boundary edge in the original graph.

Some properties of planar graphs are:

- **Euler's formula**: For any connected plane graph with n vertices, m edges, and f faces, n - m + f = 2.
- **Kuratowski's theorem**: A graph is planar if and only if it does not contain a subgraph that is a subdivision of K5 (the complete graph on five vertices) or K3,3 (the complete bipartite graph on six vertices).
- **Four color theorem**: Any planar map can be colored with at most four colors, such that no two adjacent faces have the same color.
- **Five color theorem**: Any planar graph can be colored with at most five colors, such that no two adjacent vertices have the same color.
- **Six color theorem**: Any planar graph can be colored with at most six colors, such that no two adjacent vertices have the same color, and the colors of the vertices on the outer face are distinct.
- **Planarity testing**: There are efficient algorithms to test whether a graph is planar or not, such as the Hopcroft-Tarjan algorithm.
- **Planar drawing**: There are efficient algorithms to find a plane graph of a given planar graph, such as the Tutte's spring embedding algorithm.