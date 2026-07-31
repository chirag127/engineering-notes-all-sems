### Isomorphism and Homeomorphism of graphs

- Isomorphism
  - An isomorphism between two graphs G and H is a **bijective** mapping f: V(G) -> V(H) such that (u,v) is an edge in G if and only if (f(u),f(v)) is an edge in H.
  - In other words, an isomorphism preserves both edges and non-edges between the vertices of the graphs.
  - Two graphs that are isomorphic have the same number of vertices, the same degree sequence, the same number of connected components, and the same number of cycles of any length.
  - Example: The following two graphs are isomorphic, with the mapping f: a -> 1, b -> 2, c -> 3, d -> 4, e -> 5.

  ```
  G:       H:
    a       1
   / \     / \
  b   c   2   3
  |   |   |   |
  d   e   4   5
  ```

- Homeomorphism
  - A homeomorphism between two graphs G and H is a graph isomorphism from some subdivision of G to some subdivision of H.
  - A subdivision of a graph is obtained by replacing some edges with paths of length greater than one, without introducing new vertices or changing the endpoints of the edges.
  - In other words, a homeomorphism preserves edges and connectedness of the graphs, but not necessarily non-edges or the number of vertices.
  - Two graphs that are homeomorphic have the same number of connected components, the same number of cut vertices, and the same number of bridges.
  - Example: The following two graphs are homeomorphic, with the subdivision of G obtained by replacing the edge (a,c) with the path (a,b,c) and the subdivision of H obtained by replacing the edge (1,3) with the path (1,2,3).

  ```
  G:       H:
    a       1
   / \     / \
  b   c   2   3
  |   |   |   |
  d   e   4   5
  ```