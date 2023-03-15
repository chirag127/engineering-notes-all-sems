### Isomorphism and Homeomorphism of graphs

- Isomorphism and homeomorphism are two concepts in graph theory that relate to the similarity and equivalence of graphs.
- A graph is a set of vertices and edges that connect some pairs of vertices. A graph can be represented by a diagram where vertices are points and edges are lines or curves.
- Two graphs are **isomorphic** if they have the same number of vertices and there is a one-to-one correspondence between the vertices of the two graphs such that any two vertices are adjacent in one graph if and only if they are adjacent in the other graph. In other words, isomorphic graphs have the same shape and structure, but may have different labels or orientations.
- For example, the following two graphs are isomorphic:

![isomorphic graphs](https://www.tutorialspoint.com/images/isomorphic_graphs.jpg)

- A **graph isomorphism** is a bijective function that maps the vertices of one graph to the vertices of another graph, preserving the adjacency relation. For example, the function f that maps A to 1, B to 2, C to 3, D to 4, and E to 5 is a graph isomorphism from the first graph to the second graph in the above figure.
- Two graphs are **homeomorphic** if they can be obtained from each other by a sequence of subdivisions and smoothings. A **subdivision** of a graph is the operation of replacing an edge by a path of two or more edges. A **smoothing** of a graph is the inverse operation of removing a vertex of degree two and joining its two neighbors by an edge. In other words, homeomorphic graphs have the same topology, but may have different numbers of vertices or edges.
- For example, the following two graphs are homeomorphic:

![homeomorphic graphs](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Homeomorphic_graphs.svg/1200px-Homeomorphic_graphs.svg.png)

- A **graph homeomorphism** is a graph isomorphism from some subdivision of one graph to some subdivision of another graph. For example, the function g that maps a to 1, b to 2, c to 3, d to 4, e to 5, f to 6, g to 7, h to 8, i to 9, and j to 10 is a graph homeomorphism from the first graph to the second graph in the above figure.
- Properties of isomorphisms and homeomorphisms:
  - Isomorphism is an equivalence relation on graphs, meaning that it is reflexive, symmetric, and transitive. That is, every graph is isomorphic to itself, if two graphs are isomorphic then they are isomorphic in both directions, and if two graphs are isomorphic to a third graph then they are isomorphic to each other.
  - Homeomorphism is also an equivalence relation on graphs, with the same properties as isomorphism.
  - Every isomorphic pair of graphs is also homeomorphic, but the converse is not true. That is, isomorphism implies homeomorphism, but homeomorphism does not imply isomorphism.
  - Isomorphism and homeomorphism are both preserved by graph operations such as adding or deleting vertices or edges, or taking subgraphs or complements. That is, if two graphs are isomorphic or homeomorphic, then any graph obtained by applying the same operation to both graphs is also isomorphic or homeomorphic, respectively.