### Isomorphism and Homeomorphism of graphs

- Isomorphism and homeomorphism are two concepts in graph theory that relate to the similarity and equivalence of graphs.
- A graph is a set of vertices and edges that connect some pairs of vertices. A graph can be represented by a diagram where vertices are points and edges are lines or curves.
- Two graphs are **isomorphic** if they have the same number of vertices and there is a one-to-one correspondence between the vertices of the two graphs that preserves the adjacency of the vertices. That is, two vertices are adjacent in one graph if and only if their corresponding vertices are adjacent in the other graph.
- An **isomorphism** is a bijective function that maps the vertices of one graph to the vertices of another graph in such a way that preserves the adjacency of the vertices. An isomorphism can also be seen as a relabeling of the vertices of one graph to match the vertices of another graph.
- For example, the following two graphs are isomorphic, and the function f that maps A to 1, B to 2, C to 3, D to 4, and E to 5 is an isomorphism.

![isomorphic graphs](https://i.stack.imgur.com/0f7Zu.png)

- Two graphs are **homeomorphic** if they can be obtained from each other by a sequence of subdivisions and smoothings. A **subdivision** of a graph is the operation of replacing an edge by a path of two or more edges. A **smoothing** of a graph is the inverse operation of subdivision, that is, replacing a path of two or more edges by a single edge.
- A **homeomorphism** is a graph isomorphism from some subdivision of one graph to some subdivision of another graph. A homeomorphism can also be seen as a deformation of one graph into another graph by bending, stretching, or shrinking the edges, but not breaking or crossing them.
- For example, the following two graphs are homeomorphic, and the function g that maps A to 1, B to 2, C to 3, D to 4, E to 5, F to 6, and G to 7 is a homeomorphism.

![homeomorphic graphs](https://i.stack.imgur.com/0f7Zu.png)

- Properties of isomorphisms and homeomorphisms:
  - Isomorphism and homeomorphism are equivalence relations on the set of graphs, that is, they are reflexive, symmetric, and transitive.
  - Isomorphism and homeomorphism preserve some properties of graphs, such as the number of vertices, the number of edges, the degree of vertices, the connectivity, the planarity, the Euler characteristic, etc.
  - Isomorphism is a stronger relation than homeomorphism, that is, every isomorphic pair of graphs is also homeomorphic, but not vice versa. For example, the following two graphs are homeomorphic but not isomorphic, because they have different numbers of edges.

![homeomorphic but not isomorphic graphs](https://i.stack.imgur.com/0f7Zu.png)

- Applications of isomorphism and homeomorphism:
  - Isomorphism and homeomorphism are useful for studying the structure and properties of graphs, and for classifying graphs into different types or classes.
  - Isomorphism and homeomorphism can also be used to model and compare different objects or systems that can be represented by graphs, such as molecules, networks, maps, circuits, etc.