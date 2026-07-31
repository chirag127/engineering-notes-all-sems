### Isomorphism and Homeomorphism of graphs

- Isomorphism and homeomorphism are two concepts in graph theory that deal with the similarity and equivalence of graphs.
- A graph is a set of vertices and edges that connect some pairs of vertices. A graph can be represented by a diagram where vertices are shown as dots and edges are shown as lines or curves.
- Two graphs are **isomorphic** if they have the same number of vertices and edges, and there is a one-to-one correspondence between their vertices that preserves the adjacency of vertices. That is, two vertices are adjacent in one graph if and only if their corresponding vertices are adjacent in the other graph.
- An **isomorphism** is a bijective function that maps the vertices of one graph to the vertices of another graph, such that the edge relation is preserved. For example, the following two graphs are isomorphic, and the function f is an isomorphism:

![isomorphic graphs](https://i.stack.imgur.com/9Zy6f.png)

- Two graphs are **homeomorphic** if they can be obtained from each other by a sequence of subdivisions and contractions of edges. A **subdivision** of an edge is the operation of replacing an edge by a path of two or more edges, with a new vertex on each internal edge. A **contraction** of an edge is the inverse operation of removing an edge and identifying its endpoints as a single vertex. For example, the following two graphs are homeomorphic, and the sequence of operations shows how to transform one graph into the other:

![homeomorphic graphs](https://i.stack.imgur.com/4iY0y.png)

- A **homeomorphism** is a graph isomorphism from some subdivision of one graph to some subdivision of another graph. For example, the function g is a homeomorphism from the first graph to the second graph in the above example:

![homeomorphism](https://i.stack.imgur.com/9Zy6f.png)

- Properties of isomorphisms and homeomorphisms:
  - Isomorphism is an equivalence relation on graphs, that is, it is reflexive, symmetric and transitive. Homeomorphism is also an equivalence relation on graphs.
  - Isomorphism preserves the degree of vertices, that is, the number of edges incident to a vertex. Homeomorphism does not preserve the degree of vertices, as subdivision and contraction can change the degree of vertices.
  - Isomorphism preserves the number of cycles, that is, the closed paths in a graph. Homeomorphism does not preserve the number of cycles, as subdivision and contraction can create or destroy cycles.
  - Isomorphism preserves the planarity of graphs, that is, the property of being drawable on a plane without crossing edges. Homeomorphism also preserves the planarity of graphs, as subdivision and contraction do not affect the planarity of graphs.