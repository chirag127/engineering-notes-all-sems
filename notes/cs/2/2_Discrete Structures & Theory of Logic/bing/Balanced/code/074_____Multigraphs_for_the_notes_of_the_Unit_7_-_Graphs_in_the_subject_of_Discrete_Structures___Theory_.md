# Multigraphs

- A multigraph is a graph that allows multiple edges (also called parallel edges) between the same pair of vertices. A multigraph does not allow loops, which are edges that connect a vertex to itself .
- A multigraph can be represented by an ordered pair G = (V, E), where V is a set of vertices and E is a multiset of unordered pairs of vertices. A multiset is a collection of elements that can have repetitions .
- A multigraph can be visualized by drawing the vertices as points and the edges as curves connecting the vertices. If there are multiple edges between two vertices, they are drawn as separate curves. For example, the following figure shows a multigraph with 4 vertices and 6 edges .

![A multigraph with 4 vertices and 6 edges](https://math.libretexts.org/@api/deki/files/1349/5.2.1.png)

- A multigraph can be used to model situations where there are multiple connections or relationships between the same entities. For example, a multigraph can represent a transportation network, where the vertices are cities and the edges are roads or flights between them. The number of edges between two vertices can indicate the frequency or capacity of the connection .
- Some properties and concepts of simple graphs can be extended to multigraphs, such as degree, adjacency, path, cycle, connectedness, Eulerian and Hamiltonian graphs. However, some definitions and results may differ or require modifications. For example, the degree of a vertex in a multigraph is the sum of the multiplicities of the edges incident to it, where the multiplicity of an edge is the number of times it appears in the multiset E .