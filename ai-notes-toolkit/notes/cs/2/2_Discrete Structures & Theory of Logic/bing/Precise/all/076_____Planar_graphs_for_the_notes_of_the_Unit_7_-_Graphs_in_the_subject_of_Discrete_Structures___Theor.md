# Planar Graphs

A planar graph is a type of graph that can be drawn on a plane without any of its edges crossing. In other words, it can be embedded in the plane in such a way that its edges intersect only at their endpoints. Here are some key points to remember about planar graphs:

- A graph is planar if and only if it does not contain a subgraph that is homeomorphic to K5 (the complete graph on five vertices) or K3,3 (the complete bipartite graph on six vertices).

- A planar graph can be divided into regions, called faces, by its edges. Each face is bounded by a cycle of edges, and the number of faces is given by Euler's formula: V - E + F = 2, where V is the number of vertices, E is the number of edges, and F is the number of faces.

- A planar graph can be colored using only four colors, such that no two adjacent vertices have the same color. This is known as the Four Color Theorem.

- Planar graphs have many applications, including in the design of electronic circuits, the layout of maps, and the study of molecules in chemistry.

- Some common algorithms for testing whether a graph is planar include the Hopcroft-Tarjan algorithm and the Boyer-Myrvold algorithm.
