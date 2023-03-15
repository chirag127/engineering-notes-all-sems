### Isomorphism and Homeomorphism of graphs

- Isomorphism
  - An isomorphism between two graphs G and H is a **bijective** mapping f: V(G) -> V(H) that preserves both **edges** and **non-edges**.
  - That is, for any two vertices u and v in G, u and v are adjacent in G if and only if f(u) and f(v) are adjacent in H.
  - Two graphs that are isomorphic have the same **structure** and **properties**.
  - Example: The following two graphs are isomorphic, with the mapping f(a) = 1, f(b) = 2, f(c) = 3, f(d) = 4, f(e) = 5.

  ```
  a---b     1---2
  |   |     |   |
  c---d ~~~ 3---4
  |         |
  e         5
  ```

- Homeomorphism
  - A homeomorphism between two graphs G and H is a graph isomorphism from some **subdivision** of G to some subdivision of H.
  - A subdivision of a graph is obtained by replacing some edges with paths of length at least 2, without changing the endpoints of the edges.
  - A homeomorphism preserves the **connectivity** and **planarity** of a graph, but not necessarily other properties.
  - Example: The following two graphs are homeomorphic, with the mapping f(a) = 1, f(b) = 2, f(c) = 3, f(d) = 4, f(e) = 5, f(f) = 6, f(g) = 7.

  ```
  a---b     1---2
  |   |     |   |
  c---d ~~~ 3---4
  |   |     |   |
  e---f     5---6
      |         |
      g         7
  ```

- Properties of Homomorphisms
  - A homomorphism from a graph G to a graph H is a mapping (may not be a bijective mapping) h: V(G) -> V(H) that preserves **edges**, but not necessarily non-edges.
  - That is, for any two vertices u and v in G, if u and v are adjacent in G, then h(u) and h(v) are adjacent in H.
  - A homomorphism always preserves **edges** and **connectedness** of a graph.
  - A homomorphism is an isomorphism if it is a bijective mapping.
  - Example: The following is a homomorphism from G to H, with the mapping h(a) = 1, h(b) = 2, h(c) = 3, h(d) = 2, h(e) = 3.

  ```
  a---b     1---2
  |   |     |   |
  c---d ~~~ 3---4
  |         |
  e         5
  ```