# Isomorphism and Homeomorphism of graphs

## Isomorphism

- Two graphs G and H are **isomorphic** if there is a **bijection** (one-to-one and onto) f from the vertex set of G to the vertex set of H such that two vertices u and v are adjacent in G if and only if f(u) and f(v) are adjacent in H.
- Isomorphism preserves the **structure** and **properties** of graphs, such as the number of vertices, the number of edges, the degree sequence, the connectivity, the cycles, etc.
- Isomorphic graphs are **equivalent** in terms of graph theory, and they are often denoted by G ≅ H.
- To check if two graphs are isomorphic, we can try to find an isomorphism f by **matching** the vertices of G and H according to their degrees and neighborhoods, or by using some **invariants** (properties that are preserved under isomorphism) to rule out the possibility of isomorphism.
- For example, the following two graphs are isomorphic, and one possible isomorphism is f(a) = 1, f(b) = 2, f(c) = 3, f(d) = 4, f(e) = 5.

![isomorphic graphs](https://www.tutorialspoint.com/isomorphism-and-homeomorphism-of-graphs/images/isomorphic_graphs.jpg)

## Homeomorphism

- A **subdivision** of a graph G is a graph obtained by replacing each edge of G by a path of one or more edges, such that no new vertices are introduced except on edges.
- A **smoothing** of a graph G is an inverse operation of subdivision, that is, removing a vertex of degree 2 and replacing the two edges incident to it by a single edge.
- Two graphs G and H are **homeomorphic** if there is a graph isomorphism from some subdivision of G to some subdivision of H.
- Homeomorphism is a weaker notion of equivalence than isomorphism, as it allows the graphs to have different numbers of vertices and edges, as long as they have the same **topological** shape.
- Homeomorphic graphs have the same **Euler characteristic**, **genus**, **crossing number**, and **planarity**.
- To check if two graphs are homeomorphic, we can try to find a homeomorphism by **subdividing** or **smoothing** the edges of G and H until they have the same structure, or by using some **invariants** (properties that are preserved under homeomorphism) to rule out the possibility of homeomorphism.
- For example, the following two graphs are homeomorphic, and one possible homeomorphism is obtained by subdividing the edge bd in G and the edge 24 in H, and then matching the vertices as follows: f(a) = 1, f(b) = 2, f(c) = 3, f(d) = 4, f(e) = 5, f(x) = y.

![homeomorphic graphs](https://www.tutorialspoint.com/isomorphism-and-homeomorphism-of-graphs/images/homeomorphic_graphs.jpg)

: Isomorphism and Homeomorphism of graphs - tutorialspoint.com
: Homeomorphism (graph theory) - Wikipedia