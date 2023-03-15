### Multigraphs

- A **multigraph** is a graph that allows multiple edges (also called parallel edges) between the same pair of vertices  .
- A multigraph does not allow loops, which are edges that connect a vertex to itself .
- A multigraph can be represented by an **adjacency matrix**, where each entry indicates the number of edges between two vertices, or by an **incidence matrix**, where each entry indicates the number of times an edge is incident to a vertex .
- A multigraph can also be represented by a **diagram**, where vertices are drawn as points and edges are drawn as curves connecting the points. Multiple edges are drawn as separate curves, and the order of the edges does not matter .
- A multigraph can be used to model situations where there are multiple ways to connect two entities, such as roads, flights, or communication channels .
- A multigraph can have different properties, such as being **connected**, **bipartite**, **planar**, or **Eulerian**, depending on the structure of its vertices and edges .
- A multigraph can be converted into a simple graph by removing the multiple edges or by replacing them with weighted edges that indicate the number of original edges .

Here is an example of a multigraph with 5 vertices and 7 edges:

![Multigraph example](https://mathworld.wolfram.com/images/eps-gif/Multigraph_1000.gif)

: Simple Graph, Multigraph and Pseudo Graph - DISCRETE MATHEMATICS LECTURES
: Multigraph - Wikipedia
: discrete mathematics - Clarification on the definition of multigraph ...
: 5.2: Multigraphs- Loops and Multiple Edges - Mathematics LibreTexts
: Multigraph -- from Wolfram MathWorld