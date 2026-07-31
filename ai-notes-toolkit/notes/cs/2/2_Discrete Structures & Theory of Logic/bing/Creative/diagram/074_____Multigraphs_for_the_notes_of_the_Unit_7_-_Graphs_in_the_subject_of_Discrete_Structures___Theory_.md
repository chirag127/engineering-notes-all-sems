### Multigraphs

- A **multigraph** is a graph that allows multiple edges (also called parallel edges) between the same pair of vertices .
- A multigraph does not allow loops, which are edges that connect a vertex to itself .
- A multigraph can be represented by an **adjacency list** or an **adjacency matrix**, where each entry indicates the number of edges between two vertices .
- A multigraph can also be represented by an **incidence matrix**, where each row corresponds to a vertex and each column corresponds to an edge, and the entries are 0, 1, or 2 depending on whether the vertex is not incident, incident once, or incident twice to the edge .
- A multigraph can be used to model situations where there are multiple ways to connect two entities, such as roads, flights, or circuits .
- A multigraph can be converted to a simple graph by replacing each set of parallel edges with a single edge with a weight equal to the number of parallel edges .
- A **multidigraph** is a directed graph that allows multiple arcs (also called parallel arcs) between the same pair of vertices .
- A multidigraph can have loops, which are arcs that start and end at the same vertex .
- A multidigraph can be represented by an **adjacency list** or an **adjacency matrix**, where each entry indicates the number of arcs from one vertex to another .
- A multidigraph can also be represented by an **incidence matrix**, where each row corresponds to a vertex and each column corresponds to an arc, and the entries are 0, -1, or 1 depending on whether the vertex is not incident, the tail, or the head of the arc .
- A multidigraph can be used to model situations where there are multiple directions to connect two entities, such as web links, transactions, or workflows .
- A multidigraph can be converted to a simple digraph by replacing each set of parallel arcs with a single arc with a weight equal to the number of parallel arcs .

Here is an example of a multigraph and a multidigraph:

![A multigraph with four vertices and six edges, three of which are parallel between vertices A and B.](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/MultigraphABCD.svg/220px-MultigraphABCD.svg.png)

A multigraph with four vertices and six edges, three of which are parallel between vertices A and B.

![A multidigraph with four vertices and six arcs, two of which are parallel from vertex A to vertex B, and one of which is a loop at vertex C.](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/MultidigraphABCD.svg/220px-MultidigraphABCD.svg.png)

A multidigraph with four vertices and six arcs, two of which are parallel from vertex A to vertex B, and one of which is a loop at vertex C.