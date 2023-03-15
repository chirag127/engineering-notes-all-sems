### Representation of graphs

Graphs can be represented in various ways, including:

1. **Adjacency matrix:** A two-dimensional matrix where the element in the i-th row and j-th column represents the edge between vertex i and vertex j. The value of the element can be binary (0 or 1) to represent the presence or absence of an edge, or it can be a weight to represent the cost of the edge.

2. **Incidence matrix:** A two-dimensional matrix where the element in the i-th row and j-th column represents the incidence of vertex i and edge j. The value of the element can be binary (0 or 1) to represent the presence or absence of an incidence, or it can be a weight to represent the cost of the incidence.

3. **Adjacency list:** A collection of lists where the i-th list contains the neighbors of vertex i. This representation is more space-efficient than the adjacency matrix for sparse graphs.

4. **Edge list:** A list of edges, where each edge is represented by a pair of vertices. This representation is more space-efficient than the adjacency matrix for sparse graphs.

These are some of the common ways to represent graphs. Each representation has its own advantages and disadvantages, and the choice of representation depends on the specific problem and the operations that need to be performed on the graph.